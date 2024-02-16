#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all cities from the 'cities'
table in the specified database.
The script takes three arguments: mysql username, mysql password,
and database name.
The script connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
The script only uses execute() once to fetch the results.
Results are displayed as specified in the example below.
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

    # Execute the query to fetch all cities from the 'cities' table
    cursor.execute("SELECT cities.id, cities.name,\
            states.name FROM cities JOIN states ON \
            cities.state_id=states.id ORDER BY cities.id ASC")

    # Fetch all the results
    data = cursor.fetchall()

    # Display the results
    for city in data:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()
