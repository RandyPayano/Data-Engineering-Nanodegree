# Data Modeling with Apache Cassandra

## Introduction

Sparkify, a music streaming startup, wanted to analyze the data they'd collected on songs and user activity on their new streaming app.
They are especially interested in knowing what songs users are listening to. Currently, their data is stored in a directory of CSV files,
and they would like a data engineer to create an Apache Cassandra database that will allow them to answer questions on play data.
Given that we need to have the queries we want to run before we create our Cassandra tables in order to optimize our database,
the Sparkify analytics team has provided us with the following analytical queries:

1. Provide the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4

2. Provide the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182

3. Provide every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own'

## Datasets

Our dataset consists of individual CSV files inside the event_data directory.

```
Example files:
event_data/2018-11-08-events.csv
event_data/2018-11-09-events.csv

```
## ETL Pipeline

To complete the ETL process, we will iterate over our individual CSV files inside event_data directory and create a single event data file using a python script, which we will then use to insert data into our Apache Cassandra tables to answer our analytical queries.


## Running project
```
1. Follow the instructions on running the Cassandra image locally outlined below.
2. Run the "Apache_Cassandra_ETL.ipynb" notebook from the top.
3. Verify that our tables satisfy our analytical queries. 
```

## Set up a cassandra container with Docker:

```
docker pull cassandra
docker run --name cassandra-container -p 9042:9042 -d cassandra:latest
```
```
You should be able to connect to this container from the ETL notebook using:

from cassandra.cluster import Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()

```
Make sure to STOP the container after running the ETL process:
```
docker stop cssandra-container
docker rm cassandra-container
```
