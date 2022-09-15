#!/usr/bin/python3
"""Lists all states with a name starting with N from hbtn_0e_0_usa database"""
import sys
import MySQLdb


if __name__ = "__main__":
    conn = MySQLdb(user=sys.argv[1], passd=sys.argv[2], db=sys.argv[3])
    i = conn.cursor()
    i.execute("SELECT * FROM 'states' ORDER BY 'id'")
    [print(state) for state in i.fetchall() if state[1][0] == "N"]
