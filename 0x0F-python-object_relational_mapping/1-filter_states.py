#!/usr/bin/python3
"""
This script lists all states with
a `name` starting with the letter `N`
from the database `hbtn_0e_0_usa`.
"""
'''
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    
    Access to the database and get the states
    from the database.
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
        '''
import MySQLdb
import sys

def list_states_with_N(mysql_user, mysql_password, database_name):
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user, passwd=mysql_password, db=database_name)
    cursor = db.cursor()

    # Execute the query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        state_id = row[0]
        state_name = row[1]
        print("{}: {}".format(state_id, state_name))

    # Close the database connection
    db.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_user = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        list_states_with_N(mysql_user, mysql_password, database_name)
    else:
        print("Please provide the MySQL username, password, and database name as arguments.")
