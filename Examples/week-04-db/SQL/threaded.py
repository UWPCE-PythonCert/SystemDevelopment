import logging
import os
import sys
import sqlite3
import threading
import time
from utils import AUTHORS_BOOKS


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )


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
    logging.debug("beginning read")
    cur.execute(query)
    logging.debug("selects issued")
    had_rows = False
    for row in cur.fetchall():
        print row
        had_rows = True
    logging.debug("results fetched")
    if not had_rows:
        print "no rows returned"


def show_authors(conn):
    query = author_query
    show_query_results(conn, query)


def show_books(conn):
    query = book_query
    show_query_results(conn, query)


def populate_db(conn):
    authors = ([author] for author in AUTHORS_BOOKS.keys())
    cur = conn.cursor()
    logging.debug("connected")
    cur.executemany(author_insert, authors)
    
    for author in AUTHORS_BOOKS.keys():
        params = ([book, author] for book in AUTHORS_BOOKS[author])
        cur.executemany(book_insert, params)
    
    logging.debug("changes made")


def writer():
    logging.debug("connecting")
    with sqlite3.connect(DB_FILENAME, isolation_level="EXCLUSIVE") as conn:
        populate_db(conn)
        logging.debug("waiting to sync")
        ready.wait()
        logging.debug("PAUSING")
        time.sleep(3)
        conn.commit()
        logging.debug("CHANGES COMMITTED")
    return


def reader():
    with sqlite3.connect(DB_FILENAME, isolation_level="EXCLUSIVE") as conn:
        logging.debug("waiting to sync")
        ready.wait()
        logging.debug("beginning read")
        show_authors(conn)
        show_books(conn)
    return

if __name__ == '__main__':
    if DB_IS_NEW:
        print "Database does not yet exist, please run `createdb` first"
        sys.exit(1)

    ready = threading.Event()
    
    threads = [
        threading.Thread(name="Reader", target=reader),
        threading.Thread(name="Writer", target=writer),
    ]
    
    [t.start() for t in threads]
    
    time.sleep(2)
    logging.debug('sending sync event')
    ready.set()
    
    [t.join() for t in threads]
