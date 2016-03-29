.. _logging:

###############################
Logging and the logging module
###############################


What is Logging?
================

..rst-class:: left

What is logging?
   In computing, a logfile is a file that records either events that occur in an operating system or other software runs, or messages between different users of a communication software.[citation needed] Logging is the act of keeping a log. In the simplest case, messages are written to a single logfile.

(https://en.wikipedia.org/wiki/Logfile)

But in fact, a file is only *one* place to keep a log. You may want to send a log of what your program is doing to another system, to the console, or????

What might you want to log?
 - System information
 - Error messages
 - Fine-grain tracing output

The logging module
-------------------

A flexible logging system that comes with the standard library

Any module using the logging api can have logging output routed the same
as your code.

Resources for learning more:

https://docs.python.org/3.5/howto/logging.html

http://docs.python-guide.org/en/latest/writing/logging/

https://pymotw.com/2/logging/

NOTE: these haven't been updated for py3 -- but not much (anything?) has changed.

Why not ``print()``?
------------------

We've all been using ``print()`` all over the place to track what's going on in a program.

And I still use it -- a lot.

But we (usually) don't want all sorts of crap sent to stdout when the program is running in production.

So we comment out or delete those ``print()``s -- but if we wanted to know what the program was doing when developing -- maybe we want to know when something goes wrong, too?

The ``logging`` module give you a flexible system that allows you to monitor what's going on in your system, when you need to, without cluttering thinks up when you don't need it.

Background
==========

There are lots of good tutorials, etc, on the web for getting you started with *useing* the logging module.

But not much about how it works -- how it is structured.

I found it hard to get beyond the basics without that knowledge, so the following should help.

The logging module provides a very flexible framework for customizing the logging in a simple or complex application.

The ``logging`` module
-----------------------
.. code-block:: python

    import logging

The logging module not only provides the classes and functions required to build a logging system, but also a place to centrally manage the logging for an entire application.

This allows you to set up logging in one place, and everywhere in the app, the system can be used.

So, for instance, when developing and debugging, you may want logging messages to go to the console, but for deployment, to log files.

That configuration can be changed in one place.

(NOTE: this is one good reason to prefer logging over ``print()``)


The ``Logger`` class
--------------------

The ``Logger`` class is the core class that handles logging.

Messages get sent to a ``Logger`` instance, and it is responsibility for routing them appropriately.

``Logger``s can be  nested in a hierarchical fashion, so that a message can be sent to the "root" logger, and passed down a chain to be handles by sub-loggers.

Each ``Logger`` represents a single logging channel.

``Logger`` instances are given text names, with module-style "dots" representing the hierarchy:

.. code-block:: python

    "main"
    "main.sub_logger1"
    "main.sub_logger2"
    ...

The "root" logger has no name, but is the root of all created loggers

The logging module keeps track of all the loggers you create, so you can reference them by name.

``logging.get_logger``
----------------------

The ``logging.get_logger`` function returns the logger you ask for.

The logging classes
-------------------

The four main classes of logging

-  Loggers  - the interface for your code
-  Handlers - handle log routing
-  Filters  - define which log messages to let through
-  Formatters - how the log messages get rendered

Basic logging usage
-------------------

Basic handling, filtering, and formatting can be done through the
logging module's ``basicConfig`` method

More complex and configurable configurations can be created with the
class interfaces for each of those tasks

Timestamps can be included by passing the ``kwarg``
``format='%(asctime)s %(message)s')`` to basicConfig

.. nextslide::

::

      import logging

      logging.basicConfig(filename='example.log', level=logging.DEBUG)
      logging.debug("debug level message")
      logging.warning("debug level message")


see ``Examples/logging/example1.py``

A more complex logging setup
----------------------------

..code-block:: python

      import logging

      # create logger
      logger = logging.getLogger('simple_example')
      logger.setLevel(logging.DEBUG)

      # create console handler and set level to debug
      handler = logging.StreamHandler()
      handler.setLevel(logging.DEBUG)

      # create formatter
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

      # add formatter to handler
      handler.setFormatter(formatter)

      # add handler to logger
      logger.addHandler(handler)

      # 'application' code
      logger.debug('debug message')
      logger.info('info message')
      logger.warn('warn message')
      logger.error('error message')
      logger.critical('critical message')
