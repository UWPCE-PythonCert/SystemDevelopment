import logging
import os
import sys
import sqlite3
import threading
import time


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s (%(threadName)-10s) %(message)s',
                    )

DB_FILENAME = 'test.db'

def populate_db(conn):
    conn.execute("""CREATE TABLE BOOKS(author VARCHAR, title VARCHAR)""")

def show_books(conn):
    for i in xrange(1000):
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM BOOKS LIMIT 1""")
        for row in cursor:
            print row
    

def writer(conn):
    for i in xrange(1000):
        cursor = conn.cursor()
        data = ["author", "name"]
        cursor.execute("INSERT INTO BOOKS(author, title) VALUES (?, ?)", data)
        conn.commit()

def reader(conn):
    with sqlite3.connect(DB_FILENAME) as conn:
        show_books(conn)

if __name__ == '__main__':

    if os.path.exists(DB_FILENAME):
        os.remove(DB_FILENAME)

    with sqlite3.connect(DB_FILENAME) as conn:
        populate_db(conn) 

        ready = threading.Event()
        
        threads = [
            threading.Thread(name="Reader", target=reader, args=(conn,)),
            threading.Thread(name="Writer", target=writer, args=(conn,)),
        ]
        
        [t.start() for t in threads]
        
        [t.join() for t in threads]
