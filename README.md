# Climate Data Explorer
This project simplifies data exploration and analysis of a climate database using Python and SQLAlchemy. It employs SQLAlchemy for database queries, Pandas for data handling, and Matplotlib for visualization. Additionally, it offers a Flask-based API to access the climate data.

## Details 
This project is devided to two sections:

##  Analyzing and Explore the Climate Data
The first part undertakes a basic climate analysis and data exploration of a climate database using Python and SQLAlchemy. It specifically employs SQLAlchemy ORM queries, Pandas, and Matplotlib to analyze the data. The process involves several key steps, starting with using the provided files (<a href= "https://github.com/ElleNaazB/sqlalchemy-challenge/blob/main/climate_starter.ipynb"> climate_starter.ipynb </a>, <a href ="https://github.com/ElleNaazB/sqlalchemy-challenge/blob/main/Resources/hawaii.sqlite"> hawaii.sqlite</a>, <a href= "https://github.com/ElleNaazB/sqlalchemy-challenge/blob/main/Resources/hawaii_measurements.csv">hawaii_measurements.csv</a> , and <a href= "https://github.com/ElleNaazB/sqlalchemy-challenge/tree/main/Resources">hawaii_stations.csv</a> ). The first step is to connect to the SQLite database using SQLAlchemy's create_engine() function, then reflect the database tables into classes using automap_base(), saving references to these classes as 'station' and 'measurement'. A connection between Python and the database is established by creating an SQLAlchemy session.

## Designing Climate App
<a href ="https://github.com/ElleNaazB/sqlalchemy-challenge/blob/main/app.py">The second part of this project </a> progresses to design a Flask API based on the climate data analyses previously conducted. The API uses Flask to establish various routes for accessing the climate data analysis results:

- The homepage (/) introduces users to the API, listing all available routes for easy navigation.

- The /api/v1.0/precipitation route transforms the results of the precipitation analysis into a dictionary, where dates serve as keys and precipitation values as the corresponding values. It then returns this data as a JSON object, making the last 12 months of precipitation data easily accessible.

- Through /api/v1.0/stations, the API provides a JSON list of all stations from the dataset, allowing users to explore different sources of climate data.

- The /api/v1.0/tobs route focuses on the most active station, querying temperature observations for the last year. This data is then offered as a JSON list, showcasing temperature trends over the previous year.

- This Flask API makes it straightforward to access and interact with the climate analysis findings, offering a user-friendly way to explore important climate trends and data points.
