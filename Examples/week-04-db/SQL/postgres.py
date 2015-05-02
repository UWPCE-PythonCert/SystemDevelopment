#!/usr/bin/env python

import psycopg2

conn = psycopg2.connect(host="localhost", user="velotron", password="",  database="velotron")

cursor = conn.cursor()

cursor.execute('select * from foo')

for row in cursor:
    print row
