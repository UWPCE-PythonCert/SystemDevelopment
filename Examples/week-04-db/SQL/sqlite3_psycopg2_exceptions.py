#!/usr/bin/env python

if False:
    import sqlite3 as db
    DSN = ':memory:'
    PARAM = '?'
else:
    # note differences in parameter names between string and keyword argument DSNs:
    # http://initd.org/psycopg/docs/module.html
    import psycopg2 as db
    DSN = 'dbname=velotron' 
    PARAM = '%s'

try:
    with db.connect('/bin/invalid.db') as conn:
        pass
except db.OperationalError as e:
    print "caught operational error: %s" % e

with db.connect(DSN) as conn:
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Students')
    cursor.execute('CREATE TABLE Students(id INTEGER PRIMARY KEY, name TEXT)')
    # conn.commit()
    cursor.execute('INSERT INTO Students(id, name) VALUES (%s, %s)' % (PARAM, PARAM), (1, "batman"))

    try:
        cursor.execute('INSERT INTO Students(id, name) VALUES (%s, %s)' % (PARAM, PARAM), (1, "robin"))
    except db.IntegrityError as e:
        print "caught integrity error: %s" % e
        # conn.rollback()

    try:
        cursor.execute('INSERT INTO Students(id, name) VALUES (%s, %s)' % (PARAM, PARAM), ("joker", 2))
    except db.IntegrityError as e:
        print "caught integrity error: %s" % e
    except db.DataError as e:
        print "caught data error: %s" % e
