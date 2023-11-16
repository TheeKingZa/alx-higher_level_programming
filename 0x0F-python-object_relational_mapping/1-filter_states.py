#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to select distinct states with names starting with 'N'
    cur.execute("""
        SELECT DISTINCT * FROM states
        WHERE name LIKE BINARY 'N%'
        ORDER BY states.id
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
