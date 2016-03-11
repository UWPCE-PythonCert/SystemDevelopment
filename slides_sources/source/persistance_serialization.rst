.. _serialization:

*****************************
Persistence and Serialization
*****************************

========
Overview
========

.. rst-class:: left
  Persistence and Serialization are closely related.

  *Serialization* means taking a potentially complex data structure and converting it into a single string of bytes.

  https://en.wikipedia.org/wiki/Serialization

  *Persistence* is storing data in a way that it will persist beyond the run-time of your program.

  https://en.wikipedia.org/wiki/Persistence_(computer_science)

  They are closely related, because most forms of persistent storage -- simple text files, databases, etc., require that it be turned into a simple string of bytes first. After all, at the end of the day, everything done with computers is ultimately a serial string of bytes.

  Serialization is also very useful for transmitting information between systems -- over the network, etc.


Serialization
-------------

Today is less about concepts

More about learning to use a given module

So less talk, more coding

.. nextslide::

I'm focusing on methods available in the Python standard library

Serialization is the process of putting your potentially complex
(and nested) python data structures into a linear (serial) form .. i.e. a string of bytes.

The serial form can be saved to a file, pushed over the wire, etc.

Persistence
-----------

Persistence is saving your python data structure(s) to disk -- so they
will persist once the python process is finished.

Any serial form can provide persistence (by dumping/loading it to/from
a file), but not all persistence mechanisms are serial (i.e RDBMS)

http://wiki.python.org/moin/PersistenceTools

=======================
Python Specific Formats
=======================

Python Literals
---------------

Putting plain old python literals in your file

Gives a nice, human-editable form for config files, etc.

Don't use for untrusted sources!!!

Good for basic python types.

(can work for your own classes, too -- if you write a good ``__repr__`` )

In theory, ``repr()`` always gives a form that can be re-constructed.

Often the ``str()`` form works too.

``pprint``  (pretty print) module can make it easier to read:

https://docs.python.org/3.5/library/pprint.html


Python Literal Example
----------------------

.. code-block:: ipython

    # a list of dicts
    data = [{'this':5, 'that':4}, {'spam':7, 'eggs':3.4}]
    In [51]: s = repr(data) # save a string version:
    In [52]: data2 = eval(s) # re-construct with eval:
    In [53]: data2 == data # they are equal
    Out[53]: True
    In [54]: data is data2 # but not the same object
    Out[54]: False


You can save the string to a file and even use ``import``

.. nextslide::

NOTE: ``eval()`` is **DANGEROUS**:

Not so bad if you know where your data is coming from, but ``eval()`` will run any code it gets, even:

.. code-block:: python

    import sys
    sys.system('cd /; rm -rf *')

You really don't want that run on your machine!   

The alternative:
   ``ast.literal_eval`` is safer than eval:

   https://docs.python.org/3.5/library/ast.html#ast-helpers

It will only evaluate literals.


pretty print
------------

.. code-block:: ipython

    In [68]: data = [{'this': 5, 'that': 4}, {'eggs': 3.4, 'spam': 7},
             {'foo': 86, 'bar': 4.5}, {'fun': 43, 'baz': 6.5}]
    In [69]: import pprint
    In [71]: repr(data)
    Out[71]: "[{'this': 5, 'that': 4}, {'eggs': 3.4, 'spam': 7}, {'foo': 86, 'bar': 4.5}, {'fun': 43, 'baz': 6.5}]"
    In [72]: s = pprint.pformat(data)
    In [73]: print(s)
    [{'that': 4, 'this': 5},
     {'eggs': 3.4, 'spam': 7},
     {'bar': 4.5, 'foo': 86},
     {'baz': 6.5, 'fun': 43}]


Pickle
------

Pickle is a binary format for python objects

