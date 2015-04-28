#!/usr/bin/env python

# http://xkcd.com/327/

import sqlite3

DB_NAME = ":memory:"

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    create_query = 'CREATE TABLE Students(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)'
    insert_query = 'INSERT INTO Students(name) VALUES (?)'
    select_query = 'SELECT COUNT(*) FROM Students'

    cursor.execute(create_query)

    student_data = (
        ("Don",),
        ("Sally",),
        ("Robert');DROP TABLE Students;--",)
    )
    cursor.executemany(insert_query, student_data)

    # now get pwned
    bad_insert_query = """INSERT INTO Students(name) VALUES ('%s')"""
    for name in student_data:
        cursor.executescript(bad_insert_query % name)
        print "DB contains %s rows" % cursor.execute(select_query).fetchone()[0]
