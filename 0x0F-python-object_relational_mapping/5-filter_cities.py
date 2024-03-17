#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[
        2], db=argv[3], host="localhost", port=3306)
    cur = db.cursor()
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")
    cur.execute(query, (argv[4],))
    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))
    cur.close()
    db.close()
