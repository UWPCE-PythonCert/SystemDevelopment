.. _packaging:

-------------------------
Building Your Own Package
-------------------------

The very basics of what you need to know to make your own package.

.. toctree::
   :maxdepth: 2

Why Build a Package?
====================

.. rst-class:: left

  There are a bunch of nifty tools that help you build, install and
  distribute packages.

  Using a well structured, standard layout for your package makes it
  easy to use those tools.

  Even if you never want to give anyone else your code, a well
  structured package eases development.

What is a Package?
--------------------

**A collection of modules**

* ... and the documentation

* ... and the tests

* ... and any top-level scripts

* ... and any data files required

* ... and a way to build and install it...

Python packaging tools:
------------------------

The ``distutils``::

    from distutils.core import setup

Getting klunky, hard to extend, maybe destined for deprication...

But it gets the job done -- and it does it well for the simple cases.

``setuptools``: for extra features

``pip``: for installing packages

``wheel``: for binary distributions

Where do I go to figure this out?
-----------------------------------

This is a really good guide:

Python Packaging User Guide:

https://packaging.python.org/en/latest/

**Follow it!**

And a sample project here:

https://github.com/pypa/sampleproject

(this has all the complexity you might need...)


Basic Package Structure:
------------------------

::

    package_name/
        bin/
        CHANGES.txt
        docs/
        LICENSE.txt
        MANIFEST.in
        README.txt
        setup.py
        package_name/
              __init__.py
              module1.py
              module2.py
              test/
                  __init__.py
                  test_module1.py
                  test_module2.py


.. nextslide::

``CHANGES.txt``: log of changes with each release

``LICENSE.txt``: text of the license you choose (do choose one!)

``MANIFEST.in``: description of what non-code files to include

``README.txt``: description of the package -- should be written in reST (for PyPi):

(http://docutils.sourceforge.net/rst.html)

``setup.py``: distutils script for building/installing package.


.. nextslide::

``bin/``: This is where you put top-level scripts

  ( some folks use ``scripts`` )

``docs/``: the documentation

``package_name/``: The main pacakge -- this is where the code goes.

``test/``: your unit tests. Options here:

Put it inside the package -- supports ::

     $ pip install package_name
     >> import package_name.test
     >> package_name.test.runall()

Or keep it at the top level.

The ``setup.py`` File
----------------------

Your ``setup.py`` file is what describes your package, and tells the distutils how to pacakge, build and install it

It is python code, so you can add anything custom you need to it

But in the simple case, it is essentially declarative.


``http://docs.python.org/2/distutils/``


.. nextslide::

::

  from setuptools import setup

  setup(
    name='PackageName',
    version='0.1.0',
    author='An Awesome Coder',
    author_email='aac@example.com',
    packages=['package_name', 'package_name.test'],
    scripts=['bin/script1','bin/script2'],
    url='http://pypi.python.org/pypi/PackageName/',
    license='LICENSE.txt',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.1.1",
        "pytest",
    ],
 )

``setup.cfg``
--------------

``setup.cfg`` provides a way to give the end user some ability to customise the install

It's an ``ini`` style file::

  [command]
  option=value
  ...

simple to read and write.

``command`` is one of the Distutils commands (e.g. build_py, install)

``option`` is one of the options that command supports.

Note that an option spelled ``--foo-bar`` on the command-line is spelled f``foo_bar`` in configuration files.


Running ``setup.py``
---------------------

With a ``setup.py`` script defined, the distutils can do a lot:

* builds a source distribution (defaults to tar file)::

    python setup.py sdist
    python setup.py sdist --format=zip

* builds binary distributions::

    python setup.py bdist_rpm
    python setup.py bdist_wininst

(other, more obscure ones, too....)

But you probably want to use wheel for binary disributions now.

.. nextslide::

* build from source::

    python setup.py build

* and install::

    python setup.py install

setuptools
-----------

``setuptools`` is an extension to ``distutils`` that provides a number of extensions::

    from setuptools import setup

superset of the ``distutils setup``

This buys you a bunch of additional functionality:

  * auto-finding packages
  * better script installation
  * resource (non-code files) management
  * **develop mode**
  * a LOT more

http://pythonhosted.org//setuptools/

wheels
-------

Wheels are a new binary format for packages.

http://wheel.readthedocs.org/en/latest/

Pretty simple, essentially an zip archive of all the stuff that gets put
in

``site-packages``

Can be just pure python or binary with compiled extensions

Compatible with virtualenv.

.. nextslide::

Building a wheel::

  python setup.py bdist_wheel

Create a set of wheels (a wheelhouse)::

	# Build a directory of wheels for pyramid and all its dependencies
	pip wheel --wheel-dir=/tmp/wheelhouse pyramid

	# Install from cached wheels
	pip install --use-wheel --no-index --find-links=/tmp/wheelhouse pyramid

``pip install packagename`` will find wheels for Windows and OS-X.

``pip install --no-use-wheel`` avoids that.

PyPi
-----

The Python package index:

https://pypi.python.org/pypi

You've all used this -- ``pip install`` searches it.

To upload your package to PyPi::

  python setup.py register

  python setup.py sdist bdist_wheel upload


http://docs.python.org/2/distutils/packageindex.html


Under Development
------------------

Develop mode is *really* *really* nice::

  python setup.py develop

It puts links into the python installation to your code, so that your package is installed, but any changes will immediately take effect.

This way all your test code, and client code, etc, can all import your package the usual way.

No ``sys.path`` hacking

Good idea to use it for anything more than a single file project.

(requires ``setuptools``)

Getting Started
----------------

For anything but a single-file script (and maybe even then):

1. Create the basic package structure

2. Write a ``setup.py``

3. ``python setup.py develop``

4. Put some tests in ``package/test``

5. ``py.test`` or ``nosetests``


LAB
-----

* Create a small package

  - package structure

  - ``setup.py``

  - ``python setup.py develop``

  - ``at least one working test``


* If you are ready -- it can be the start of your project package.

(example in ``code/Capitalize``)





