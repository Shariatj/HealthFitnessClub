
# Health Fitness Club

### Overview

Name: Shariat Jahan Shanu

ID: 101285602

This project was developed as part of the requirements for COMP3005 FInal project V2

[Link to Video Demonstration](https://youtu.be/S3xLxGlhGHA)

### Setting up the PostgreSQL Database

- Launch pgAdmin 4.
- Create a new database. I am using `healthfitnessclub`.
- Open the query tool for the database you just created and run the `DDL.sql` and then `DML.sql` file in `SQL`.
- This will create the required tables and populate it with initial data.


### Installing Python Dependencies

Install [psycopg 3](https://pypi.org/project/psycopg/):

```bash
pip3 install --upgrade pip           # to upgrade pip
pip3 install "psycopg[binary,pool]"  # to install package and dependencies
```
### Files

1. The ER model Diagram and database schema and mapping are in `Conceptual_Design.pdf`
2. `member_functions.py` handles member operations
3. `trainer_functions.py` handles trainer operations
4. `admin_functions.py` handles administrative staff operations
5. `main.py` is the main function to operaton this project


### Running the Application

1. Update the database connection settings at the top of `main.py` to match your PostgreSQL database connection details.

2. Execute the following command in the terminal:

```bash
python3 ./main.py
```

Enjoy managing your Health fitness club!
