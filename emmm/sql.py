#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('user.db')
print("Opened database successfully")
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS USER''')
c.execute('''DROP TABLE IF EXISTS LOG;''')
c.execute('''CREATE TABLE USER
       (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
       NAME           TEXT    NOT NULL,
       LEVEL          INT     NOT NULL,
       ADDRESS        CHAR(50),
       FAVORATE       CHAR(50));''')
c.execute('''CREATE TABLE LOG
       (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
       NAME           TEXT    NOT NULL,
       LEVEL          INT     NOT NULL,
       ADDRESS        CHAR(50));''')
print("Table created successfully")
conn.commit()
conn.close()