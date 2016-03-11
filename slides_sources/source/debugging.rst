.. _debugging:

#########
Debugging
#########

- Maria McKinley


``parody@uw.edu``


Topics
######

-  The call stack
-  Exceptions
-  Iterators
-  Debugging


The Call Stack
--------------

-  A stack is a Last-In-First-Out (LIFO) data structure (stack of plates)
-  The call stack is a stack data structure that stores information
   about the current active function call
-  The objects in the stack are known as "stack frames". Each frame
   contains the arguments passed to the function, space for local
   variables, and the return address
-  When a function is called, a stack frame is created for it and pushed
   onto the stack
-  When a function returns, it is popped off the stack and control is
   passed to the next item in the stack. If the stack is empty, the
   program exits


.. nextslide::

Visualize the stack!
--------------------

http://www.pythontutor.com/visualize.html#mode=edit


|image0|

.. rubric:: How deep can that stack be?
   :name: how-deep-can-that-stack-be

::

    i = 0

    def recurse():
        global i
        i += 1
        print i
        recurse()

    recurse()
      

That value can be changed with sys.setrecursionlimit(N)
if we try to put more than sys.getrecursionlimit() frames on the stack, we get a RuntimeError, which is python's version of StackOverflow

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: inspecting frames in the call stack
   :name: inspecting-frames-in-the-call-stack

::

    import sys, traceback

    def one():
        one_local_var = "foo"
        two()

    def two():
        two_local_var = "foo"
        three()

    def three():
        # print the stack
        for num in range(3):
            frame = sys._getframe(num)
            show_frame(num, frame)

        # or,
        traceback.print_stack()
        # or more rudely
        1/0

    def show_frame(num, frame):
        print "  frame     = sys._getframe(%s)" % num
        print "  function  = %s()" % frame.f_code.co_name
        print "  file/line = %s:%s" % (frame.f_code.co_filename, frame.f_lineno)
        print "  locals: %s" % frame.f_locals.keys()

    one()
      

Also see the `inspect
module <https://docs.python.org/2/library/inspect.html>`__

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Exceptions
   :name: exceptions

.. rubric:: It's easier to ask for forgiveness than permission
   :name: its-easier-to-ask-for-forgiveness-than-permission

.. raw:: html

   <div class="slide">

When either the interpreter or your own code detects an error condition,
an exception may be raised

The exception will bubble up the call stack until it is handled. If it's
not, the interpreter will exit.

At each level in the stack, a handler can either:

-  let it pass through (the default)
-  swallow the exception
-  catch the exception and raise it again
-  catch the exception and raise a new one

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Handling exceptions
   :name: handling-exceptions

The most basic form uses the builtins try and except

::

    try:
        print "do some stuff"
        1 / 0
        print "do some more stuff"
    except:
        print "stuff failed"

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: A few more builtins for exception handling: finally, else,
   and raise
   :name: a-few-more-builtins-for-exception-handling-finally-else-and-raise

::

    def divide(x, y):

    try:
        print "line 1"
        result = x / y
        print "line 2"

    except ZeroDivisionError as e:
        print "caught division error: %s" % str(e)

    except Exception as e:
        print "unhandled exception %s.  message: %s " % (type(e), e.args)
        raise

    else:
        print "everything worked great"
        return result

    finally:
        print "this is executed no matter what"

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Built-in exceptions
   :name: built-in-exceptions

::

    [name for name in dir(__builtin__) if "Error" in name]

If one of these meets your needs, by all means use it. Else, define a
new exception type by subclassing one, perhaps Exception

::

    In [32]: import exceptions
    In [33]: exceptions?
    Type:       module
    String Form:
    Docstring:
    Python's standard exception class hierarchy.

    Exceptions found here are defined both in the exceptions module and the
    built-in namespace.  It is recommended that user-defined exceptions
    inherit from Exception.  See the documentation for the exception
    inheritance hierarchy.

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Exercise
   :name: exercise

Modify the example program examples/wikidef

Enforce the argument to api.Wikipedia.title to have length greater than
0

If a 0 length argument is passed to this function, raise a new exception
called ZeroLengthTitleError

Handle this exception in the caller (Not necessarily the immediate
caller, which one makes sense to you?)

Feel free to edit the code in place. You can throw away your changes at
the end with "git reset --hard", store them for later with "git stash",
or commit them!

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Further reading
   :name: further-reading

-  https://wiki.python.org/moin/HandlingExceptions
-  http://docs.python.org/2/library/exceptions.html
-  http://docs.python.org/2/tutorial/errors.html

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Exceptions aren't just for errors
   :name: exceptions-arent-just-for-errors

Exception handling can be used for control flow as well

i.e. StopIteration for iterators

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Iterators
   :name: iterators

