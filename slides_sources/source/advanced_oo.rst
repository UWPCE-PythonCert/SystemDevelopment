.. _advanced_oo:

############################################
Advanced Object Oriented Features of Python
############################################

- Chris Barker


``PythonCHB@gmail.com``


Multiple Inheritance
#####################


Pulling methods from more than one class


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
            print("doing A's stuff")

    class B(A):
        def do_your_stuff(self):
            A.do_your_stuff(self)
            print("doing B's stuff")

    class C(A):
        def do_your_stuff(self):
            A.do_your_stuff(self)
            print("doing C's stuff")

    class D(B,C):
        def do_your_stuff(self):
            B.do_your_stuff(self)
            C.do_your_stuff(self)
            print("doing D's stuff")


The Diamond Problem
--------------------

Multiple paths to the same superclass:

.. image:: /_static/Diamond_inheritance.png
    :align: center
    :height: 400px

A's methods can get called twice.

(demo: ``Examples/advancedOO/diamond.py``)


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
| demo: ``Examples/week-06-OO/super_test.ipnb``


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

.. nextslide::

First: Python 3 has cleaned this up, it's just:

.. code-block:: python

  class B(A):
      def a_method(self, *args, **kwargs)
          super().a_method(*args, **kwargs)

In py3.

In Python2, super was tacked on, so the additonal info is
needed, and it does have the advantage of being explicit about the two
inputs to the computation (the mro of self and the current position in
the mro).

Note that while `self` needs to be a subclass of B here, it may not
actually be an *instance* of B -- it could be a subclass.

That's why both need to be specified.


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

LAB
----

In ``Examples/week-06-OO/mixins.py``, you will find a few Vehicle classes
laid out in a hierarchy

The log() method is defined on Vehicle then called on a couple of
instances

Modify the class definition for Bike to mix in fancier log() method
from LoggingMixin

Does the output change accordingly? If it didn't, look at the MRO for
Bike? Is it what you expected?


__new__
########

.. rst-class:: large

  Into the depths of object creation:

.. rst-class:: medium

  What *really* happens when a class instance is created?

Class Creation
----------------

What happens when a class instance is created?

This is the usual thing...

.. code-block:: python

    class Class(object):
        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
            .....

* A new instance is created
* ``__init__`` is called
* The code in ``__init__`` is run to initialize the instance

Note that ``self`` is already an instance of the class.

.. nextslide::

What if you need to do something before creation?

Enter: ``__new__``

.. code-block:: python

    class Class(object):
        def __new__(cls, arg1, arg2):
            some_code_here
            return cls(...)
            ...

* ``__new__`` is called: it returns a new instance

* The code in ``__new__`` is run to pre-initialize the instance

* ``__init__`` is called

* The code in ``__init__`` is run to initialize the instance


.. nextslide::

``__new__`` is a static method -- but it must be called with a class object as the first argument.

.. code-block:: python

    class Class(superclass):
        def __new__(cls, arg1, arg2):
            some_code_here
            return superclass.__new__(cls)
            .....

``cls`` is the class object.

The arguments (arg1, arg2) are what's passed in when calling the class.

It needs to return a class instance -- usually by directly calling the superclass ``__new__``

If nothing else, you can call ``object.__new__``


When to use ``__new__``
------------------------

.. rst-class:: medium

  When would  you need to use it:

* Subclassing an immutable type:

  - It's too late to change it once you get to ``__init__``

* When ``__init__`` is not called:

  - unpickling

  - copying

You may need to put some code in ``__new__`` to make sure things
go right

More detail here:

http://www.python.org/download/releases/2.7/descrintro/#__new__


LAB
----

**Demo:**

 ``Examples/advancedOO/new_example.py``

**Exercise:**

Write a subclass of int that will always be an even number:
round the input to the closest even number:

  ``Examples/advancedOO/even_int.py``


  ``Examples/advancedOO/test_even_int.py``


Wrap Up
-------

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


