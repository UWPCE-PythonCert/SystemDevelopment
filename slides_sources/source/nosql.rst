.. _nosql:


================
No SQL Databases
================

An SQL system is not always the best way to store your data.

What is a Database?
====================

"A database is an organized collection of data. The data are typically organized to model relevant aspects of reality in a way that supports processes requiring this information.

Usually a way to persist and recover that organized data.

These days, when you say "Database" almost everyone thinks "Relational Database", and SQL is the standard way to do that.

SQL RDBMS systems are robust, powerful, scalable and very well optimized.

But: They require you to adapt the relational data model.

Non RDBMS options:
------------------

A key buzzword these days is "NOSQL"

OK: They don't use SQL -- but what are they?

Not one thing, but key features are mostly shared:
 * "schema less"
   - Document oriented

 * More direct mapping to an object model.

 * Highly Scalable
   - Easier to distribute / parallelize:


Database Schema
------------------


Schema:
  A database schema is the organization of data, and description of how a database is constructed: Divided into database tables, and relationships: foreign keys, etc...

  Includes what fields in what tables, what data types each field is, normalization of shared data, etc.

This requires a fair bit of work up-front, and can be hard to adapt as the system requirements change.

It also can be a bit ugly to map your programming data model to the schema.

Schemaless
------------------


Schemaless databases generally follow a "document model".

Each entry in the database is a "document":
 * essentially an arbitrary collection of fields.
 * often looks like a Python dict.

Not every entry has to have exactly the same structure.

Maps well to dynamic programming languages.

Adapts well as the system changes.

NoSQL in Python:
------------------


Three Categories:

1. Simple key-value object store:

   - shelve
   - anydbm
   - Can store (almost) any Python object
   - Only provides storage and retrieval

NoSQL in Python:
----------------


2. External NoSQL system:

  - Python bindings to external NoSQL system
  - Doesn't store full Python objects
  - Generally stores arbitrary collections of data (but not classes)
  - Can be simple key-value stores
     - Redis, etc...
  - Or a more full featured document database:
     in-database searching, etc.
     - mongoDB, etc...
  - Or a Map/Reduce engine:
     - Hadoop

.. nextslide::

3. Python object database:

  - Stores and retrieves arbitrary Python objects.
    - Don't need to adapt your data model at all.
  - ZODB is the only robust maintained system (I know of)


Why a DB at all?
----------------


Reasons to use a database:
  - Need to persist the data your application uses
  - May need to store more data than you can hold in memory
  - May need to have multiple apps (or multiple instances) accessing the same data
  - May need to scale -- have the DB running on a separate server(s)
  - May need to access data from systems written in different languages.


ZODB
----

The Zope Object Data Base: A native object database for Python

 * Transparent persistence for Python objects
 * Full ACID-compatible transaction support (including savepoints)
 * History/undo ability
 * Efficient support for binary large objects (BLOBs)
 * Pluggable storages
 * Scalable architecture

http://http://www.zodb.org/

MongoDB
--------

Document-Oriented Storage
 * JSON-style documents with dynamic schemas offer simplicity and power.

Full Index Support
 * Index on any attribute, just like you're used to.

Replication & High Availability
 * Mirror across LANs and WANs for scale and peace of mind.

Auto-Sharding
 * Scale horizontally without compromising functionality.

Querying
 * Rich, document-based queries.

https://www.mongodb.org/


Other Options to Consider:
--------------------------


Redis: Advanced, Scalable  key-value store.

 - http://redis.io/

Riak: High availablity/scalablity (but not so good for small)
 - http://docs.basho.com/riak/latest/dev/taste-of-riak/python/

HyperDex: "Next generation key-value store"
 - http://hyperdex.org/

Apache Cassandra: A more schema-based NoSQL solution
 - http://pycassa.github.io/pycassa/


A Data Model
------------

An Address Book with a not quite trivial data model.

There are people::

        self.first_name
        self.last_name
        self.middle_name
        self.cell_phone
        self.email

There are households::

        self.name
        self.people
        self.address
        self.phone

(similarly businesses)

``address_book_model.py``

Using ZODB
----------

ZODB stored Python objects.

To make an object persistent::

  import persistent

  class Something(persistent.Persistent):
      def __init__(self):
          self.a_field = ''
          self.another_field ''

When a change is made to the fields, the DB will keep it updated.

``code/address_book_zodb.py``

Mutable Attributes
-------------------

``Something.this = that`` will trigger a DB action

But:

``Something.a_list.append`` will not trigger anything.

The DB doesn't know that that the list has been altered.

Solution:

  ``self.a_list = PersistentList()``

(also ``PersistantDict()`` )

(or write getters and setters...)

``code/address_book_zodb.py``

mongoDB
-------

Essentially a key-value store, but the values are JSON-like objects. (Actually BSON (binary JSON) )

So you can store any object that can look like JSON:
  * dicts
  * lists
  * numbers
  * strings
  * richer than JSON.

mongoDB and Python
------------------

mongoDB is written in C++ -- can be accessed by various language drivers.

( http://docs.mongodb.org/manual/applications/drivers/ )

For Python: ``PyMongo``

http://api.mongodb.org/python/current/tutorial.html

(``pip install pymongo`` - but may need a copmiler!)

There are also various tools for integrating mongoDB with FRameworks:
 * Django MongoDB Engine
 * mongodb_beaker
 * MongoLog: Python logging handler
 * Flask-PyMongo
 * others...

Getting started with mongoDB
----------------------------

mongoDB is separate program. Installers here:

http://www.mongodb.org/downloads

Simple copy and paste install (at least on OS-X)
 (drop the files from ``bin`` into ``usr/local/bin`` or similar)

Create a dir for the database:

``$ mkdir mongo_data``

And start it up:

``$ mongod --dbpath=mongo_data/``

Creating a DB:
--------------

::

  # create the DB
  from pymongo import MongoClient

  client = MongoClient('localhost', 27017)
  store = client.store_name # creates a Database
  people = store.people # creates a collection

mongo will link to the given database ans collection, or create new ones if they don't exist.

Adding some stuff::

    people.insert({'first_name': 'Fred',
                 'last_name': 'Jones'})

Pulling Stuff Out:
------------------

And reading it back::

  In [16]: people.find_one({'first_name':"Fred"})
  Out[16]:
    {u'_id': ObjectId('534dcdcb5c84d28b596ad15e'),
     u'first_name': u'Fred',
     u'last_name': u'Jones'}

Note that it adds an ObjectID for you.

``Examples/nosql/address_book_mongo.py










