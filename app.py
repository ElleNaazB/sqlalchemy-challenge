# Importing the dependencies.
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, func
import datetime as dt

#################################################
# Database Setup
#################################################
# Creating the database engine.
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Automapping the base.
Base = automap_base()
# Reflecting the tables from the database.
Base.prepare(engine, reflect=True)

# Saving references to each table.
Station = Base.classes.station
Measurement = Base.classes.measurement

# Creating our session link to the DB.
Session = sessionmaker(bind=engine)

#################################################
# Flask Setup
#################################################
# Creating the Flask application.
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """Listing all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )

def calculate_dates():
    """Calculating the dates for data retrieval."""
    with Session() as session:
        most_recent_date_str = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    most_recent_date = dt.datetime.strptime(most_recent_date_str, '%Y-%m-%d')
    one_year_before = most_recent_date - dt.timedelta(days=365)
    return one_year_before

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Retrieving precipitation data."""
    one_year_before = calculate_dates()
    with Session() as session:
        precipitation_data = session.query(Measurement.date, Measurement.prcp)\
                                    .filter(Measurement.date > one_year_before)\
                                    .order_by(Measurement.date).all()
    
    all_precip = [{date: prcp for date, prcp in precipitation_data}]
    return jsonify(all_precip)

@app.route("/api/v1.0/stations")
def stations():
    """Retrieving station data."""
    with Session() as session:
        stations_list = session.query(Station.station).all()
    
    all_stations = list(np.ravel(stations_list))
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Retrieving temperature observations."""
    one_year_before = calculate_dates()
    with Session() as session:
        temp_data = session.query(Measurement.date, Measurement.tobs)\
                           .filter(Measurement.date > one_year_before)\
                           .filter(Measurement.station == "USC00519281")\
                           .order_by(Measurement.date).all()
    
    all_temps = [{date: temp for date, temp in temp_data}]
    return jsonify(all_temps)

def calculate_temps(start_date, end_date=None):
    """Calculating temperatures."""
    with Session() as session:
        sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
        if end_date:
            temps = session.query(*sel).filter(Measurement.date >= start_date, Measurement.date <= end_date).one()
        else:
            temps = session.query(*sel).filter(Measurement.date >= start_date).one()
    return temps

@app.route("/api/v1.0/<start>")
def start(start):
    """Calculating temperatures from a start date."""
    lowest_temp, highest_temp, avg_temp = calculate_temps(start)
    return jsonify([{"Lowest Temperature": lowest_temp, "Highest Temperature": highest_temp, "Average Temperature": avg_temp}])

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Calculating temperatures between a start and end date."""
    lowest_temp, highest_temp, avg_temp = calculate_temps(start, end)
    return jsonify([{"Lowest Temperature": lowest_temp, "Highest Temperature": highest_temp, "Average Temperature": avg_temp}])

if __name__ == '__main__':
    app.run(debug=True)
