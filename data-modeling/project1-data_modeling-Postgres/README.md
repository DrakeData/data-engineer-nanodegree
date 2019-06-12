# Introduction
This is the first project for Udacity's Data Engineering nanodegree. 

A startup company that provides music streaming, called Sparkify, is looking to analyst user data. The songs details and the user activity data from the application are currently available and stored in the format of JSON.  

The analytic team is particularly interested in understanding what songs users are listening to, but would like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. This is where I come in.

The data we receive is in JSON files, which can take time to analysis. Our goal is to import the data into a Postgres database and use modeling techniques to allow fast retrieval of data. In this case, we will use the STAR schema.

The STAR schema consists of one or more FACT tables referencing any number of DIMENSION tables. These tables can help Sparkify solve simplified common business logic. This logic includes:
* What song should play next for the Sparkify user, based on past behavior.
* Which song an user would be interested in listening to at that particular point of time.

Sparkify would use the STAR schema like this:
* FACT Table: songplays: attributes referencing to the dimension tables.
* DIMENSION Tables: users, songs, artists and time table.

The above databases will help the analytics team at Sparkify to run different kinds of analysis to recommend a Sparkify user.
* Favorite songs of user based on the week day: By joining songplay and songs and user table based on level.
* Recent listened to songs: By joining songplays and user table can show recommendation on the app based on subscription level.
* Help in recommending most popular songs of the day/week.

# ETL Pipeline
* Create FACT table from the dimensison tables and log_data called songplays.
* Create DIMENSION songs and artist table from extracting songs_data by selected columns.
* Create DIMENSION users and time tables from extracting log_data by selected columns.

# Usage
1. test.ipynb displays the first few rows of each table to let you check your database.
2. create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
5. sql_queries.py contains all your sql queries, and is imported into the last three files above.

# Execute the below files in order each time before pipeline.
1. create_tables.py
   $ python3 create_tables.py
2. etl.ipynb/et.py
   $ python3 etl.py
3. test.ipynb

