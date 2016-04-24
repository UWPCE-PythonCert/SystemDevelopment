#!/usr/bin/env python

import os
import sqlite3
import sys

from address_book_model import create_sample

SCHEMA_FILE = "address_book_ddl.sql"
DB_FILE = "address.sqlite3"

if os.path.isfile(DB_FILE):
    print "%s exists, exiting" % DB_FILE
    sys.exit(-1)

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

def create_schema():
    with open(SCHEMA_FILE, 'rt') as f:
        schema = f.read()
        conn.executescript(schema)
        

create_schema()
address_book = create_sample()

for person in address_book.people:
    insert_statement = "INSERT INTO Person(first_name, last_name, middle_name, cell_phone, email) VALUES (?,?,?,?,?)"
    row = ( person.first_name, 
            person.last_name,
            person.middle_name,
            person.cell_phone,
            person.email)

    cursor.execute(insert_statement, row)
    print cursor.rowcount
    conn.commit()

# TODO: also insert Addresses, Businesses, AddressBook, and relationships between them.

conn.close()