You can essentially dump any python object to disk (or string, or socket, or...

.. code-block:: ipython

    In [87]: import pickle
    In [83]: data
    Out[83]:
    [{'that': 4, 'this': 5},
     {'eggs': 3.4, 'spam': 7},
     {'bar': 4.5, 'foo': 86},
     {'baz': 6.5, 'fun': 43}]
    In [84]: pickle.dump(data, open('data.pkl', 'wb'))
    In [85]: data2 = pickle.load(open('data.pkl', 'rb'))
    In [86]: data2 == data
    Out[86]: True

https://docs.python.org/3.5/library/pickle.html

.. nextslide::

.. rst-class:: medium

  **Warning**

The pickle module is not secure against erroneous or maliciously constructed data. Never unpickle data received from an untrusted or unauthenticated source.

``pickle`` is cool because it can serialize virtually ANY object -- including your self-defined classes.

But to do this, it must run essentially arbitrary code -- so **not safe**.

Do not use it for receiving data from an external source.

But you probably won't want to do that anyway -- pickle is python-specific, not very useful for data interchange.

Shelve
------

A "shelf" is a persistent, dictionary-like object.

(It's also a place you can put a jar of pickles...)

The values (not the keys!) can be essentially arbitrary Python objects (anything picklable)

**NOTE:** it will not reflect changes in mutable objects without re-writing them to the db. (or use ``writeback=True``)

If less that 100s of MB -- just use a dict and pickle it.

https://docs.python.org/3.5/library/shelve.html

.. nextslide::

``shelve``  presents a ``dict``  interface:

.. code-block:: ipython

    import shelve
    d = shelve.open(filename)
    d[key] = data   # store data at key
    data = d[key]   # retrieve a COPY of data at key
    del d[key]      # delete data stored at key
    flag = d.has_key(key)   # true if the key exists
    d.close()       # close it

(it uses pickle under the hood -- same security issues)

https://docs.python.org/3.5/library/shelve.html

LAB
---

Here are two datasets embedded in Python:

:download:`add_book_data.py <../../Examples/persistance/add_book_data.py>`
and
:download:`add_book_data_flat.py <../../Examples/persistance/add_book_data_flat.py>`

They can be loaded with:: 

    from add_book_data import AddressBook

They have address book data -- one with a nested dict, one "flat"

* Write a module that saves the data as python literals in a file

  - and reads it back in

* Write a module that saves the data as a pickle in a file

  - and reads it back in

* Write a module that saves the data in a shelve

  - and accesses it one by one.


===================
Interchange Formats
===================

INI
---

INI files

(the old Windows config files)

::

    [Section1]
    int = 15
    bool = true
    float = 3.1415
    [Section2]
    int = 32
    ...



Good for configuration data, etc.

ConfigParser
------------

Writing ``ini``  files:

.. code-block:: python

    import configparser
    config = configparser.ConfigParser()
    config.add_section('Section1')
    config.set('Section1', 'int', '15')
    config.set('Section1', 'bool', 'true')
    config.set('Section1', 'float', '3.1415')
    # Writing our configuration file to 'example.cfg'
    config.write(open('example.cfg', 'w'))

Note: all keys and values are strings

.. nextslide::

Reading ``ini``  files:

.. code-block:: python

    >>> config = configparser.ConfigParser()
    >>> config.read('example.cfg')
    >>> config.sections()
    ['Section1', 'Section2']
    >>> config.get('Section1', 'float')
    '3.1415'
    >>> config.items('Section1')
    [('int', '15'), ('bool', 'true'), ('float', '3.1415')]


https://docs.python.org/3.5/library/configparser.html

CSV
---

CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases.

No real standard -- the Python csv package more or less follows MS Excel "standard" (with other "dialects" available)

Can use delimiters other than commas... (I like tabs better)

Most useful for simple tabular data

CSV module
----------

Reading ``CSV``  files:

.. code-block:: python

    >>> import csv
    >>> spamReader = csv.reader( open('eggs.csv', 'r') )
    >>> for row in spamReader:
    ...     print(', '.join(row))
    Spam, Spam, Spam, Spam, Spam, Baked Beans
    Spam, Lovely Spam, Wonderful Spam

``csv``  module takes care of string quoting, etc. for you

https://docs.python.org/3.5/library/csv.html

.. nextslide::

Writing ``CSV``  files:

.. code-block:: python

    >>> import csv
    >>> with open('eggs2.csv', 'w') as outfile:
    >>>     spam_writer = csv.writer(outfile,
                                     quoting=csv.QUOTE_MINIMAL)
    >>>     spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    >>>     spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
    >>>     spam_writer.writerow(['Spam', 'Spam, Wonderful spam..', 'Very-Wonderful Spam'])


``csv``  module takes care of string quoting, etc for you

https://docs.python.org/3.5/library/csv.html

JSON
----

JSON (JavaScript Object Notation) is a subset of JavaScript syntax used as a lightweight data interchange format. LOTS of systems can read JSON -- notably browsers...

Python module has an interface similar to pickle

Can handle the standard Python data types

Specializable encoding/decoding for other types -- but I wouldn't do that!

Presents a similar interface as ``pickle``

http://www.json.org/

https://docs.python.org/3.5/library/json.html

Python json module
------------------

.. code-block:: ipython

    In [93]: import json
    In [94]: s = json.dumps(data)
    Out[95]: '[{"this": 5, "that": 4}, {"eggs": 3.4, "spam": 7},
               {"foo": 86, "bar": 4.5}, {"fun": 43, "baz": 6.5}]'
        # looks a lot like python literals...
    In [96]: data2 = json.loads(s)
    Out[97]:
    [{u'that': 4, u'this': 5},
     {u'eggs': 3.4, u'spam': 7},
    ...
    In [98]: data2 == data
    Out[98]: True # they are the same

(also ``json.dump() and json.load()`` for files)

**NOTE:** JSON is less "rich" than python -- no tuples, no distiction between integers and floats, no comments!

https://docs.python.org/3.5/library/json.html

XML
---

XML is a standardized version of SGML, designed for use as a data storage / interchange format.

NOTE: HTML is also SGML, and modern versions conform to the XML standard.

XML in the python std lib
-------------------------

``xml.dom``

``xml.sax``

``xml.parsers.expat``

``xml.etree``

https://docs.python.org/3.5/library/xml.etree.elementtree.html

elementtree
-----------

elementtree is the simplest tool -- maps pretty directly to XML.

The Element type is a flexible container object, designed to store hierarchical data structures in memory.

Essentially an in-memory XML -- can be read from / written-to XML

an ``ElementTree``  is an entire XML doc

an ``Element``  is a node in that tree

https://docs.python.org/3.5/library/xml.etree.elementtree.html

LAB
---

Use the same addressbook data:

::

    # load with:
    from add_book_data import AddressBook

* Write a module that saves the data as an INI file

   - and reads it back in

* Write a module that saves the data as a CSV file

   - and reads it back in

* Write a module that saves the data in JSON

   - and reads it back in

* Write a module that saves the data in XML

   - and reads it back in

   - this gets ugly!

(NEED a good example here!)

=========
DataBases
=========

anydbm
------

``dbm``  is a generic interface to variants of the DBM database

Suitable for storing data that fits well into a python dict with strings as both keys and values

Note: dbm will use the dbm system that works on your system -- this may be different on different systems -- so the db files may NOT be compatible! ``whichdb``  will try to figure it out, but it's not guaranteed

https://docs.python.org/3.5/library/dbm.html

dbm module
-------------
Writing data:

code-block:: python

    #creating a dbm file:
    import dbm
    dbm.open(filename, 'n')

flag options are:

* 'r' --  Open existing database for reading only (default)
* 'w' -- Open existing database for reading and writing
* 'c' --  Open database for reading and writing, creating it if it doesn’t exist
* 'n' -- Always create a new, empty database, open for reading and writing

https://docs.python.org/3.5/library/dbm.html

anydbm module
-------------

``dbm``  provides dict-like interface:

::

    import dbm
    db = dbm.open("dbm", "c")
    db["first"] = "bruce"
    db["second"] = "micheal"
    db["third"] = "fred"
    db["second"] = "john" #overwrite
    db.close()
    # read it:
    db = dbm.open("dbm", "r")
    for key in db.keys():
        print(key, db[key])

http://docs.python.org/library/anydbm.html


sqlite
------

SQLite: C library provides a lightweight disk-based single-file database

Nonstandard variant of the SQL query language

Very broadly used as as an embedded databases for storing application-specific data etc.

Firefox plug-in:

https://addons.mozilla.org/en-US/firefox/addon/sqlite-manager/


python sqlite module
--------------------

``sqlite3``  Python module wraps C lib -- provides standard DB-API interface

Allows (and requires) SQL queries

Can provide high performance, flexible, portable storage for your app

https://docs.python.org/3.5/library/sqlite3.html

.. nextslide::

Example:

::

    import sqlite3
    # open a connection to a db file:
    conn = sqlite3.connect('example.db')
    # or build one in-memory
    conn = sqlite3.connect(':memory:')
    # create a cursor
    c = conn.cursor()

https://docs.python.org/3.5/library/sqlite3.html

python sqlite module
--------------------

Execute SQL with the cursor:

::

    # Create table
    c.execute("'CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)'")
    # Insert a row of data
    c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    # Save (commit) the changes
    conn.commit()
    # Close the cursor if we are done with it
    c.close()


https://docs.python.org/3.5/library/sqlite3.html

python sqlite module
--------------------

``SELECT``  creates an cursor that can be iterated:

::

    >>> for row in c.execute('SELECT * FROM stocks ORDER BY price'):
            print row
    ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)
    ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)
    ...


