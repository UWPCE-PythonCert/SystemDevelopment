#!/usr/bin/env python

import sqlite3

DB_NAME = ":memory:"

with sqlite3.connect(DB_NAME) as conn:
    cursor = conn.cursor()

    create_query = 'CREATE TABLE foo(id INT, value FLOAT)'
    insert_query = 'INSERT INTO foo(id, value) VALUES (?,?)'
    select_query = 'SELECT * FROM foo'


    data_generator = ((x,float(x)*2) for x in xrange(10))

    cursor.execute(create_query)

    cursor.executemany(insert_query, data_generator)

    print cursor.execute(select_query).fetchall()

    print "row description: %s" % str(cursor.description)

    print cursor.executemany("INSERT INTO foo(id, value) VALUES (?, ?)", ((1,2.0), (2,5.5)))

    print "%d rows affected" % cursor.rowcount

