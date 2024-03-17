#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all cities from the 'cities'
table in the specified database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that connects to a MySQL server and lists all
    cities from the 'cities' table.
    """

    username = sys.argv[1]  # MySQL username
    password = sys.argv[2]  # MySQL password
    db_name = sys.argv[3]   # Database name

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name,\
            states.name FROM cities JOIN states ON \
            cities.state_id=states.id ORDER BY cities.id ASC")

    data = cursor.fetchall()

    for city in data:
        print(city)

    cursor.close()
    db.close()
