.. _installing_scipy:

==========================
Installing The SciPy Stack
==========================

There are lot of notes online about this, but this is summary of my recommendations.

To build extensions to Python, you need a C (and maybe C++) compiler that is compatible with your Python build.

Scipy
=====

"SciPy" is really two things:

1) A particular package of modules useful for computational/scientific computing: what you get when you do::

.. code-block:: python

   import scipy

2) A community of folks doing scientific computing, and all the packages that are developed and used -- ** A LOT**

But there are a few packages that what most people will want, regardless of domain. To help calrify all this the "scipy stack" was officially declared:

http://www.scipy.org/stackspec.html

What's in the scipy stack?
--------------------------

* Python (http://www.python.org)
* NumPy (http://www.numpy.org)
* SciPy library (http://www.scipy.org)
* Matplotlib (http://matplotlib.org/)
* IPython (http://ipython.org/)
* pandas (http://pandas.pydata.org/)

* nose (https://nose.readthedocs.org) (for testing)
* Sympy (http://sympy.org/) (symbolic algebra)

Installing the Stack
---------------------

Many of these packages are compiled code, some of it in Fortran -- so it can be quite a pain to install from source. There are a number of ways to find pre-complied packages, some of which are outlined here:

http://www.scipy.org/install.html

But here are my thoughts:

* If you are doing a lot of scientific computing, and not much else:

  - Install the Anaconda distribution, and use it to install the other packages you'll need:

  https://store.continuum.io/cshop/anaconda/

  There are free versions for Windows, Linux and OS-X.

If you want to just add numpy, etc. to the python.org install

* Windows and OS-X:

  - try ``pip install``: I _think_ that there are binaries up on pypi for Windows and OS-X. So

::

  pip install numpy
  pip install scipy
  pip install ipython[all]
  pip install pandas

* Windows:

Another good option is Chris Gohlke's packages, which you can find here:

http://www.lfd.uci.edu/~gohlke/pythonlibs/

These are binary wheels, so once downloaded, they can be installed with pip::

  pip install numpy‑1.9.2+mkl‑cp26‑none‑win_amd64.whl

Note that he has both 32 bit and 64 bit packages there, install the ones that match your python. Despite the name, the "amd64" packages will work with Intel processors, too.


* Linux

These may be available from your system package manager (yum, apt-get) -- try that first. If not, then you'll need the compilers set up right, which may require some additional system packages first.

Checking if it works:
---------------------

Once installed, you should be able do the following imports::

  import numpy
  import scipy
  import matplotlib
  import pandas

And be able to run the ipython notebook from the command line::

  $ ipython notebook

(that should start up your browser, pointed back at the notebook running in the dir you started it up in)













