.. _extensions:

===================================
Extending Python with Complied Code
===================================


- Chris Barker

.. Contents:

.. .. toctree::
..    :maxdepth: 2

Topics
=======

.. rst-class:: left

  * Motivation

  * The C API

  * ctypes

  * Cython

  * Auto-generating wrappers

  * Others to consider


Motivation
-----------

Motivations for exiting pure Python

 - Performance
 - Integration with existing C libraries
 - Working as a glue language
 - Implement new builtin types

What is an extension module?

 - written in C (C API)
 - compiled code
 - lets you work directly with the CPython engine

Further reading:

http://docs.python.org/2/extending/extending.html

Example Case
-------------

To focus on the integration techniques, rather than complex C code,
we'll work with the following function we want to integrate::

  #include <stdio.h>

  int add(int x, int y) {
      return x+y;
  }
  int main(void) {
      int w = 3;
      int q = 2;
      printf("%d + %d = %d\n\n", w, q, add(w,q));
  }

This is, of course, trivial and built in to Python, but the techniques
are the same.

(``Examples/week-08-extensions/pure-c/add.c``)


.. nextslide:: Building

Build it with the Makefile (Linux and OS-X)::

  all: add; gcc -o add add.c

::

  $ make
  gcc -o add add.c

and run it::

  $ ./add
  3 + 2 = 5

So are simple function works -- but how to call it from Python?

The C API
---------

Write your function in pure C using the Python API and import it into Python

Good for integrating with C library functions and system calls

The API isn't trivial to learn

Lots of opportunity for error -- you must do manual reference counting:

