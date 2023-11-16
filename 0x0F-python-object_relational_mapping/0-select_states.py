#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to select all records from the 'states' table
    cur.execute("SELECT * FROM states")

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Iterate through each row and print it
    for row in rows:
        print(row)

    # Close the cursor to release resources
    cur.close()

    # Close the database connection
    db.close()
