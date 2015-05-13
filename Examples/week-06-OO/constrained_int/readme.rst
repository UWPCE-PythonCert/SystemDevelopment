__new__ example
---------------

A little excercise for __new__ and making a new class act like a regular type.

Here is a replacement for int which can only take new values between 0 and 255:

::

    class ConstrainedInt(int):
        def __new__(cls, value):
            value = value % 256
            self = int.__new__(cls, value)
            return self

A reminder of Magic methods:
-----------------------------

Magic Methods

They all start with and end with '__', and do things like support operators and comparisons, and provide handlers for the object lifecycle.

__cmp__(self, other)

__eq__(self, other)

__add__(self, other)

Also, __call__, __str__, __repr__, __sizeof__,
__setattr__, __getattr__, __len__, __iter__,
__contains__, __lshift__, __rshift__, __xor__,
__div__, __enter__, __exit__,

and my personal favorite __rxor__(self,other)......

The list is really long, it's mostly important to get a flavor of how
they are used in Python so you can find and implement the right one when
you need it.

See ``http://www.rafekettler.com/magicmethods.html`` for more

Exercise
---------

Our ConstrainedInt handles initialization for us, but doesn't handle
modification of the value

Develop ConstrainedInt until it passes all tests in
``test_constrained_int.py``

::

    class ConstrainedInt(int):
        """keeps value between 0 and 255"""
        def __new__(cls, value):
            value = value % 256
            self = int.__new__(cls, value)
            return self