Or you can get the rows one by one or in a list:

::

     c.fetchone()
     c.fetchall()


python sqlite module
--------------------

Good idea to use the DB-API’s parameter substitution:

::

    t = (symbol,)
    c.execute('SELECT * FROM stocks WHERE symbol=?', t)
    print c.fetchone()
    # Larger example that inserts many records at a time
    purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
                 ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
                 ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
                ]
    c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)


http://xkcd.com/327/

DB-API
------

The DB-API spec (PEP 249) is a specification for interaction between Python and Relational Databases.

Support for a large number of third-party Database drivers:

  * MySQL
  * PostgreSQL
  * Oracle
  * MSSQL (?)
  * ...

http://www.python.org/dev/peps/pep-0249}

=============
Other Options
=============

Object-Relation Mappers
-----------------------

Systems for mapping Python objects to tables

Saves you writing that glue code (and the SQL)

Usually deal with mapping to variety of back-ends:
 -- test with SQLite, deploy with PostreSQL

 SQL Alchemy
 -- http://www.sqlalchemy.org/

Django ORM
https://docs.djangoproject.com/en/dev/topics/db/

Object Databases
----------------

Directly store and retrieve Python Objects.

Kind of like ``shelve``, but more flexible, and give you searching, etc.

ZODB: (http://www.zodb.org/)

NoSQL
-----
Map-Reduce, etc.

....Big deal for "Big Data": Amazon, Google, etc.

Document-Oriented Storage

* MongoDB (BSON interface, JSON documents)

* CouchDB (Apache):

  *  JSON documents

  *  Javascript querying (MapReduce)

  *  HTTP API


LAB
---

::
    # load with:
    from add_book_data import AddressBook

* Write a module that saves the data in a dbm datbase

  - and reads it back in

* Write a module that saves the data in an SQLite datbase

  - and reads it back in

  - helps to know SQL here...


