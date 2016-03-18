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

http://www.pythontutor.com/visualize.html#mode=edit

.. nextslide::

Visualize the stack!
--------------------

.. image:: /_static/program_callstack.png
   :height: 580 px

.. nextslide::

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

If we try to put more than sys.getrecursionlimit() frames on the stack, we get a RuntimeError, which is python's version of StackOverflow

.. nextslide::

.. code-block:: ipython

    import inspect

    def recurse(limit):
        local_variable = '.' * limit
        print limit, inspect.getargvalues(inspect.currentframe())
        if limit <= 0:
            return
        recurse(limit - 1)
        return

    if __name__ == '__main__':
        recurse(3)


module <https://docs.python.org/2/library/inspect.html>`__

.. nextslide::

Exceptions
----------

It's easier to ask for forgiveness than permission

When either the interpreter or your own code detects an error condition,
an exception will be raised

The exception will bubble up the call stack until it is handled. If it's
not, the interpreter will exit the program.

.. nextslide::

At each level in the stack, a handler can either:

-  let it bubble through (the default)
-  swallow the exception
-  catch the exception and raise it again
-  catch the exception and raise a new one

.. nextslide::

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


.. nextslide::

.. rubric:: A few more builtins for exception handling: finally, else,
   and raise
   :name: a-few-more-builtins-for-exception-handling-finally-else-and-raise

::

    try:
        result = x / y

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

.. nextslide::

.. rubric:: Built-in exceptions
   :name: built-in-exceptions

::

    [name for name in dir(__builtin__) if "Error" in name]

Use the builtin exceptions when you can, add messages if you need to.
If none meet your needs, define a new exception type by subclassing one,
perhaps Exception.


If one of these meets your needs, by all means use it. Else, define a
new exception type by subclassing one, perhaps Exception


.. nextslide::

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


.. nextslide::

.. rubric:: Further reading
   :name: further-reading

-  https://wiki.python.org/moin/HandlingExceptions
-  http://docs.python.org/2/library/exceptions.html
-  http://docs.python.org/2/tutorial/errors.html


.. nextslide::

Debugging
---------

.. rubric:: Python Debugging
   :name: python-debugging

You will spend most of your time as a developer debugging. 
You will spend more time than you expect on google.


Debuggers are code which allows the inspection of state of other code
during runtime.

Rudimentary tools

-  print()
-  interpreter hints
-  import logging.debug
-  assert()

.. nextslide::

Console debuggers

-  pdb/ipdb

GUI debuggers

-  Winpdb
-  IDEs: Eclipse, Wing IDE, PyCharm, Visual Studio

.. nextslide::

.. rubric:: help from the interpreter
   :name: help-from-the-interpreter

investigate import issues with -v

inspect environment after running script with -i


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
