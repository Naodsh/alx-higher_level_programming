#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves all states from
the 'states' table in the specified database.
The script takes three arguments: mysql username, password, and database name.
The results are sorted in ascending order by the 'id' of the 'states' table.
The script uses the MySQLdb module to interact with the MySQL database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that connects to a MySQL server and retrieves
    all states from the 'states' table.
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    data = cursor.fetchall()

    for state in data:
        print(state)

    cursor.close()
    db.close()
