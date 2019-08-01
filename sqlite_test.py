#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('test.db')
    cur = con.cursor()  
    cur.execute('SELECT SQLITE_VERSION()')
    
    cur.execute("CREATE TABLE Users(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Users VALUES(1,'Michelle')")
    cur.execute("INSERT INTO Users VALUES(2,'Sonya')")
    cur.execute("INSERT INTO Users VALUES(3,'Greg')")
    
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    print(type(row))
    #print(data)
    #print("SQLite version: %s" % data)                
except lite.Error as e:   
    print("Error %s:" % e.args[0])
    sys.exit(1)
finally:    
    if con:
        con.close()