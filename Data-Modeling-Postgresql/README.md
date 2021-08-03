<h1>Introduction</h1>

Sparkify, a startup, wants to analyze the data they've gathered on songs and user activity on their new music streaming app. The analytics team is particularly interested in learning about the songs that users are listening to. They currently lack an easy way to query their data, which is stored in a directory of JSON logs on user activity on the app,
in addition to a directory containing JSON metadata on the songs in their app.

They would like to build a Postgres database with tables optimized for song play analysis queries. To conduct our analysis, several steps must be completed, including the creation of a database schema and an ETL pipeline. The database and ETL pipeline will be validated against the expected results by running SQL queries provided by Sparkify's analytics team.

As the Data Engineer assigned to this project, I will define fact and dimension tables for a star schema for a specific analytic focus, as well as write an ETL pipeline that uses Python and SQL to transfer data from files in two local directories into these tables in Postgres.

<h2>Song Dataset</h2>

Song datasets are organized in subdirectories under /data/song data. Here is an example of one of these files:

ex: song_data/A/B/C/TRABCEI128F424C983.json

```{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}```

<h2>Log Dataset</h2>
All json files in the /data/log data directory are nested in subdirectories. A single row from each file is shown below as an example:

```{"artist":"Slipknot","auth":"Logged In","firstName":"Aiden","gender":"M","itemInSession":0,"lastName":"Ramirez","length":192.57424,"level":"paid","location":"New York-Newark-Jersey City, NY-NJ-PA","method":"PUT","page":"NextSong","registration":1540283578796.0,"sessionId":19,"song":"Opium Of The People (Album Version)","status":200,"ts":1541639510796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.1) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"20"}```

You could see it as a Panda DataFrame by typing the following line in your Notebook 

```pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True)```
![Alt text](img/log-data.png?raw=true "Log data Dataframe")

To provide an easy way to access and manipulate the data with simple JOIN statements, I came up with the following Star Schema design. 

![Alt text](img/star-schema.jpg?raw=true "star schema")


<h1>Files in repository</h1>

1) test.ipynb displays the first few rows of each table to check the database.
2) create_tables.py drops and creates all ables. Run this file to reset all tables before each time before running the ETL scripts.
3) etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook was used to architech the ETL process for each of the tables.
4) etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5) sql_queries.py contains all your sql queries, and is imported into the last three files above.
6) Data folder contains your data which resides in JSON log files. 



*** To run the above files you can use MS Visual Studio and Jupyter Notebook ***

*** For this Project we will host our postgres server on a Docker container, below are instructions on how to run the complete project**


To run the project locally clone this repository and then follow the steps below:

```git clone https://github.com/RandyPayano/Sparkify-DataModeling-ETL.git```

<h3>Step 1:</h3>

<b>Run a postgres instance on Docker</b>

a) ```Docker pull postgres:latest```

b) ```Docker run --name randydb-postgres -e POSTGRES_PASSWORD=datapassword -d -p 5432:5432 postgres```

c) ```Docker exec -it randydb-postgres bash```

d) ```psql -U postgres```

e) ```Create Database student_randy;```

The database is now ready to be queried.

For more details on this process, I have written an article on Medium. 
https://randypayano.medium.com/running-a-postgres-server-on-docker-da2268acf00f

<h3>Step 2:</h3>

<b>Create all the tables before inserting data (this will check if the tables already existed, delete, and re-create them)</b>

a) ```Run create_tables.py```

<h3>Step 3:</h3> 

<b>Run the Extract, Transform and Load process</b>

a) ```Run etl.py```

![Alt text](img/processed.jpg?raw=true "Files processed")

<b>Our files have been processed, lastly open up test.ipynb in Jupyter Notebook to test our analytical queries! </b>

![Alt text](img/testing_dataset.jpg?raw=true "Testing our database")