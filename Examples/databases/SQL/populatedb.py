import os
import sys
import sqlite3
from utils import AUTHORS_BOOKS

DB_FILENAME = 'books.db'
DB_IS_NEW = not os.path.exists(DB_FILENAME)

author_insert = "INSERT INTO author (name) VALUES(?);"
author_query = "SELECT * FROM author;"
book_query = "SELECT * FROM book;"
book_insert = """
INSERT INTO book (title, author) VALUES(?, (
    SELECT authorid FROM author WHERE name=? ));
"""


def show_query_results(conn, query):
    cur = conn.cursor()
    cur.execute(query)
    had_rows = False
    for row in cur.fetchall():
        print row
        had_rows = True
    if not had_rows:
        print "no rows returned"


def show_authors(conn):
    query = author_query
    show_query_results(conn, query)


def show_books(conn):
    query = book_query
    show_query_results(conn, query)


if __name__ == '__main__':
    if DB_IS_NEW:
        print "Database does not yet exist, please import `createdb` first"
        sys.exit(1)

    with sqlite3.connect(DB_FILENAME) as conn1:
        print "\nOn conn1, before insert:"
        show_authors(conn1)

        authors = ([author] for author in AUTHORS_BOOKS.keys())
        cur = conn1.cursor()
        cur.executemany(author_insert, authors)
        print "\nOn conn1, after insert:"
        show_authors(conn1)

        with sqlite3.connect(DB_FILENAME) as conn2:
            print "\nOn conn2, before commit:"
            show_authors(conn2)

            conn1.commit()
            print "\nOn conn2, after commit:"
            show_authors(conn2)



