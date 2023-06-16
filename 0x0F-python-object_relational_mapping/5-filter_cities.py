#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def list_states(username, password, database, sname):
    """a function to list states"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = "SELECT DISTINCT cities.name FROM cities JOIN states ON \
    cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (sname,))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))
    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    sname = sys.argv[4]

    list_states(username, password, database, sname)
