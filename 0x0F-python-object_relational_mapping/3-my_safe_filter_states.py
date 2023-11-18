#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Extract the search pattern from the command-line arguments
    match = sys.argv[4]

    # Execute a parameterized SQL query to
    # select states with names containing the specified pattern
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    # Fetch all the rows returned by the query
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor to release resources
    cur.close()

    # Close the database connection
    db.close()
