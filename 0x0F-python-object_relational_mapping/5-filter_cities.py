#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute a SQL query to retrieve the names of cities for a given state
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))

    # Fetch all the rows (city names) from the result set
    rows = cur.fetchall()

    # Extract city names from the rows and store them in a list
    tmp = list(row[0] for row in rows)

    # Print the city names separated by commas
    print(*tmp, sep=", ")

    # Close the cursor and the database connection
    cur.close()
    db.close()
