.. _metaclasses:

###########
Metaclasses
###########

adapted from work by Joseph Sheedy

A class is just an object
=========================

.. rst-class:: left

  A class is a first-class object:

  Can be created at runtime

  Passed as a parameter

  Returned from a function

  Assigned to a variable


Example
-------

::

   >>> def create_a_class(**kw):
   ...    return type('CoolClass', (object,), dict(**kw))
   ...
   >>> cool_class = create_a_class(foo='nice', bar='sweet')
   >>> cool_class
   <class '__main__.CoolClass'>
   >>> cool_object = cool_class()
   >>> cool_object
   <__main__.CoolClass object at 0x10224e208>
   >>> cool_object.foo
   'nice'
   >>> cool_object.bar
   'sweet'


Equivalent to:
--------------


::

   class CoolClass(object):
      foo = 'nice'
      bar = 'sweet'


But it was created at runtime, returned from a function and assigned to a variable.


http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example


More on Classes
---------------

  Objects get created from classes. So what is the class of a class?

  The class of Class is a metaclass

  The metaclass can be used to dynamically create a class

  The metaclass, being a class, also has a metaclass


What is a metaclass?
--------------------

-  A class is something that makes instances
-  A metaclass is something that makes classes
-  A metaclass is most commonly used as a class factory
-  Metaclasses allow you to do 'extra things' when creating a class,
   like registering the new class with some registry, adding methods
   dynamically, or even replace the class with something else entirely
-  Every object in Python has a metaclass
-  The default metaclass is ``type()``


``type()``
----------

With one argument, ``type()`` returns the type of the argument

With 3 arguments, ``type()`` returns a new class

.. code-block:: ipython

    type?
    Type:       type
    String Form: <type 'type'>
    Namespace:  Python builtin
    Docstring:
    type(object) -> the object's type
    type(name, bases, dict) -> a new type

    name: string name of the class
    bases: tuple of the parent classes
    dict: dict containing attribute names and values


using type() to build a class
-----------------------------

The ``class`` keyword is syntactic sugar, we can get by without it by
using type

.. code-block:: python

    class MyClass(object):
        x = 1

or

.. code-block:: python

    MyClass = type('MyClass', (), {'x': 1})

(``object`` is automatically a superclass)


Adding methods to a class built with ``type()``
-----------------------------------------------

Just define a function with the correct signature and add it to the attr
dictionary

.. code-block:: python

    def my_method(self):
        print("called my_method, x = %s" % self.x)

    MyClass = type('MyClass',(), {'x': 1, 'my_method': my_method})
    o = MyClass()
    o.my_method()


MyClass = type(name, bases, dct)

-  name: name of newly created class
-  bases: tuple of class's base classes
-  dct: class attribute mapping


What type is type?
------------------

.. code-block:: ipython

  In [30]: type(type)
  Out[30]: type


``metaclass``
---------------

Setting a class' metaclass:

.. code-block:: python

  class Foo(metaclass=MyMetaClass):
      pass


the class assigned to the ``metaclass`` keyword argument will be used to create the object class ``Foo``.

If the ``metaclass`` kwarg is not defined, it will use type to create the class.

Whatever is assigned to ``metaclass`` should be a callable with the
same signature as type()

**Python2 NOTE:**

In Python 2, instead of the keyword argument, a special class attribute: ``__metaclass__`` is used:

.. code-block:: python

    class Foo(object):
      __metaclass__ = MyMetaClass


Why use metaclasses?
--------------------

Useful when creating an API or framework

Whenever you need to manage object creation for one or more classes

For example, see ``Examples/metclasses/singleton.py``

Or consider the Django ORM:

.. code-block:: python

  class Person(models.Model):
      name = models.CharField(max_length=30)
      age = models.IntegerField()

  person = Person(name='bob', age=35)
  print person.name

When the Person class is created, it is dynamically modified to
integrate with the database configured backend. Thus, different
configurations will lead to different class definitions. This is
abstracted from the user of the Model class.

.. nextslide::

Here is the Django Model metaclass:

https://github.com/django/django/blob/master/django/db/models/base.py#L77


__new__  vs  __init__ in Metaclasses
------------------------------------


``__new__`` is used when you want to control the creation of the class (object)

``__init__`` is used when you want to control the initiation of the class (object)

``__new__`` and ``__init__`` are both called when the module containing the class is imported for the first time.

``__call__`` is used when you want to control how a class (object) is called (instantiation)


.. nextslide::


..code-block:: python

   class CoolMeta(type):
       def __new__(meta, name, bases, dct):
           print('Creating class', name)
           return super(CoolMeta, meta).__new__(meta, name, bases, dct)
       def __init__(cls, name, bases, dct):
     print('Initializing class', name)
     super(CoolMeta, cls).__init__(name, bases, dct)
       def __call__(cls, *args, **kw):
           print('Meta has been called')
     return type(cls, *args, **kw)

   class CoolClass(metaclass=CoolMeta):
       def __init__(self):
           print('And now my CoolClass exists')

   print('Actually instantiating now')
   foo = CoolClass()


Metaclass example
-----------------

Consider wanting a metaclass which mangles all attribute names to
provide uppercase and lower case attributes

.. code-block:: python

    class Foo(metaclass=NameMangler):
        x = 1

    f = Foo()
    print(f.X)
    print(f.x)


NameMangler
-----------

.. code-block:: python

  class NameMangler(type):

      def __new__(cls, clsname, bases, _dict):
          uppercase_attr = {}
          for name, val in _dict.items():
              if not name.startswith('__'):
                  uppercase_attr[name.upper()] = val
                  uppercase_attr[name] = val
              else:
                  uppercase_attr[name] = val

          return super().__new__(cls, clsname, bases, uppercase_attr)


  class Foo(metaclass=NameMangler):
      x = 1


Exercise: Working with NameMangler
----------------------------------

In the repository, find and run ``Examples/metaclasses/mangler.py``

Modify the NameMangler metaclass such that setting an attribute f.x also
sets f.xx

Now create a new metaclass, MangledSingleton, composed of the
NameMangler and Singleton classes in the ``Examples/metaclasses`` directory.

Assign it to the ``metaclass`` keyword argument of a new class and verify that it works.

Your code should look like this:

.. code-block:: python

    class MyClass(metaclass=MangledSingleton) # define this
        x = 1

    o1 = MyClass()
    o2 = MyClass()
    print(o1.X)
    assert id(o1) == id(o2)


The Singleton
-------------

One common use of metaclasses is to create a singleton. There is an example of this called singleton.py in the Examples directory. However, metaclasses are not the only way to create a singleton. It really depends on what you are trying to do with your singleton.


http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html

http://stackoverflow.com/questions/6760685/creating-a-singleton-in-python


Reference reading
-----------------

About metaclasses (Python 3):

.. rst-class:: small

  http://blog.thedigitalcatonline.com/blog/2014/09/01/python-3-oop-part-5-metaclasses

Python 2 (mostly the same):

What is a metaclass in Python?

.. rst-class:: small

  http://stackoverflow.com/a/6581949/747729

Python metaclasses by example:

.. rst-class:: small

  http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/

A Primer on Python Metaclasses:

.. rst-class:: small

  http://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/

And some even more advanced tricks:

.. rst-class:: small

  http://blog.thedigitalcatonline.com/blog/2014/10/14/decorators-and-metaclasses


