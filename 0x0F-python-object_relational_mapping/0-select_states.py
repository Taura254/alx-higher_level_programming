#!/usr/bin/python3
"""Lists all states fro the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ = "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passd=sys.argv[2], db=sys.argv[3])
    i = conn.cursor()
    i.execute("select * from 'states' ORDER BY 'id'")
    [print(state) for state in i.fetchall()]
