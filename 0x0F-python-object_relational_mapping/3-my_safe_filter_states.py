#!/usr/bin/python3
"""
This script connects to a MySQL server and retrieves all states from the
'states' table in the specified database where the matches the user input.
The script takes four arguments: mysql username, mysql password, database
name, and the state name to search for (safe from MySQL injection).
The results are sorted in asc order by the 'id' column of the 'states' table.
The script uses the MySQLdb module to interact with the MySQL database.
"""

import MySQLdb
import sys


def safe_search_state(cursor, state_name):
    """
    Function to safely search for a state in the
    database to prevent SQL injection.
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    return cursor.fetchall()


if __name__ == "__main__":
    """
    Main function that connects to a MySQL server and retrieves states
    based on user input (safe from SQL injection).
    """

    username = sys.argv[1]  # MySQL username
    password = sys.argv[2]  # MySQL password
    db_name = sys.argv[3]   # Database name
    state_name = sys.argv[4]  # State name to search for

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

    # Use the safe_search_state function to search for the state
    data = safe_search_state(cursor, state_name)

    # Display the results
    for state in data:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()
