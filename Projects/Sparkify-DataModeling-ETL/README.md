![Alt text](img/star-schema.jpg?raw=true "star schema")

To run the project locally follow the steps below:

Step 1:

Run a postgres instance on Docker

a) Docker pull postgres:latest

b) Docker run --name randydb-postgres -e POSTGRES_PASSWORD=datapassword -d -p 5432:5432 postgres

c) Docker exec -it randydb-postgres bash

d) psql -U postgres

e) create Database student_randy

The database should now be ready to be queried.


Step 2:

Create all the tables before inserting data.

a) Run create_tables.py


Step 3: 

Run the Extract, Transform and Load process.

a) Run etl.py



After etl.py is done organizing our files you can head over to the test.pynb notebook to query our fully load database.

