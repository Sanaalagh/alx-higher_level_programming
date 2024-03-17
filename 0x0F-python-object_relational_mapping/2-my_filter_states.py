#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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

    # Construct SQL query to select states based on user input
    sql_query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(
            sys.argv[4])

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