Iterators are objects which support a concept of iteration over a
collection

::

    # looping over the lines in a file is done via an iterator:
      with open("file.dat") as f:
          for line in f:
              print line

      # and you can create your own
      for x in foo():
          print x

An iterator is an object which follows the Python `iterator
protocol <https://docs.python.org/2/library/stdtypes.html#container.__iter__>`__

An iterator defines two required methods in order to iterate

-  \_\_iter\_\_() returns the iterator itself
-  next() returns the next item in the sequence

http://docs.python.org/2/library/stdtypes.html#iterator-types

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Demonstration iterator
   :name: demonstration-iterator

::

    class CountToTen(object):
          """an iterator which returns integers from 0 to 9, inclusive"""

          def __init__(self):
              self.data = range(10)

          def __iter__(self):
              return self

          def next(self):
              try:
                  return self.data.pop(0)
              except IndexError:
                  raise StopIteration

      for x in CountToTen():
          print x

      # or consume the whole thing at once by converting to a list:
      list(CountToTen())
      

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Now let's build an iterator
   :name: now-lets-build-an-iterator

Calculate the first 20 values in the Fibonacci sequence: [0, 1, 1, 2, 3,
5, ... ] using an iterator

The Fibonnaci sequence is defined as such:

The first two integers in the sequence are 0 and 1
Each member of the sequence is the sum of the previous two elements
::

    for x in FibonacciIterator(20):
      print x
          

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: generators
   :name: generators

A `generator <https://wiki.python.org/moin/Generators>`__ is a concrete
type that implements the iterator protocol.

Convert a function to a generator using the yield keyword

::

    def count_to_10():
        for i in range(10):
            yield i

    for x in count_to_10():
        print x
          

(4700 upvotes on this stackoverflow question, yield is confusing at
first)

http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Using a generator expression to create a generator
   :name: using-a-generator-expression-to-create-a-generator

Python list comprehensions allow you to build lists of values

::

    my_list = [x for x in open('file.dat')]

Convert that list comprehension to a generator just by replacing '[]'
with '()'

::

    my_generator = (x for x in open('file.dat'))

https://wiki.python.org/moin/Generators

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Python Debugging
   :name: python-debugging

Debuggers are code which allows the inspection of state of other code
during runtime.

.. raw:: html

   <div class="slide">

Rudimentary tools

-  print()
-  interpreter hints
-  import logging.debug
-  assert()

Console debuggers

-  pdb/ipdb

GUI debuggers

-  Winpdb
-  IDEs: Eclipse, Wing IDE, PyCharm, Visual Studio

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: help from the interpreter
   :name: help-from-the-interpreter

investigate import issues with -v

inspect environment after running script with -i

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: the logging module
   :name: the-logging-module

A flexible logging system that comes with the standard library

Any module using the logging api can have logging output routed the same
as your code

The four main classes of logging

-  Loggers - the interface for your code
-  Handlers - handle log routing
-  Filters - define which log messages to let through
-  Formatters - how the log messages get rendered

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: basic logging usage
   :name: basic-logging-usage

Basic handling, filtering, and formatting can be done through the
logging module's basicConfig method

More complex and configurable configurations can be created with the
class interfaces for each of those tasks

Timestamps can be included by passing the kwarg
``format='%(asctime)s %(message)s')`` to basicConfig

::

      import logging

      logging.basicConfig(filename='example.log', level=logging.DEBUG)
      logging.debug("debug level message")
      logging.warning("debug level message")

      

see examples/logging/example1.py

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: A more complex logging setup
   :name: a-more-complex-logging-setup

::

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
      

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: `Pdb - The Python
   Debugger <http://docs.python.org/2/library/pdb.html>`__
   :name: pdb---the-python-debugger

Pros:

-  You have it already, ships with the standard library
-  Easy remote debugging
-  Works with any development environment

Cons:

-  Steep-ish learning curve
-  Easy to get lost in a deep stack
-  Watching variables isn't hard, but non-trivial

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: `Pdb - The Python
   Debugger <http://docs.python.org/2/library/pdb.html>`__
   :name: pdb---the-python-debugger-1

The 4-fold ways of invoking pdb

-  Postmortem mode
-  Run mode
-  Script mode
-  Trace mode

Note: in most cases where you see the word 'pdb' in the examples, you
can replace it with 'ipdb'. ipdb is the ipython enhanced version of pdb
which is mostly compatible, and generally easier to work with. But it
doesn't ship with Python.

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Postmortem mode
   :name: postmortem-mode

For analyzing crashes due to uncaught exceptions

::

          python -i script.py
          import pdb; pdb.pm()
          

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Run mode
   :name: run-mode

::

          pdb.run('some.expression()')
          

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Script mode
   :name: script-mode

