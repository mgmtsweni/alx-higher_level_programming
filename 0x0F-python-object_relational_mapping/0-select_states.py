#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    SQL_User = sys.argv[1]
    SQL_Psswrd = sys.argv[2]
    DBName = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=SQL_User,
                        passwd=SQL_Psswrd, db=DBName)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
