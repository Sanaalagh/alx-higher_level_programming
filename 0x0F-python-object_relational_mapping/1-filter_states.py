#!/usr/bin/python3
"""
A script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Construct SQL query to select states starting with 'N'
    sql_query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    # Execute the SQL command
    cursor.execute(sql_query)

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    # Print results
    for row in results:
        print(row)

    # Close the cursor
    cursor.close()

    # Close the database connection
    db.close()
