
# Student Records Management Application

### Overview

Name: Shariat Jahan Shanu

ID: 101285602

This project was developed as part of the requirements for COMP3005 FInal project V2

[Link to Video Demonstration]()

### Setting up the PostgreSQL Database

- Launch pgAdmin 4.
- Create a new database. I am using `healthfitnessclub`.
- Open the query tool for the database you just created and run the `DDL.sql` and then `DML.sql` file.
- This will create the required tables and populate it with initial data.


### Installing Python Dependencies

Install [psycopg 3](https://pypi.org/project/psycopg/):

```bash
pip3 install --upgrade pip           # to upgrade pip
pip3 install "psycopg[binary,pool]"  # to install package and dependencies
```

### Running the Application

1. Update the database connection settings at the top of `main.py` to match your PostgreSQL database connection details.

2. Execute the following command in the terminal:

```bash
python3 ./main.py
```

Enjoy managing your Health fitness club!
