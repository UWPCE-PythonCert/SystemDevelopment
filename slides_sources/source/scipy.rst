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

The ipython "notebook"
-----------------------

We've been using iPython a lot in this class (at least I have)

It provides a great interactive environment fo testing and running
Python code.

It turns out it has antoher interface: the "notebook"

The notebook provides a way to interspese littel chunks of code, adn text, adn images, etc...

It runs in a browser, you start it up with:

.. code-block:: bash

  ipython notebook

It should start your browser, and show you the notebooks in the dir you started it up in.

I'll be using it for lots of demos in this class.


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

So I'm going to spend about an hour or so on the regular old "how do you use it" stuff.

Then, I'm going to cover a bit about the guts and some advanced issues.

This is harder to find explanations for -- and will help you understand what's really going on under the hood.

NOTE: I've been using numpy and its predecessors for long time -- so have kind of forgotten what is obvious and what is not -- so:

 **ask questions**

 as we go!

Getting started
================

.. rst-class:: left

  Example code is in the class repo:

  ``SystemDevelopment2015/Examples/week-05-numpy``

  Those are a bunch of ipython notebooks.

  Get your command line into that dir, then start up the iPyhton notebook:

  ``$ ipython notebook``

  This should fie up your browser, and give you a list of notebooks to choose from.

Array Constructors:
-------------------

How do you make an array?

From scratch: ``ones(), zeros(), empty(), arange(), linspace(), logspace()``

( Default dtype: ``np.float64`` )

From sequences:  ``array(), asarray()`` ( Build from any sequence )

From binary data:  ``fromstring(), frombuffer(), fromfile()``

Assorted linear algebra standards: ``eye(), diag()``, etc.

demo: ``constructors.ipynb``


Indexing and slicing
--------------------

How do you get parts of the array out?

Indexing and slicing much like regular python sequences, but extended to multi-dimensions.

However: a slice is a "view" on the array -- new object, but shares memory:

demo: ``slice.ipynb``


Reshaping:
-----------

numpy arrays have a particular shape.

But they are really wrappers around a block of data

So they can be re-shaped -- same data, arranged differently

demo: ``reshaping.ipynb``


Broadcasting:
-------------

Element-wise operations among two different rank arrays:

This is the key power of numpy!

Simple case: scalar and array:
::

    In [37]: a
    Out[37]: array([1, 2, 3])
    In [38]: a*3
    Out[38]: array([3, 6, 9])


Great for functions of more than one variable on a grid

demo: ``broadcasting.ipynb``

Fancy Indexing
--------------

As we've seen, you can slice and dice nd arrays much like regular python sequences.

This model is extended to multiple dimensions.

But it still only lets you extract rectangular blocks of elements.

For more complex sub-selection: we use "fancy indexing":

demo: ``fancy_indexing.ipynb``


What is an nd array under the hood?
-----------------------------------

 * N-dimensional (up to 32!)

 * Homogeneous array:

   - Every element is the same type

     (but that type can be a pyObject)

   - Int, float, char -- more exotic types

   - "rank" – number of dimensions

 * Strided data:

   - Describes how to index into block of memory

   - PEP 3118 -- Revising the buffer protocol


demo: ``memory_struct.ipynb``


Built-in Data Types
-------------------

* Signed and unsigned Integers

  - 8, 16, 32, 64 bits

* Floating Point

  - 32, 64, 96, 128 bits (not all platforms)

* Complex

  - 64, 128, 192, 256 bits

* String and unicode

  - Static length

* Bool --  8 bit

* Python Object

  - Really a pointer

demo: ``object.ipynb``


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

    - Still Homogeneous:  Array of structs.
  * Can name the fields

  * Can be like a database table

  * Useful for reading binary data


demo: ``dtypes.ipynb``


