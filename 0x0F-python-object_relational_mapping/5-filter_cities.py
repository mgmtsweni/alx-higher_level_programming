#!/usr/bin/python3
"""lists all cities of that state using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities INNER JOIN states \
        ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id ASC", (argv[4],))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
