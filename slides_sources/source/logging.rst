.. _logging:

###############################
Logging, and the logging module
###############################


Logging
=======

Logging 

 - Chris Barker

The logging module
-------------------

A flexible logging system that comes with the standard library

Any module using the logging api can have logging output routed the same
as your code

.. nextslide::

The four main classes of logging

-  Loggers - the interface for your code
-  Handlers - handle log routing
-  Filters - define which log messages to let through
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
      
