#!/usr/bin/python3
""" script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    SQL_User = sys.argv[1]
    SQL_Psswrd = sys.argv[2]
    DBName = sys.argv[3]
    
    DB_Conn = MySQLdb.connect(host="localhost", port=3306, user=SQL_User,
                        passwd=SQL_Psswrd, db=DBName, charset="utf8")
    cursor = DB_Conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    DB_Conn.close()
