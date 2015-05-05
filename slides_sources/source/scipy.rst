.. _scipy:

======================
Intro to Numpy / Scipy
======================

- Chris Barker

.. Contents:

.. .. toctree::
..    :maxdepth: 2


Scipy
=====

.. rst-class:: left

  The scipy "Stack" is a collection of core packages used for scientific / numerical computing.

  http://www.scipy.org/stackspec.html

  Many other domain-specific packages area available:

    Core "stack" is what most people will want, regardless of domain.

What's in the scipy stack?
--------------------------

* Python (http://www.python.org)
* NumPy (http://www.numpy.org)
* SciPy library (http://www.scipy.org)
* Matplotlib (http://matplotlib.org/)
* IPython (http://ipython.org/)

* nose (https://nose.readthedocs.org)
* pandas (http://pandas.pydata.org/)
* Sympy (http://sympy.org/)

Learning Resources
------------------

There are a lot of tutorials, documentation, etc. out there. In this class, we only have a couple hours, so won't get that far. Here are some nice options:

http://scipy-lectures.github.io/

https://github.com/SciTools/courses/blob/master/README.md

https://github.com/jrjohansson/scientific-python-lectures

(note: this one does ``import *`` -- don't do that!)

https://github.com/WeatherGod/AnatomyOfMatplotlib

http://wiki.scipy.org/Tentative_NumPy_Tutorial

For those familiar with MATLAB:

http://wiki.scipy.org/NumPy_for_Matlab_Users


numpy
=====

.. rst-class:: left

  numpy is the core package that the rest of the scipy stack is built on.
  numpy is really the core of everything.

  All the rest requires an understanding good understanding of what a numpy array is -- so that's mostly what I'll talk about here.

So what is numpy?
-----------------

Not just for lots of numbers!
(but it's great for that!)

http://www.numpy.org/


1) An N-Dimensional array object

  - Really this ``ndarray`` is the core of it all

2) A whole pile of tools for operations on/with that object.


Why numpy?
----------

Classic answer: Lots of numbers

  * Faster
  * Less memory
  * More data types

Even if you don't have lot of numbers:

  * N-d array slicing
  * Vector operations
  * Flexible data types


Why numpy?
----------

Wrapper for a block of memory:

  * Interfacing with C libs
  * PyOpenGL
  * GDAL
  * NetCDF4
  * Shapely

Image processing:

  * PIL
  * WxImage
  * ndimage


This Talk
----------

There are a lot of tutorials and documentation out there.

So I'm going to spend about an hour on the regular old "how do you use it" stuff.

Then, I'm going to cover a bit about the guts and some advanced issues.

This is harder to find explanations for -- and will help you understand what's really going on under the hood.

First Tutorial:
---------------

Lets get started by working through the start of what I think is one of the best tutorials:

https://github.com/SciTools/courses/blob/master/README.md

NOTE: this is said to be about a 3-1/2 hour course -- so we're only going to start it...

That is an ipython notebook, which you can download and play around with.

We'll be back after that.....

Getting into the guts of the numpy array
========================================

A few more deatils about what is inside an ndarray

Example code is in the class repo:

``SystemDevelopment2015/Examples/week-05-numpy``

Those are a bunch of ipython notebooks.

Array Constructors:
-------------------

From scratch:
 * ``ones(), zeros(), empty(), arange(), linspace(), logspace()``

 ( Default dtype: ``np.float64`` )

From sequences:
 * ``array(), asarray()`` ( Build from any sequence )

From binary data:
 * ``fromstring(), frombuffer(), fromfile()``

Assorted linear algebra standards:

``eye(), diag()``, etc.

demo: ``constructors.ipynb``


Slicing -- views:
-----------------

a slice is a "view" on the array -- new object, but shares memory:

.. code-block:: ipython

    In [12]: a = np.array((1,2,3,4))
    In [13]: b = a[:]
    # for lists -- [:] means copy -- not for arrays!
    In [15]: a is b
    Out[15]: False
    # it's new array, but...
    In [16]: b[2] = 5
    In [17]: a
    Out[17]: array([1, 2, 5, 4])
    # a and b share data


demo: ``slice.ipynb``


Broadcasting:
-------------

Element-wise operations among two different rank arrays:

Simple case: scalar and array:
::

    In [37]: a
    Out[37]: array([1, 2, 3])
    In [38]: a*3
    Out[38]: array([3, 6, 9])


Great for functions of more than one variable on a grid

demo: ``broadcasting.ipynb``

What is an nd array?
--------------------

  * N-dimensional (up to 32!)
  * Homogeneous array:

    * Every element is the same type
          (but that type can be a pyObject)
    * Int, float, char -- more exotic types

  * "rank" – number of dimensions
  * Strided data:

    * Describes how to index into block of memory
    * PEP 3118 -- Revising the buffer protocol


demo: ``memory_struct.ipynb``


Built-in Data Types
-------------------

  * Signed and unsigned Integers
        8, 16, 32, 64 bits
  * Floating Point
        32, 64, 96, 128 bits (not all platforms)
  * Complex
        64, 128, 192, 256 bits
  * String and unicode
        Static length
  * Bool --  8 bit
  * Python Object
        Really a pointer

demo: ``object.ipynb``

Strides
-------

Core to how numpy works is the stri

Text File I/O
--------------

Loading from text (CSV, etc):

  * ``np.loadtxt``
  * ``np.genfromtxt`` ( a few more features )

Saving as text (CSV):

  * ``np.savetxt()``

Compound dtypes
---------------


  * Can define any combination of other types
        Still Homogeneous:  Array of structs.
  * Can name the fields
  * Can be like a database table
  * Useful for reading binary data


demo: ``dtypes.ipynb``


Numpy Persistence:
------------------

``np.tofile() / np.fromfile()``

 -- Just the raw bytes, no metadata

pickle

``np.savez()``  -- numpy zip format

Compact: binary dump plus metadata

netcdf
  * NetCDF4

Hdf
  * Pyhdf
  * pytables


Working with compiled code
---------------------------

Wrapper around a C pointer to a block of data}

  * Some code can't be vectorized
  * Interface with existing libraries

Tools:

  * C API: you don't want to do that!
  * Cython: typed arrays
  * Ctypes
  * SWIG: numpy.i
  * Boost: boost array
  * f2py

We'll get into this more in a later class...

Example of numpy+cython:

https://github.com/cython/cython/wiki/examples-mandelbrot

Other stuff:
------------

  * Masked arrays
  * Memory-mapped files
  * Set operations: unique, etc
  * Random numbers
  * Polynomials
  * FFT
  * Sorting and searching
  * Linear Algebra
  * Statistics

(And all of scipy, pandas, etc.)

numpy docs:
-----------

www.numpy.org
   -- Numpy reference Downloads, etc

www.scipy.org
   -- lots of docs

Scipy cookbook:

   http://www.scipy.org/Cookbook

"The Numpy Book"

http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf

(old, but written by the primary author -- key stuff in there)

matplotlib
==========

.. rst-class: left
  Matplotlib is the most common plotting library for python.

  * Powerful
  * Flexible
  * Publication quality
  * Primarily 2d graphics (some 3d)

  See the Gallery here:

  http://matplotlib.org/gallery.html

matplotlib APIs
-------------------

Matplotlib has essentially 2 different (but related) APIs:

The "pylab" API:

  * Derived from the MATLAB API, and most suitable for interactive use

The Object Oriented API:

  * reflects the underlying OO structure of matplolib
  * more "pythonic"
  * much better suited to embedding plotting in applications
  * better suited to re-using code

I'll introduce the OO API, but you will see a LOT of example code using the interactive "pylab" interface.

Fortunately, the concepts and most of the commands are the same.

Tutorial
--------

We'll run through a simple tutorial in class.

I suggest you run through amore thourough one to really get an idea how it all works:

https://github.com/WeatherGod/AnatomyOfMatplotlib





