.. _weak_references:

*********************************************
Python Memory Management and Weak References
*********************************************

Chris Barker

``PythonCHB@gmail.com``

``https://github.com/PythonCHB``

==================
Memory Management
==================

..  rst-class:: left

 * You don't want python objects that are no longer in use taking up memory.
 * You don't want to keep track of all that yourself.
 * Most "scripting languages" or "virtual machines" have some sort of
   automated memory management

.. rst-class:: center medium

    Many ways to do "Garbage Collection"


Reference Counting
--------------------

How memory is managed is not part of the Python language spec:
 * Jython uses the JVM
 * Iron Python uses the CLR
   - Both are garbage collected
 * PyPy uses Minimark_

 .. _Minimark:  https://pypy.readthedocs.org/en/release-2.4.x/garbage_collection.html#minimark-gc


The CPython interpreter uses a reference counting scheme:
 * Every time there is a new reference to a Python object, its reference
   count is increased
 * Every time a reference is removed -- the count is decreased
 * When the reference count goes to zero: the object is deleted
   (memory freed)


What makes a reference?
------------------------

* Binding to a name::

   x = an_object

* Putting it in a container::

   l.append(an_object)

* Passing it to a function::

   func(an_object)

Most of the time, you don't need to think about this at all.


How do I see what's going on?
------------------------------

.. code-block:: python


  import sys
  sys.getrefcount(object)


**NOTE:** This will always return one more than you'd expect, as passing the object to the function increases its refcount by one:

.. code-block:: ipython

  In [5]: a = []

  In [6]: sys.getrefcount(a)
  Out[6]: 2

The Heisenberg Uncertainty Principle:
   - you can't observe it without altering it


Playing with References
------------------------

(live demo)

.. code-block:: ipython

	In [7]: a = []

	In [8]: sys.getrefcount(a)
	Out[8]: 2

	In [9]: b = a

	In [10]: sys.getrefcount(a)
	Out[10]: 3

	In [11]: l = [1,2,3,a]

	In [12]: sys.getrefcount(a)
	Out[12]: 4

.. nextslide::

.. code-block:: ipython

	In [13]: del b

	In [14]: sys.getrefcount(a)
	Out[14]: 3


	In [15]: del l

	In [16]: sys.getrefcount(a)
	Out[16]: 2


.. nextslide::


.. code-block:: ipython

    # function local variables

	In [17]: def test(x):
	   ....:     print "x has a refcount of:", sys.getrefcount(x)
	   ....:

	In [18]: sys.getrefcount(a)
	Out[18]: 2

	In [19]: test(a)
	x has a refcount of: 4

	In [20]: sys.getrefcount(a)
	Out[20]: 2


.. nextslide::

.. code-block:: ipython

	In [21]: x = 3

	In [22]: sys.getrefcount(x)
	Out[22]: 428

WHOA!!

(hint: interning....)


The Power of Reference Counting
--------------------------------


* You don't need to think about it most of the time.

* Code that creates objects doesn't need to delete them

* Objects get deleted right away

   . They can "clean up" on deletion (files, for instance) -- and it will happen right away.

* Performance is predictable


The Limits of Reference Counting
--------------------------------

* Performance overhead on all operations. But the big one:

.. rst-class:: medium

  Circular references

If a python object somehow references itself -- i.e. it references another object that references the first
object:

You have a circular reference ...

===================
Circular References
===================

.. rst-class:: left

    .. code-block:: ipython

        In [8]: l1 = [1,] ; l2 = [2,]

        In [9]: l1.append(l2); l2.append(l1)

        In [10]: l1
        Out[10]: [1, [2, [...]]]

        In [11]: l2
        Out[11]: [2, [1, [...]]]

        In [12]: l1[1]
        Out[12]: [2, [1, [...]]]

        In [13]: l2[1][1][1]
        Out[13]: [1, [2, [...]]]

(demo) -- :download:`simple_circular.py <../code/weak_references/simple_circular.py>`


The Garbage Collector
----------------------

As of Python 2.0 -- a garbage collector was added.

 - (https://docs.python.org/2/library/gc.html)

It can find and clean up "unreachable" references.

It is turned on by default::

	In [1]: import gc
	In [2]: gc.isenabled()
	Out[2]: True

or you can force it::

	In [4]: gc.collect()
	Out[4]: 64

But it can be slow, and doesn't always work!

.. nextslide::

How does the garbage collector work?

  * Not a full "mark and sweep" type.

It searches for reference cycles -- then cleans those up.

   * It doesn't have to bother checking non-container types (ints, strings, etc.)

   * Faster, and not as dependent on having a clear "root" namespace.

Details here:

http://arctrix.com/nas/python/gc/  (or in the source!)

Big issue: classes that define a ``__del__`` method are not cleaned up.

  * ``__del__`` methods often act on references that may no be there if
    they are cleaned up in the wrong order.

NOTE: you can work with gc.garbage() -- but tricky and messy

=====
Tools
=====

.. rst-class:: left

    If these objects are no longer "reachable" -- how do you find out what's going on?

    We saw ``sys.getrefcount()`` -- but you need a reference to the object to use it.

    You can see what the refcount is before you delete the last reference, but that isn't always easy.


Process Memory Use
-------------------

A really coarse way to find a memory leak is to see if the process memory
is growing.

It can be subtle --python (and the OS) do tricks to re-use memory, etc.

But if you have a "real" leak -- you'll see it. (Example to follow)

:download:`mem_check.py <../code/weak_references/mem_check.py>`

provides functions that report the memory use of the current running process.

(\*nix and Windows code)

id checks
----------

As it happens, the Python ``id()`` function returns a memory address.

It's really dangerous, but that means we can examine an object if we know
its `id`, even if we don't hold a reference to it.

Bill Bumgarner wrote a nifty extension module that returns the python
object pointed to by an id (memory address) -- "di":

http://www.friday.com/bbum/2007/08/24/python-di/

I added a function that returns the reference count of an object from its id.

https://github.com/PythonCHB/di_refcount

NOTE: it would be a really bad idea to use these in production code!

Examples
----------

:download:`simple_circular_di.py <../code/weak_references/simple_circular_di.py>`

uses the ref_by_id() function to see what's going on with a circular
reference and garbage collection.

More real examples in iPython notebook:

:download:`CircularReferenceExample.ipynb  <../code/weak_references/CircularReferenceExample.ipynb>`

Or: :download:`circular.py <../code/weak_references/circular.py>`

:download:`memcount.py <../code/weak_references/memcount.py>` is a test
file that show memory growth if circular references are not cleaned up.

( :download:`mem_check.py <../code/weak_references/mem_check.py>` )
is code that reports process memory use.

You can find this code in the main repo here:

https://github.com/PythonCHB/PythonTopics/tree/master/Sources/code/weak_references


Weak References
-----------------

For times when you don't want to keep objects alive, Python provides
"weak references" -- we saw this in the examples.

(https://docs.python.org/2/library/weakref.html)

1. The built-in containers:

  - ``WeakKeyDictionary``

  - ``WeakValueDictionary``

  - ``WeakSet``

2. ``Proxy`` objects

  - act much like regular references -- client code doesn't know the difference

3. ``WeakRef`` objects

  - When you want to control what happens when the referenced object is gone.

=========
Exercise
=========

.. rst-class:: left

    Build a "weak cache":

    For large objects that are expensive to create:

    * Use a WeakValueDictionay to hold references to (probably large) objects.

    * When the client requests an object that doesn't exist -- one is created, returned, and cached (weakly).

    * If the object is in the cache, it is returned.

    * when no other references exist to the object, it is NOT retained by the cache.

