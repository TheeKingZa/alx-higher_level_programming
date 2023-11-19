# Object Relational Mapping
[<](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x0E-SQL_more_queries/README.md) 0x0F [>](https://github.com/TheeKingZa/alx-higher_level_programming/tree/master/0x12-javascript-warm_up/README.md)
---

# NEED TO KNOW?
* [Resources](#resources)
* [Installing](#installing)
    * [MySQLdb v2.0.x](#install-mysqldb-module-version-20x)
    * [SQLAlchemy)](#install-sqlalchemy-module-version-14x)
* [How to connect to a MySQL database from a Python script?](#how-to-connect-to-a-mysql-database-from-a-python-script)
* [How to SELECT rows in a MySQL table from a Python script?](#how-to-SELECT-rows-in-a-mysql-table-from-a-python-script)
* [How to INSERT rows in a MySQL table from a Python script?](#how-to-insert-rows-in-a-mysql-table-from-a-python-script)
* [What ORM means?](#what-orm-means)
* [How to map a Python Class to a MySQL table?](#how-to-map-a-python-class-to-a-mysql-table)
* [How to create a Python Virtual Environment?](#how-to-create-a-python-virtual-enviroment)

# Resources
Read or watch:

* [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
* [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io)(please don’t pay attention to _mysql)
* [MySQLdb tutorial](https://www.mikusa.com/python-mysql-docs/index.html)
* [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
* [SQLAlchemy](https://docs.sqlalchemy.org/en/13/)
* [mysqlclient/MySQLdb](https://github.com/PyMySQL/mysqlclient)
* [Introduction to SQLAlchemy](https://www.youtube.com/watch?v=woKYyhLCcnU)
* [Flask SQLAlchemy](https://youtube.com/playlist?list=PLXmMXHVSvS-BlLA5beNJojJLlpE0PJgCW&si=lNIZSJpSa2j2vqYJ)
* [10 common stumbling blocks for SQLAlchemy newbies](http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html)
* [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
* [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
  (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
* [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
* [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

# Installng
--
## Install MySQLdb module version 2.0.x
--
For installing MySQLdb, you need to have MySQL installed: [How to install MySQL 8.0 in Ubuntu 20.04](https://phoenixnap.com/kb/install-mysql-ubuntu-20-04)
--
    $ sudo apt-get install python3-dev
    $ sudo apt-get install libmysqlclient-dev
    $ sudo apt-get install zlib1g-dev
    $ sudo pip3 install mysqlclient
    ...
    $ python3
    >>> import MySQLdb
    >>> MySQLdb.version_info 
    (2, 0, 3, 'final', 0)

## Install SQLAlchemy module version 1.4.x
    $ sudo pip3 install SQLAlchemy
    ...
    $ python3
    >>> import sqlalchemy
    >>> sqlalchemy.__version__ 
    '1.4.22'
---
also, you can have this warning messages:
---
    /usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
    moved in a future release.")                                                                                                                    
      cursor.execute(statement, parameters)
---
You can ignore it
---

[^](#need-to-know)

# How to connect to a MySQL database from a Python script?
    Connecting to MySQL Database from Python

    Introduction:
      This document provides a simple guide on how to connect to a MySQL database using Python. We'll use the mysql-connector-python library for this example.
      
      Prerequisites:
      
      Before you begin, ensure that you have the following:

        * Python installed on your machine.
        * mysql-connector-python library. You can install it using:

            pyCode
              pip install mysql-connector-python
      
      Usage
      ------
        * Import the necessary modules:

            pycode
              import mysql.connector
              from mysql.connector import Error

      /**/
        Import the required modules, including 'mysql.connector' for database connectivity.

      # Establish the database connection:

            pyCOde
              def create_connection(host, user, password, database):
                try:
                    connection = mysql.connector.connect(
                      host=host,
                      user=user,
                      password=password,
                      database=database
                    )
                    return connection
                except Error as e:
                    print(f"Error: {e}")
                    return None
      /**/
      Define a function 'create_connection' to establish a connection to the MySQL database.
      Return the connection object if successful,
      otherwise print the error
      and return 'None'.

      # Connect to the database:

            pyCode
              # Replace these with your own database credentials
              host = "your_host"
              user = "your_username"
              password = "your_password"
              database = "your_database"

              connection = create_connection(host, user, password, database)

              if connection:
                print("Connected to the MySQL database")
                # Perform your database operations here
                connection.close()  # Don't forget to close the connection when done
                else:
                print("Failed to connect to the MySQL database")
    /**/
    Replace the placeholder values with your actual database credentials.
    Call the create_connection function to establish a connection and print a success message if the connection is successful.

    Conclusion:

        You have successfully connected to a MySQL database using Python. Customize the code according to your specific use case and database requirements.

[^](#need-to-know)

# How to SELECT rows in a MySQL table from a Python script?
    To SELECT rows from a MySQL table in a Python script, follow these steps:

      * Importing Modules:
        Import the necessary modules, including mysql-connector-python, for MySQL database interaction.

      * Establishing a Connection:
        Create a connection to the MySQL database using mysql.connector.connect() with host, user, password, and database parameters.

      * Creating a Cursor:
        After establishing a connection, create a cursor to execute SQL queries on the database.

      * Executing the SELECT Query:
        Use the cursor to execute a SELECT query with the desired columns and table.

      * Fetching Results:
        Fetch the query results using methods like fetchone(), fetchall(), or fetchmany().

      * Processing Results:
        Process the retrieved data in your Python script as needed.

      * Closing the Cursor and Connection:
        Close the cursor and connection using close() to free up resources.

      * Error Handling:
        Implement error handling with try-except blocks to manage potential issues during database interactions.


[^](#need-to-know)

# How to INSERT rows in a MySQL table from a Python script?
    To INSERT rows into a MySQL table from a Python script:

      # Importing Modules:
        Import the required modules,
        including mysql-connector-python,
        for MySQL database interaction.

      # Establishing a Connection:
        Create a connection to the MySQL database using mysql.connector.connect()
        with host,
        user,
        password,
        and database parameters.

      # Creating a Cursor:
        After establishing a connection,
        create a cursor to execute SQL queries on the database.

      # Executing the INSERT Query:
        Use the cursor to execute an INSERT query with the data you want to add to the table.

      # Committing Changes:
        Commit the changes to the database using commit()
        to persist the inserted data.

      # Closing the Cursor and Connection:
        Close the cursor and connection using close()
        to release resources.

      # Error Handling:
        Implement error handling with try-except blocks to manage
        potential issues during the database interaction.


[^](#need-to-know)

# What ORM means?
    ORM stands for Object-Relational Mapping.
    It is a programming technique that allows the conversion of data between incompatible type systems,
    in particular, between a relational database and an object-oriented programming language.



[^](#need-to-know)

# How to map a Python Class to a MySQL table?
    **Define a Class**:
      Create a Python class representing the structure of the data you want to store.

    **Use an ORM Framework**:
      Choose an ORM framework like SQLAlchemy or Django ORM.

    **Create a Model**:
      Define a model by extending a base class provided by the ORM framework. This model represents the mapping between the Python class and the MySQL table.

    **Specify Fields**:
      Specify fields in the model that correspond to columns in the MySQL table.

    **Define Relationships**:
      If needed, define relationships between classes/models to represent associations between tables.

    **Perform Migrations**:
      Use migration tools provided by the ORM framework to synchronize the database schema with your Python class definitions.



[^](#need-to-know)

# How to create a Python Virtual Environment?
    To create a Python Virtual Environment:

    1. Install virtualenv: If not installed, install virtualenv using the following command:
        bash
          pip install virtualenv
    
    2. Navigate to Project Directory:
        * Navigate to Project Directory:
          - Open a terminal and navigate to the directory where you want to create the virtual environment.
    
    3. Create Virtual Environment:
        - Run the following command to create a virtual environment named "venv":

          virtualenv venv

    4. Activate Virtual Enviroment:
        Activate the Virtual enviroment
          * On Windows:
              bashCode
                .\venv\Scripts\activate
          * On macOS/Linux:
              bashCode
                source venev/bin/activate
    5. Deactivate Virtual Environment
        To deactivate the virtual environment, simply run:
            deactivate

[^](#object-relational-mapping)

