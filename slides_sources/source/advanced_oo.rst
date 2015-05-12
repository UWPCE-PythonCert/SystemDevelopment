.. _advanced_oo:

===========================================
Advanced Object Oriented Features of Python
===========================================

- Chris Barker


``PythonCHB@gmail.com``


Multiple Inheritance
====================


Pulling methoda from more than one class


multiple inheritance
---------------------

.. code-block:: python

    class Combined(Super1, Super2, Super3):
        def __init__(self, something, something else):
            Super1.__init__(self, ......)
            Super2.__init__(self, ......)
            Super3.__init__(self, ......)

(calls to the super classes ``__init__`` are optional and case dependent)


.. nextslide::

**Method Resolution Order:**  left to right

1. Is it an instance attribute ?

2. Is it a class attribute ?

3. Is it a superclass attribute ?

   a. is it an attribute of the left-most superclass?

   b. is it an attribute of the next superclass?

   c. ``....``

4. Is it a super-superclass attribute ?

5. also left to right...


( This can get complicated --- more on that later...)

Mix-ins
--------

Why would you want to do this?


Hierarchies are not always simple:


* Animal

  * Mammal

    * GiveBirth()

  * Bird

    * LayEggs()

Where do you put a Platypus?


Real World Example: ``wxPython FloatCanvas``


The Diamond Problem
--------------------

.. code-block:: python

    class A(object):
        def do_your_stuff(self):
            print "doing A's stuff"

    class B(A):
        def do_your_stuff(self):
            A.do_your_stuff(self)
            print "doing B's stuff"

    class C(A):
        def do_your_stuff(self):
            A.do_your_stuff(self)
            print "doing C's stuff"

    class D(B,C):
        def do_your_stuff(self):
            B.do_your_stuff(self)
            C.do_your_stuff(self)
            print "doing D's stuff"


The Diamond Problem
--------------------

Multiple paths to the same superclass:

.. image:: /_static/Diamond_inheritance.png
    :align: center
    :height: 400px

A's methods can get called twice.

(demo: ``Examples/week-06-OO/diamond.py``)


The Method Resolution Order
----------------------------

Python's The Method Resolution Order ( MRO ) is defined by the C3
linearization algorithm:

http://en.wikipedia.org/wiki/C3_linearization.

In C3, only the last occurrence of a given class is retained.

In short: corrects the multiple calls to the same method problem

The classic description of modern MRO by Guido:

http://www.python.org/download/releases/2.2.2/descrintro/#mro

And one more:

http://www.python.org/download/releases/2.3/mro/

demo: ``__mro__``

super()
-------

Getting the superclass:

.. code-block:: python

    class SafeVehicle(Vehicle):
        """
        Safe Vehicle subclass of Vehicle base class...
        """
        def __init__(self, position=0, velocity=0, icon='S'):
            Vehicle.__init__(self, position, velocity, icon)


``Vehicle`` is repeated here -- what if we wanted to change the superclass?

And there were a bunch of references to Vehicle?


super()
--------

Getting the superclass:

.. code-block:: python

    class SafeVehicle(Vehicle):
        """
        Safe Vehicle subclass of Vehicle base class
        """
        def __init__(self, position=0, velocity=0, icon='S'):
            super(SafeVehicle, self).__init__(position, velocity, icon)


``super`` is about more than just making it easier to refactor.

Remember the method resolution order?

And the diamond problem?


What does super() do?
----------------------

``super`` returns a "proxy object" that delegates method calls.


It's not returning the object itself -- but you can call methods on it.


It runs through the method resolution order (MRO) to find the method
you call.


Key point: the MRO is determined *at run time*


http://docs.python.org/2/library/functions.html#super


.. nextslide::

Not the same as calling one superclass method: ``super()``
will call all the sibling superclass methods: ::

    class D(C, B, A):
        def __init__(self):
           super(D, self).__init__()

same as::

    class D(C, B, A):
        def __init__(self):
           C.__init__()
           B.__init__()
           A.__init__()

| You may not want that --
| demo: ``code /super_test.ipnb``


super() mechanics
------------------

Notice this (frankly ugly) requirement:

.. code-block:: python

  super(type[, object-or-type])

which usually is somethign like:

.. code-block:: python

  class B(A):
      def a_method(self, *args, **kwargs)
          super(B, self).a_method(*args, **kwargs)

So why in the world do you need to specify both `B` (the type), and
`self` (the instance?)

First: Python 3 has cleaned this up, it's just:

.. code-block:: python

  class B(A):
      def a_method(self, *args, **kwargs)
          super().a_method(*args, **kwargs)

In py3. But in Python2, super was tacked on, so the additonal info is
needed, and it does have the advantage of being explicit about the two
inputs to the computation (the mro of self and the current position in
the mro).

Note that while `self` needs to be a subclass of B here, it may not
actually be an *instance* of B -- it could be a subclass.

That's why both need to be specified.

**But I'm specifying the class name twice, still!**

The first argument to ``super()`` must be the class object that you want
the superclass of -- that is the class you are currently defining. But
you don't need to write that specifically -- you can use its
``__class__`` magic method:

.. code-block:: python

  class B(A):
      def a_method(self, *args, **kwargs)
          super(self.__class__, self).a_method(*args, **kwargs)


That way you only specify the superclass in one place.

More detail about super()
-------------------------

Two seminal articles about ``super()``:


"*Super Considered Harmful*"

  - James Knight

https://fuhm.net/super-harmful


"*super() Considered Super!*"

  - Raymond Hettinger


http://rhettinger.wordpress.com/2011/05/26/super-considered-super


(Both worth reading....)


super() issues...
-----------------

Both actually say similar things:

* The method being called by super() needs to exist
* Every occurrence of the method needs to use super():

  - Use it consistently, and document that you use it, as it is part
    of the external interface for your class, like it or not.

calling super():
-----------------

The caller and callee need to have a matching argument signature:

Never call super with anything but the exact arguments you received,
unless you really know what you're doing.

If you add one or more optional arguments, always accept

.. code-block:: python

  *args, **kwargs

and call super like

.. code-block:: python

  super(MyClass, self).method(args_declared, *args, **kwargs)




Wrap Up
---------

Thinking OO in Python:


Think about what makes sense for your code:

* Code re-use
* Clean APIs
* ...


Don't be a slave to what OO is *supposed to look like*.


Let OO work for you, not *create* work for you.


Wrap Up
--------

OO in Python:


*The Art of Subclassing*:  -- Raymond Hettinger


  http://pyvideo.org/video/879/the-art-of-subclassing


"classes are for code re-use -- not creating taxonomies"


*Stop Writing Classes*:  -- Jack Diederich


http://pyvideo.org/video/880/stop-writing-classes

"If your class has only two methods and one of them is ``__init__`` -- you don't need a class"

and

"I hate code: I want as little of it in our product as possible"