::

          python -m pdb script.py
          

"-m [module]" finds [module] in sys.path and executes it as a script

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Trace mode
   :name: trace-mode

Insert the following line into your code where you want execution to
halt:

::

          import pdb; pdb.set_trace()
          

It's not always OK/possible to modify your code in order to debug it,
but this is often the quickest way to begin inspecting state

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: pdb in ipython
   :name: pdb-in-ipython

::

          
          In [2]: pdb
          Automatic pdb calling has been turned ON

          %run app.py

          # now halts execution on uncaught exception

          
          

If you forget to turn on pdb, the magic command %debug will activate the
debugger (in 'post-mortem mode').

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Navigating pdb
   :name: navigating-pdb

The goal of each of the preceding techniques was to get to the pdb
prompt and get to work inspecting state

::

    % python -m pdb define.py robot
      pdb> break api.py:21
      # list breakpoints
      pdb> break
      pdb> clear 1
      # print lines of code in current context
      pdb> list
      # print lines in range
      pdb> list 1,28
      # print stack trace, aliased to (bt, w)
      pdb> where
      # move one level up the stack
      pdb> up
      # move one level down the stack
      pdb> down
      # execute until function returns
      pdb> return
      # Execute the current line, stop at the first possible occasion
      pdb> step
      # Continue execution until the next line in the current function is reached or it returns.
      pdb> next
      # Continue execution until the line with a number greater than the current one is reached or until the current frame returns.  Good for exiting loops.
      pdb> until
      # create commands to be executed on a breakpoint
      pdb> commands
      pdb> continue

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Breakpoints
   :name: breakpoints

::

    pdb> help break
      b(reak) ([file:]lineno | function) [, condition]
      With a line number argument, set a break there in the current
      file.  With a function name, set a break at first executable line
      of that function.  Without argument, list all breaks.  If a second
      argument is present, it is a string specifying an expression
      which must evaluate to true before the breakpoint is honored.

      The line number may be prefixed with a filename and a colon,
      to specify a breakpoint in another file (probably one that
      hasn't been loaded yet).  The file is searched for on sys.path;
      the .py suffix may be omitted.

Clear (delete) breakpoints

::

          clear [bpnumber [bpnumber...]]
          

disable breakpoints

::

          disable [bpnumber [bpnumber...]]
          

enable breakpoints

::

          enable [bpnumber [bpnumber...]]
          

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Conditional Breakpoints
   :name: conditional-breakpoints

::

          pdb> help condition
          condition bpnumber str_condition
          str_condition is a string specifying an expression which
          must evaluate to true before the breakpoint is honored.
          If str_condition is absent, any existing condition is removed;
          i.e., the breakpoint is made unconditional.
          

Set conditions

::

          condition 1 x==1
          

Clear conditions

::

          condition 1
          

see debugging/examples/long\_loop.py

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Invoking pdb with nose
   :name: invoking-pdb-with-nose

On error condition, drop to pdb

::

    nosetests --pdb
      

On test failure, drop to pdb:

::

    nosetests --pdb-failures
      

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Python IDEs
   :name: python-ides

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: PyCharm
   :name: pycharm

From JetBrains, and integrates some of their vast array of development
tools

Free Community Edition (CE) is available

Good visual debugging support

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Eclipse
   :name: eclipse

A multi-language IDE

Python support via http://pydev.org/

Automatic variable and expression watching

Supports a lot of debugging features like conditional breakpoints,
provided you look in the right places!

Further reading

http://pydev.org/manual_adv_debugger.html

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: winpdb
   :name: winpdb

A multi platform Python debugger with threading support

Easier to start up and get debugging

::

          
          winpdb your_app.py
          
          

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Remote debugging with winpdb
   :name: remote-debugging-with-winpdb

To debug an application running a different Python, even remotely:

::

          
          import rpdb2; rpdb2.start_embedded_debugger("password")
          
          

http://winpdb.org/tutorial/WinpdbTutorial.html

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Debugging exercise
   :name: debugging-exercise

Find the wikidef app in the examples folder

Using (i)pdb in module mode (python -m pdb ) debug the app and find the
server type that wikipedia is using by looking at
response.headers.headers in Wikipedia.article

You can enter the debugger by running

::

    python -m pdb ./define.py robot

You can get to the code by walking through each line with 's'tep and
'n'ext commands, or by setting a breakpoint and 'c'ontinuing.

What's the result?

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Questions?
   :name: questions

.. raw:: html

   </div>

.. raw:: html

   <div aria-role="navigation">

`← <#>`__ `→ <#>`__

.. raw:: html

   </div>

 /

.. raw:: html

   </div>

.. |image0| image:: images/ProgramCallStack2.png

