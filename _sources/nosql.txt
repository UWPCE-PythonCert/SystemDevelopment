.. _nosql:



Non RDBMS Database Options
===========================

NoSQL databases
----------------

In "NoSQL" these key features are mostly shared:

-  "schema less" - Document oriented
-  More direct mapping to an object model.
-  Scalable - Easy to distribute / parallelize

Database Schema
----------------

A database schema is the organization of data, and description of how a
database is constructed: Divided into database tables, and
relationships: foreign keys, etc.

Includes what fields in what tables, what data types each field is,
normalization of shared data, etc.

This requires work up-front, and can be hard to adapt as the system
requirements change.

It can also require effort to map your programming data model to the
schema.


Schemaless
-----------

Schemaless databases generally follow a "document model".

Each entry in the database is a "document":

-  essentially an arbitrary collection of fields.
-  often looks like a Python dict.

Not every entry has to have exactly the same structure.

Maps well to dynamic programming languages.

Adapts well as the system changes.

NoSQL in Python:
-----------------

Three Categories:

1. Simple key-value object store

-  `shelve <https://docs.python.org/2/library/shelve.html>`__, based on
   `pickle <https://docs.python.org/2/library/pickle.html>`__ and
   `anydbm <https://docs.python.org/2/library/anydbm.html>`__
-  Can store any `picklable Python
   object <https://docs.python.org/2/library/pickle.html#what-can-be-pickled-and-unpickled>`__
-  Only provides storage and retrieval

2. External NoSQL systems
-------------------------

-  Python bindings to external NoSQL system
-  Doesn't store full Python objects
-  Generally stores arbitrary collections of data (but not classes)
-  Can be simple key-value stores - Redis, etc...
-  Or a more full featured document database: in-database searching,
   etc. - mongoDB, etc...
-  Or a Map/Reduce engine: - Hadoop


3. Python object database
--------------------------

-  Stores and retrieves arbitrary Python objects.
-  Don't need to adapt your data model at all.
-  ZODB is the most robust and maintained system

`ZODB <http://http://www.zodb.org/>`__
--------------------------------------

The Zope Object Data Base: A native object database for Python

-  Transparent persistence for Python objects
-  Full ACID-compatible transaction support (including savepoints)
-  History/undo ability
-  Efficient support for binary large objects (BLOBs)
-  Pluggable storages
-  Scalable architecture



`MongoDB <https://www.mongodb.org/>`__
---------------------------------------

-  Document-Oriented Storage - JSON-style documents with dynamic schemas
   offer simplicity and power.
-  Full Index Support - Index on any attribute, just like you're used
   to.
-  Replication and High Availability - Mirror across LANs and WANs for
   scale and peace of mind.
-  Auto-Sharding - Scale horizontally without compromising
   functionality.
-  Querying - Rich, document-based queries.

Other Options to Consider
-------------------------


`Redis <http://redis.io/>`__: Advanced, Scalable key-value store.

`Riak <http://docs.basho.com/riak/latest/dev/taste-of-riak/python/>`__:
High availability/scalablity

`HyperDex <http://hyperdex.org/>`__: "Next generation key-value store"

`Apache Cassandra <http://pycassa.github.io/pycassa/>`__: A more
schema-based NoSQL solution


Example Data Model
-------------------

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

see examples/NoSQL/address\_book\_model.py

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Using ZODB
   :name: using-zodb

ZODB stores Python objects. To make an object persistent:

::

    import persistent

    class Something(persistent.Persistent):
      def __init__(self):
          self.a_field = ''
          self.another_field ''

When a change is made to the fields, the DB will keep it updated.

See examples/NoSQL/address\_book\_zodb.py

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Mutable Attributes in ZODB
   :name: mutable-attributes-in-zodb

::

    Something.this = that
    # will trigger a DB action

    # But:

    Something.a_list.append
    # will not trigger anything.

    # The DB doesn't know that that the list has been altered.
    # Solution:

    self.a_list = PersistentList()
    # (also PersistantDict() )

    # (or write getter and setter properties...)

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: MongoDB
   :name: mongodb-1

Essentially a key-value store, but the values are JSON-like objects in
the `BSON (binary JSON) <http://bsonspec.org/>`__ format

So you can store any object that can look like JSON:

-  dicts
-  lists
-  numbers
-  strings
-  richer than JSON.

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: MongoDB and Python
   :name: mongodb-and-python

MongoDB is written in C++ -- can be accessed by various language
`drivers <http://docs.mongodb.org/manual/applications/drivers/>`__

For Python we have
`PyMongo <http://api.mongodb.org/python/current/tutorial.html%0A>`__

There are also various tools for integrating mongoDB with Python
frameworks:

-  Django MongoDB Engine
-  mongodb\_beaker
-  MongoLog: Python logging handler
-  Flask-PyMongo
-  others...

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Getting started with mongoDB
   :name: getting-started-with-mongodb

mongoDB is separate program. Installers here:
http://www.mongodb.org/downloads

Create a dir for the database:

::

    $ mkdir mongo_data
    # And start it up:
    $ mongod --dbpath=mongo_data/

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Creating a Mongo DB:
   :name: creating-a-mongo-db

::

    # create the DB
    from pymongo import MongoClient

    client = MongoClient('localhost', 27017)
    store = client.store_name # creates a Database
    people = store.people # creates a collection

mongo will link to the given database and collection, or create new ones
if they don't exist.

Adding some stuff:

::

    people.insert({'first_name': 'Fred',
                  'last_name': 'Jones'})

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

Pulling Data Out
-----------------

::

    In [16]: people.find_one({'first_name':"Fred"})
    Out[16]:
    {u'_id': ObjectId('534dcdcb5c84d28b596ad15e'),
     u'first_name': u'Fred',
     u'last_name': u'Jones'}

Note that it adds an ObjectID for you. See
examples/NoSQL/address\_book\_mongo.py


Questions?
