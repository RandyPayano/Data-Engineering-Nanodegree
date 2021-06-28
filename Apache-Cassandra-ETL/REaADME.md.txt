# Data Modeling with Apache Cassandra

## Introduction

Sparkify, a music streaming startup, wanted to analyze the data they'd collected on songs and user activity on their new streaming app.
They are especially interested in knowing what songs users are listening to. Currently, their data is stored in a directory of CSV files,
and they would like a data engineer to create an Apache Cassandra database that will allow them to answer questions on play data.
Given that we need to have the queries we want to run before we create our Cassandra tables in order to optimize our database,
the Sparkify analytics team has provided us with the following analytical queries:

1. Provide the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4:

2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182:

3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own':

## Project Description

### To run the .ipynb file, follow instructions below:

1. Load the Docker image using the instructions below.
2. Make sure the unzipped `event_data` folder is in the same directory as the "Project_1B_Data_Modeling_with_Cassandra.ipynb" file.
3. Run all cells in the "Project_1B_Data_Modeling_with_Cassandra.ipynb" file.
4. Verify that all three queries return the expected data based on the three query requirement questions in the notebook.

## ETL Pipeline
I was provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables. The provided project template takes care of all the imports and provides a structure for an ETL pipeline that I needed to process this data.

## To run locally follow the following steps to set up a cassandra container with Docker:

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