(http://docs.python.org/2/c-api/refcounting.html)

Further reading:

 - http://docs.python.org/2/extending/extending.html

 - Python 2.7 source code


Intro to the C API
-------------------

You'll need the Python dev package installed on your system

Pull in the Python API to your C code via::

  #include <Python.h>
  /*
  Note: Since Python may define some pre-processor definitions which
  affect the standard headers on some systems, you must include
  Python.h before any standard headers are included.

  stdio.h, string.h, errno.h, and stdlib.h are included for you.
  */

Passing Data in and out of your function
-----------------------------------------

Function arguments must be parsed on the way in and the way out

On the way in, we can call ``PyArg_ParseTuple``::

  if (!PyArg_ParseTuple(args, "s", &var1, ...))
      return NULL;

http://docs.python.org/2/c-api/arg.html#PyArg_ParseTuple

|

On the way out, we can call ``Py_BuildValue``::

  PyObject* Py_BuildValue(const char *format, ...)

http://docs.python.org/2/c-api/arg.html#Py_BuildValue

Registering your functions
---------------------------

First, register the name and address of your function in the method table::

  // Module's method table and initialization function
  static PyMethodDef AddMethods[] = {
      {"add", add, METH_VARARGS, "add two numbers"},
      {NULL, NULL, 0, NULL} // sentinel
  };

https://docs.python.org/2/extending/extending.html#the-module-s-method-table-and-initialization-function


Initializing the module
-----------------------

Define an initialization function::

  PyMODINIT_FUNC // does the right thing on Windows, Linux, etc.
  initadd(void) {
      // Module's initialization function
      // Will be called again if you use Python's reload()
      (void) Py_InitModule("add", AddMethods);
  }

It *must* be called ``initthe_module_name``

https://docs.python.org/2/extending/extending.html#the-module-s-method-table-and-initialization-function

The whole thing:
-----------------

::

  #include <Python.h>

  static PyObject *
  add(PyObject *self, PyObject *args)
  {
      int x, y, sts;

      if (!PyArg_ParseTuple(args, "ii", &x, &y))
          return NULL;
      sts = x+y;
      return Py_BuildValue("i", sts);
  }
  static PyMethodDef AddMethods[] = {
      {"add", add, METH_VARARGS, "add two numbers"},
      {NULL, NULL, 0, NULL} // sentinel
  };
  PyMODINIT_FUNC initadd(void) {
      (void) Py_InitModule("add", AddMethods);
  }

Building your extension
------------------------

``setuptools`` provides features for automatically building extensions::

  from setuptools import setup, Extension
  setup(
      name='Cadd',
      version='1.0',
      description='simple c extension for an example',
      ext_modules=[Extension('add', sources=['add.c'])],
  )

(``distutils`` does too -- but setuptools is getting updated to better
support new stuff)

Run the setup.py::

  python setup.py build_ext --inplace

(you can also just do ``install`` or ``develop`` if you want it properly
installed)


Run the tests
--------------

``test_add.py``::

  import pytest

  import add

  def test_basic():
      assert add.add(3,4) == 7

  def test_negative():
      assert add.add(-12, 5) == -7

  def test_float():
      with pytest.raises(TypeError):
          add.add(3, 4.0)

``$ py.test``



Subtleties we avoided:
======================

There are a LOT of things you need to get right with a hand-written
C Extension.


Exception handling
-------------------

Works somewhat like the Unix errno variable:

* Global indicator (per thread) of the last error that occurred.
* Most functions don’t clear this on success, but will set it to indicate the cause of the error on failure.
* Most functions also return an error indicator:

  - NULL if they are supposed to return a pointer,
  - -1 if they return an integer
  - The PyArg_*() functions return 1 for success and 0 for failure (and they set the Exception for you)

The easy way to set this indicator is with PyErr_SetString

http://docs.python.org/2/c-api/exceptions.html

(you can completely control the Exception handling if you need to)


ReferenceCounting
------------------

Whenever you create or no longer need a Py_Object, you need to increment or decrement the reference count:

``Py_INCREF(x)`` and ``Py_DECREF(x)``

``PyArg_ParseTuple``  and  ``Py_BuildValue``

Handle this for you.

But if you're creating new objects inside your function, you need to keep track.

And what it the function raises an exception in the middle and can't finish?

This gets really ugly and error-prone (and hard to debug!)

LAB
----

LAB 1:

* Add another function to the add.c file that multiplies two numbers instead.
* Write some test code and make sure it works.

LAB 2:

* Find the divide module in the examples/c-api directory
* What happens when you call divide.divide(1/0)?
* This is a different result than a pure Python 1/0, which throws an exception

Advanced:

* Change the divide method to throw an appropriate exception in the
  divide-by-zero case

ctypes
======

Isn't there an easier way to just call some C code?


What is ctypes?
---------------

A foreign function interface in Python

Binds functions in shared libraries to Python functions

Benefits:
 - Ships with Python, since 2.5
 - No new language to learn, it's all Python

Drawbacks:
 - Performance hit for on the fly type translation
 - "thicker" interface in python

Example::

  from ctypes import *
  add = cdll.LoadLibrary("add.so")
  print add.add(3,4)

Further reading:

http://docs.python.org/2/library/ctypes.html


Calling functions with ctypes
------------------------------

The shared lib must be loaded::

    add = ctypes.cdll.LoadLibrary("add.so")

An already loaded lib can be found with::

    libc = ctypes.CDLL("/usr/lib/libc.dylib")

ctypes comes with a utility to help find libs::

    ctypes.util.find_library(name)

(good for system libs)

.. nextslide::

Once loaded, a ctypes wrapper around a c function can be called directly::

    print add.add(3,4)

But....


C is statically typed -- once compiled, the function must be called with
the correct types.

ctypes Data Types
-----------------

ctypes will auto-translate these native types:

  - ``None``
  - int
  - byte strings (``bytes()``, ``str()``)
  - ``unicode`` (careful! unicode is ugly in C!)

These can be directly used as parameters when calling C functions.

.. nextslide::

Most types must be wrapped in a ctypes data type::

    printf("An int %d, a double %f\n", 1234, c_double(3.14))

There are ctypes wrappers for all the "standard" C types

http://docs.python.org/2/library/ctypes.html#fundamental-data-types


You can also do pointers to types::

    a_lib.a_function( ctypes.byref(c_float(x)))

http://docs.python.org/2/library/ctypes.html#passing-pointers-or-passing-parameters-by-reference

.. nextslide:: C structs

You can define C structs::

  >>> class POINT(ctypes.Structure):
  ...     _fields_ = [("x", ctypes.c_int),
  ...                 ("y", ctypes.c_int)]
  ...
  >>> point = POINT(10, 20)
  >>> print point.x, point.y
  10 20
  >>> point = POINT(y=5)
  >>> print point.x, point.y
  0 5

.. nextslide:: Custom Python Classes

You can define how to pass data from your custom classes to ctypes:

Define an ``_as_parameter_`` attribute (or property)::

  class MyObject(object):
      def __init__(self, number):
          self._as_parameter_ = number

  obj = MyObject(32)
  printf("object value: %d\n", obj)

https://docs.python.org/2/library/ctypes.html#calling-functions-with-your-own-custom-data-types

(careful with types here!)

.. nextslide:: Return Types

To define the return type, define the ``restype`` attribute.

Pre-defining the entire function signature::

  libm.pow.restype = ctypes.c_double
  libm.pow.argtypes = [ctypes.c_double, ctypes.c_double]

And you can just call it like a regular python function -- ctypes will type check/convert at run time::

  In [10]: libm.pow('a string', 4)
  ---------------------------------------------------------------------------
  ArgumentError                             Traceback (most recent call last)
  <ipython-input-10-01be690a307b> in <module>()
  ----> 1 libm.pow('a string', 4)

  ArgumentError: argument 1: <type 'exceptions.TypeError'>: wrong type

Some more features
-------------------

Defining callbacks into Python code from C::

    ctypes.CFUNCTYPE(restype, *argtypes, use_errno=False, use_last_error=False)

http://docs.python.org/2/library/ctypes.html#ctypes.CFUNCTYPE

|

Numpy provides utilities for numpy arrays:

http://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.ctypes.html

(works well for C code that takes "classic" C arrays)


Summary:
--------

``ctypes`` allows you to call shared libraries:
  - Your own custom libs
  - System libs
  - Proprietary libs

Supports almost all of C:
 - Custom data types

   - structs
   - unions
   - pointers

 - callbacks

.. nextslide::

* Upside:

  - You can call system libs with little code
  - You don't need to compile anything

    - at least for system and pre-compiled libs

* Downsides:

  - You need to specify the interface

    - and it is NOT checked for you!

  - Translation is done on the fly at run time

    - performance considerations

LAB
----

In ``Examples/week-08-extensions/ctypes`` you'll find ``add.c``

You can build a shared lib with it with ``make``
(``make.bat``) on Windows.

``test_ctypes.py`` will call that dll, and a few system dlls.

* Take a look at what's there, and how it works.

* add another function to add.c, that takes different types (maybe divide?)

* rebuild, and figure out how to call it with ctypes.

* Try calling other system functions with ctypes.


Cython
======

A Python like language with static types which compiles down to C code
for Python extensions.


Cython
-------

* Can write pure python

  - Fully understands the python types

* With careful typing -- you get pure C (and pure C speed)

* Can also call other C code: libraries or compiled in.

* Used for custom Python extensions and/or call C and C++ code.

.. nextslide::

Further reading:

**Web site:**

http://www.cython.org/

**Documentation:**

http://docs.cython.org/

**Wiki:**

https://github.com/cython/cython/wiki



Developing with Cython
----------------------

First, install cython with::

  pip install cython

Cython files end in the .pyx extension. An example add.pyx::

  def add(x, y):
      cdef int result=0
      result = x + y
      return result

(looks a lot like Python, eh?)

.. nextslide::

To build a cython module: write a setup.py that defines the extension::

   from setuptools import setup
   from Cython.Build import cythonize

   setup(name = "cython_example",
         ext_modules = cythonize(['cy_add1.pyx',])
      )

``cythonize`` is a utility that sets up extension module builds for you in a cython-aware way.

Building a module
------------------

For testing, it's helpful to do::

  python setup.py build_ext --inplace

which builds the extensions, and puts the resulting modules right in with the code.

If you have your setup.py set up for a proper package, you can do::

  python setup.py develop
   or
  python setup.py install

Just like for pure-python packages.

.. nextslide::

You can also do only the Cython step by hand at the command line::

  cython a_file.pyx

Produces: ``a_file.c`` file that you can examine, or compile.

For easier reading, you can generate an annotated html version::

  cython -a a_file.pyx

Generates``a_file.html`` html file that is easier to read and gives
additional information that is helpful for debugging and performance
tuning.

More on this later.


Basic Cython
-------------

Cython functions can be declared three ways::

  def foo # callable from Python

  cdef foo # only callable from Cython/C

  cpdef foo # callable from both Cython and Python

Inside those functions, you can write virtually any python code.

But the real magic is with the optional type declarations: the ``cdef`` lines. Well see this as we go...


Calling a C function from Cython
--------------------------------

You need to tell Cython about extenal functions you want to call with ``cdef extern``.

The Cython code::

  # distutils: sources = add.c
  # This tells cythonize that you need that c file.

  # telling cython what the function we want to call looks like.
  cdef extern from "add.h":
      # pull in C add function, renaming to c_add for Cython
      int c_add "add" (int x, int y)

  def add(x, y):
      # now that cython knows about it -- we can just call it.
      return c_add(x, y)

.. nextslide::

and the setup.py::

  from setuptools import setup
  from Cython.Build import cythonize

  setup(name = "cython_example",
        ext_modules = cythonize(['cy_add_c.pyx']  )
        )


.. nextslide::

To build it::

    $ python setup.py build_ext --inplace

and test it::

    Chris$ python test_cy_add_c.py

    if you didn't get an assertion, it worked


A pure Cython solution
----------------------

Here it is as python code::

  def add(x, y):
      result = x + y
      return result

Which we can put in a pyx file and compile with the setup.py::

  #!/usr/bin/env python

  from setuptools import setup
  from Cython.Build import cythonize

  setup(name = "cython_example",
        ext_modules = cythonize(['cy_add1.pyx',
                                 ])
        )

.. nextslide::

and build::

  python setup.py build_ext --inplace

and test::

  Chris$ python test_cy_add1.py

  if you didn't get an assertion, it worked

.. nextslide::

But this is still essentially Python. So let's type define it::

  def add(int x, int y):

      cdef int result=0
      result = x + y

      return result

now Cython knows that ``x, y``, and ``result`` are ``ints``, and can use
raw C for that.

Build and test again::

  Chris$ python setup.py build_ext --inplace

  Chris$ python test_cy_add2.py

If you didn't get an assertion, it worked


A real Example: the Cython process
-----------------------------------

Consider a more expensive function::

  def f(x):
      return x**2-x

  def integrate_f(a, b, N):
      s = 0
      dx = (b-a)/N
      for i in range(N):
          s += f(a+i*dx)
      return s * dx

This is a good candidate for Cython -- an essentially static function called a lot.

Cython from pure Python to C
-----------------------------

Let's go through the steps one by one. In the ``Examples/week-08-extensions/cython/integrate`` directory::


  cy_integrate1.pyx
  cy_integrate2.pyx
  cy_integrate3.pyx
  cy_integrate4.pyx
  cy_integrate5.pyx
  cy_integrate6.pyx
  cy_integrate7.pyx

At each step, we'll time and look at the output from::

  $cython -a cy_integrate1.pyx

AGC Example
-----------

Another useful example of doing something useful, and using a numpy
array is in:

Examples/week-08-extensions/AGC_example

This one impliments an Automatic Gain Control Signal processing filter.

It turns out that you can use some advanced numpy tricks to get pretty
good performancew with this filter, but you can't get full-on speed
without some compiled code.


This example uses all of:
 * Pure Cython
 * C called from Cython
 * f2py and Fortran


Auto-generated wrappers
=======================

There are few ways to auto-generate wrapper for C/C++ code:

SWIG

SIP

XDress

[also Boost-Python -- not really a wrapper generator]

f2py -- for Fortran


SWIG
-----

**Simple Wrapper Interface Generator**

A language agnostic tool for integrating C/C++ code with high level languages

**Advantages:**

 * Code generation for other environments than Python.

 * Doesn't require modification to your C source.

**Disadvantages:**

 * For anything non-trivial, requires substantial effort to develop the interface.

 * Awkward when you want to mix python and C in the interface.

 * Inefficient passing of "Swigified Pointers"


.. nextslide::

Language interfaces:

 * Python

 * Tcl

 * Perl

 * Guile (Scheme/Lisp)

 * Java

 * Ruby

And a bunch of others:

http://www.swig.org/compat.html#SupportedLanguages

Further reading:

http://www.swig.org/Doc1.3/Python.html

SWIGifying add()
----------------

SWIG doesn't require modification to your C source code

The language interface is defined by an "interface file", usually with
a suffix of ``.i``

From there, SWIG can generate interfaces for the languages it supports

The interface file contains ANSI C prototypes and variable declarations

The ``%module`` directive defines the name of the module that will be
created by SWIG

Creating a wrapper:
-------------------

(``Examples/week-08-extensions/swig``)

Create ``add.i``::

  %module add
  %{
  %}
  extern int add(int x, int y);

Create  ``setup.py``::

  from setuptools import setup, Extension

  setup(
      name='add',
      py_modules=['add'],
      ext_modules=[
          Extension('_add', sources=['add.c', 'add.i'])
      ]
  )

.. nextslide::

And build it::

  python setup.py build_ext --inplace

NOTE: distutils (and thus setuptools) "knows" about SWIG, so it does the
swig step for you when you give it a \*.i file.

Notice what gets created:

 * an ``add_wrap.c`` file -- the wrapper code.
 * an ``add.py`` file -- python code that calls the C function
 * an ``_add.so`` (or ``_add.pyd``) file -- the compiled extension

.. nextslide::


You can then run the code::

  python -c 'import add; print add.add(4,5)'

http://www.swig.org/Doc2.0/SWIGDocumentation.html#Introduction_nn5

Installing SWIG
----------------

On the SWIG download page, there is a source tarball for \*nix, and
Windows binaries:

http://www.swig.org/download.html

For Linux:

You may have it in your package repository:

apt-get install swig

If not, download the tarball, unpack it, and::

  ./configure
  make
  sudo make install

should do it.

.. nextslide:: OS-X Install

For OS-X: the same thing, except you also need the "pcre" package.
Which you can get from:

http://sourceforge.net/projects/pcre/files/pcre/8.37/pcre-8.37.tar.gz/download

Put it in the dir created when the SWIG source was unpacked.

Unpack it, then run this to set it up for use with SWIG::

  Tools/pcre-build.sh

Then you can do the standard::

  ./configure
  make
  make install




Decisions, Decisions...
=======================

.. rst-class:: large

  So what to use???


My decision tree
-----------------

Are you calling a few system library calls?

 * Use ctypes

Do you have a really big library to wrap? -- use a wrapper generator:

 * SWIG (other languages?)

 * SIP

 * XDress

Are you writing extensions from scratch?

 * Cython

 * Do you love C++ ?

   - Boost Python

Do you want a "thick" wrapper around a C/C++ lib:

  * Cython