Numpy Persistence:
------------------

  * ``np.tofile() / np.fromfile()``

    - Just the raw bytes, no metadata

  *  ``pickle``

  * ``np.savez()``  -- numpy zip format

    - Compact: binary dump plus metadata

  * netcdf

    - NetCDF4 (https://github.com/Unidata/netcdf4-python)

  * Hdf

    - Pyhdf

    - pytables


Stride Tricks
--------------

numpy arrays are really wrappers about "strided data"

This means that there is a single linear block of memory with the
values in it.

The "strides" describe how that data is arranged to look like an array of more dimensions: 2D, 3D, 4D etc.

Mostly, numpy handles all this under the hood for you, so you can logically work with the data as though it were multi-dimensional.

But you can actually manipulate the description of the data, so that it "acts" like it is arranged differently than it is:

``stride_tricks.ipynb``


Working with compiled code
---------------------------

  * Some code can't be vectorized
  * Interface with existing libraries

numpy arrays are essentially a wrapper around a C pointer to a block of data -- some tools:

  * C API: you don't want to do that!
  * Cython: typed arrays
  * Ctypes
  * SWIG: numpy.i
  * Boost: boost array
  * f2py

We'll get into this more in a later class...

Example of numpy+cython: https://github.com/cython/cython/wiki/examples-mandelbrot

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

numpy docs:
-----------

www.numpy.org

  - Numpy reference Downloads, etc

www.scipy.org

  - lots of docs

Scipy cookbook:

  - http://www.scipy.org/Cookbook

"The Numpy Book"

http://csc.ucdavis.edu/~chaos/courses/nlp/Software/NumPyBook.pdf

(old, but written by the primary author -- key stuff in there)

matplotlib
==========

.. rst-class:: left

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

We'll run through a simple tutorial in class:

``SystemDevelopment2015/Examples/week-05-matplotlib``

There are "learner" and instructor notebooks in there. They are identical, but if you use the learner one you can mess with it and not mess up the main one...

If you really want to use MPL, I suggest you run through a more thorough one to really get an idea how it all works:

https://github.com/WeatherGod/AnatomyOfMatplotlib

This one is pretty nice -- but would take the entire class...

Using numpy arrays when computation isn't critical
--------------------------------------------------

numpy arrays are mostly about performance and memory use.

But you still may want to use them for toher reasons.

some data naturally is in 2-d or 3-d arrays.

sometimes you need to work on a sub-view of the data as an independent object.

For example: A Sudoko game:

 * The board is 9X9
 * Sub-divided into 3X3 squares
 * And you need to examine the rows and columns

Example: ``sudoku-chb.py``


Pandas
=======

.. rst-class:: left

  Python Data Analysis Library

  Pandas provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

  Modeled after R's dataframe concept, it provides some pretty neat tools for doing simple statistical analysis and plotting of larg-ish data sets.

  It's particularly powerful for time series.

  ``http://pandas.pydata.org/``

Learning Pandas
----------------

The official documentation is excellent, including tutorials:

http://pandas.pydata.org/pandas-docs/stable/

http://pandas.pydata.org/pandas-docs/stable/10min.html

http://pandas.pydata.org/pandas-docs/stable/tutorials.html

In addition, there are a large number of tutorials on the web:

This one is oriented to folks familiar with SQL:

http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/

And this is a good one to get started quick:

http://synesthesiam.com/posts/an-introduction-to-pandas.html

We'll give that one a shot in class now...

Scipy
=====

.. rst-class:: left

  The scipy package itself is a large collection of cool stuff for scientific computing. ( http://docs.scipy.org/doc/scipy/reference/ )

  You'll see there lots of stuff! If it's at all general purpose for computation, you're likely to find it there.

  Some of the most common sub-packages:

   * Special functions (scipy.special)
   * Integration (scipy.integrate)
   * Optimization (scipy.optimize)
   * Interpolation (scipy.interpolate)
   * Fourier Transforms (scipy.fftpack)
   * Signal Processing (scipy.signal)
   * Linear Algebra (scipy.linalg)
   * Spatial data structures and algorithms (scipy.spatial)
   * Statistics (scipy.stats)
   * Multidimensional image processing (scipy.ndimage)






