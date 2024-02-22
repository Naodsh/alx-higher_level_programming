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

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute a SELECT query to retrieve states with names starting with 'N'
    cursor.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the results
    data = cursor.fetchall()

    # Display the results
    for state in data:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
