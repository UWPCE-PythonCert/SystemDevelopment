.. _metaclasses:

###########
Metaclasses
###########

adapted from work by Joseph Sheedy

A class is just an object
=========================

.. rst-class:: left

Objects get created from classes. So what is the class of a class?
The class of Class is a metaclass

The metaclass can be used to dynamically create a class

The metaclass, being a class, also has a metaclass


What is a metaclass?
--------------------

-  A class is something that makes instances
-  A metaclass is something that makes classes
-  A metaclass is most commonly used as a class factory
-  metaclasses allow you to do 'extra things' when creating a class,
   like registering the new class with some registry, adding methods
   dynamically, or even replace the class with something else entirely
-  Every object in Python has a metaclass
-  The default metaclass is type()

``type()``
----------

With one argument, ``type()`` returns the type of the argument

With 3 arguments, ``type()`` returns a new class

::

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

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: using type() to build a class
   :name: using-type-to-build-a-class

The ``class`` keyword is syntactic sugar, we can get by without it by
using type

::

    class MyClass(object):
        x = 1

OR

::

    MyClass = type('MyClass', (), {'x': 1})

(``object`` is automatically a superclass)

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Adding methods to a class built with ``type()``
   :name: adding-methods-to-a-class-built-with-type

Just define a function with the correct signature and add it to the attr
dictionary

::

    def my_method(self):
        print "called my_method, x = %s" % self.x

    MyClass = type('MyClass',(), {'x': 1, 'my_method': my_method})
    o = MyClass()
    o.my_method()

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: What type is type?
   :name: what-type-is-type

::

    type(type)
    Out[1]: type

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: \_\_metaclass\_\_
   :name: metaclass__

::

    class Foo(object):
      __metaclass__ = MyMetaClass

Python will look for \_\_metaclass\_\_ in the class definition.

If it finds it, it will use it to create the object class Foo.

If it doesn't, it will use type to create the class.

\_\_metaclass\_\_ can be defined at the module level

Whatever is assigned to \_\_metaclass\_\_ should be a callable with the
same signature as type()

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Why use metaclasses?
   :name: why-use-metaclasses

Useful when creating an API or framework

Whenever you need to manage object creation for one or more classes

For example, see examples/singleton.py

Or consider the Django ORM: ````

::

    class Person(models.Model):
      name = models.CharField(max_length=30)
      age = models.IntegerField()

    person = Person(name='bob', age=35)
    print person.name

When the Person class is created, it is dynamically modified to
integrate with the database configured backend. Thus, different
configurations will lead to different class definitions. This is
abstracted from the user of the Model class.

Here is the Django Model metaclass:
https://github.com/django/django/blob/master/django/db/models/base.py#L59

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Metaclass example
   :name: metaclass-example

Consider wanting a metaclass which mangles all attribute names to
provide uppercase and lower case attributes

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Metaclass example
   :name: metaclass-example-1

::

    class Foo(object):
        __metaclass__ = NameMangler
        x = 1

    f = Foo()
    print f.X
    print f.x

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: NameMangler
   :name: namemangler

::

    class NameMangler(type):
        def __new__(cls, clsname, bases, dct):
            uppercase_attr = {}
            for name, val in dct.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                    uppercase_attr[name] = val
                else:
                    uppercase_attr[name] = val

            return super(NameMangler, cls).__new__(cls, clsname, bases, uppercase_attr)

    class Foo(object):
        __metaclass__ = NameMangler
        x = 1

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Exercise: Working with NameMangler
   :name: exercise-working-with-namemangler

In the repository, find and run examples/mangler.py

Modify the NameMangler metaclass such that setting an attribute f.x also
sets f.xx

Now create a new metaclass, MangledSingleton, composed of the
NameMangler and Singleton classes in the examples/ directory. Assign it
to the \_\_metaclass\_\_ attribute of a new class and verify that it
works.

Your code should look like this:

::

    class MyClass(object):
        __metaclass__ = MangledSingleton # define this
        x = 1

    o1 = MyClass()
    o2 = MyClass()
    print o1.X
    assert id(o1) == id(o2)

.. raw:: html

   </div>

.. raw:: html

   <div class="section slide">

.. rubric:: Reference reading
   :name: reference-reading

`What is a metaclass in
Python? <http://stackoverflow.com/a/6581949/747729>`__

`Python metaclasses by
example <http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example/>`__

`A Primer on Python
Metaclasses <http://jakevdp.github.io/blog/2012/12/01/a-primer-on-python-metaclasses/>`__

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
