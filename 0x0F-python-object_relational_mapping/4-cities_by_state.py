#!/usr/bin/python3
""" Lists all states and their cities from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to select data
    # from 'cities' and 'states' tables using an INNER JOIN
    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
    """)

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor to release resources
    cur.close()

    # Close the database connection
    db.close()
