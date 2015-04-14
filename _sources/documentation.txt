.. _documentation:

-------------
Documentation
-------------

A (very) quick run down of how to document your python package.

* Chris Barker


Why
===

.. rst-class:: left

  Documentation is a key part of software development.

  You'll be glad you have it, even if you are the only one that uses your code.

  If you are writing a package you want others to use -- documentation can make all the difference

  And there are some nice tools for documenting Python code.

  There is even a hosting service:

   - http://readthedocs.org


Sphinx
--------

Sphinx is a documentation system build specifically for documenting Python itself:

http://spinx-doc.org

But it's also useful for any sort of structured documentation -- and is sometimes used for non-code projects.

It Produces:
 * HTML (multiple styles available)
 * PDF(via LaTeX)
 * ePub
 * man pages
 * plain text
 * and others!

Extendability
--------------

Sphinx has an extension architecture for adding special functionality:
  * Hieroglyph (It is used for these slides...)

  * Matplotlib added some nice stuff:

   - http://matplotlib.org

  * Math

  * Embedded ASCII art

  * Embedding Excel spreadsheets

  * Unlimited possibilities

Automatic Documentation
------------------------

One of the great features of Sphinx:

It can extract docstrings from your code and build docs from them.

Includes cross referencing of modules and classes, etc.

This keeps your code and docs in sync, and encourages you to have nice docstrings.

It's a bit tricky to get it all set up though :-(

Documentation for the Documentation System
-------------------------------------------

Sphinx is, of course, documented with sphinx itself.


Its tutorial is pretty good, but can be a little confusing (particularly the autodoc stuff)
   - http://sphinx-doc.org/tutorial.html

So here are a couple other resources (and many more out there):

Basic getting started tutorial:
 - https://pythonhosted.org/an_example_pypi_project/sphinx.html

Tutorial focused on getting autodoc set up:
 - http://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/



reStructuredText
-----------------

reStructuredText is the markup language used for Sphinx.

Developed (adapted, really) for Python documentation.

It's a plain text, easy to read and write markup.

Like many similar markup languages (Markdown, etc.)
 * designed to be easy to read and write
 * makes sense in plain text
 * looks a lot like what you might write in plain text anyway.

So it's suitable for use both as plain text and for fancier formatting (i.e. docstrings)

But more extensible than most others -- so good for sphinx


reStructuredText
-----------------

::

	============================
	This is the top level header
	============================

	And now some normal text

	And a level-2 header
	=====================

	more text: **this** is bold.

	And ``this`` is code.

	::

	  #And now a code block
	  for i in range(10):
	      do_something_interesting(i)


reStructuredText documentation sources
---------------------------------------

RST directives::

  .. toctree::
     :maxdepth: 2

``toctree`` is a reStructuredText directive:

Directives can have arguments, options and content

Some docs to get started:

 - http://docutils.sourceforge.net/rst.html

 - http://docutils.sourceforge.net/docs/user/rst/quickstart.html


Sphinx Directives for docstrings
---------------------------------

::

 def a_function(a, b, c='fred'):
     """
     computes something which I would describe here.

     :param a: the first input value
     :type a:  int

     :param b: the second input value
     :type b: float

     :param c='fred': a string flag
     :type c: str

     :returns: a useless string
     """
     return compute_something(a,b,c)

LAB:
----

Set up a Sphinx project to document the package in::

  Examples/Capitalize

Put it in::

  Examples/Capitalize/doc

Set it up to autodoc

Clean up the docstrings so that autodoc works well.

(Or do it for your code!)

Tutorial Script:
-----------------

The following as a script to follow for setting up and starting to document a pacakge with Sphinx and Autodoc.

It uses the ``Capitalize`` package (included in this repo) as an example, but you can follow along with your own package if you like.

First, you need the tool::

  $ pip install sphinx


(Thanks to: http://codeandchaos.wordpress.com/2012/07/30/sphinx-autodoc-tutorial-for-dummies/
)

Setting Up sphinx:
-------------------

You need to be in a good place to build your docs::

  $ cd code/Capitalize/doc

Sphinx comes with a nice utility for getting your documentation set up::

  $ sphinx-quickstart

It will ask you a number of questions on the command line: You can use the defaults for most of these.

You are already in a doc dir, so you can use ``.`` (the default) for the root path::

  > Root path for the documentation [.]:

QuickStart (cont):
-------------------

I like to keep the source can built docs separate::

  > Separate source and build directories (y/N) [n]: y

Give it a name and an author::

  > Project name: Capitalize
  > Author name(s): Chris Barker

Use ``.rst`` for restructured text::

  > Source file suffix [.rst]:

QuickStart (cont):
-------------------

You absolutely want autodoc!::

  > autodoc: automatically insert docstrings from modules (y/N) [n]: y


This is kind of nice, to help you keep in line::

  > coverage: checks for documentation coverage (y/N) [n]: y

A Makefile (and/or DOS batch file) is really handy::

  > Create Makefile? (Y/n) [y]: y
  > Create Windows command file? (Y/n) [y]: y

Project Structure:
-------------------

``sphinx-quickstart`` will have created the project structure for you::

  $ ls
  Makefile   README.txt build      make.bat   source

  $ ls source
  _static    _templates conf.py    index.rst

``index.rst`` is the start of your documentation

``conf.py`` is the configuration that was created by ``sphinx-quickstart`` -- you can edit it if you change you mind about anything.


Building the docs:
-------------------

The ``Makefile`` will build the docs for you in various ways::

  $ make html
  sphinx-build -b html -d build/doctrees   source build/html
  Making output directory...
  Running Sphinx v1.1.3
   ....
  Build finished. The HTML pages are in build/html.

Or::

  $ make latexpdf

(if you have LaTeX installed...)

Take a look at ``build/html/index.html``


Getting Started with Writing:
------------------------------

The ``index.rst`` file will look like this::

  Welcome to Capitalize's documentation!
  ======================================

  Contents:

  .. toctree::
     :maxdepth: 2

  Indices and tables
  ==================

  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`



A tiny bit of RST
-----------------

Underlining creates headings::

    Welcome to Capitalize's documentation!
    ======================================

This will give you a lower level heading::

    Welcome to a Subsection
    ------------------------

(each new underlining character you introduce goes another level down.)

A tiny bit of RST
------------------

The ``..`` is either a comment or a "directive"::

  .. toctree::
     :maxdepth: 2

if sphinx understand the directive ``toctree``, then it is used. Otherwise, it is treated as a comment.

``toctree`` builds a table of contents tree.

AutoDoc
--------

AutoDoc extracts the docstrings from your code.

In order to find them -- sphinx needs to be able to import the code.

Another reason to build a package and use ``develop`` mode!

Alternatively, you can add the path to your code by adding this to the conf.py file::

  os.path.abspath('mydir/myfile.txt')

(Path is relative to the conf.py file)

But I'm not going to do that, 'cause I use ``develop`` mode

Adding Autodoc to your docs.
----------------------------

Add the automodule directive to your ``index.rst`` file::

  The Capitalize Package
  -----------------------

  .. automodule:: capitalize

Then rebuild::

  $ make html

And reload ``index.rst``

Finding the members.
---------------------

Not much there, is there? Where is the capital_mod module?

Sphinx only creates the main doc for each package.

You need to create a entry for each module yourself::

  capital_mod
  ............

  .. automodule:: capitalize.capital_mod
     :members:

The ``:members:`` directive tells Sphinx you want all the members documented as well.

Documenting the members.
-------------------------

You can specify only particular ones if you want::

  .. automodule:: capitalize.capital_mod
     :members: capitalize

For classes, there is ``autoclass``::

  .. autoclass:: a_package.a_class
     :members:

You may want to set ``autoclass_content`` configuration to one of: "class",
"init", or "both"

(http://sphinx-doc.org/ext/autodoc.html)


Multiple Files
---------------

For most projects, you'll want multiple pages in your docs. You can put each in their own `*.rst` file, and reference them in the ``toctree`` section::

  .. toctree::
     :maxdepth: 2

     installation.rst
     tutorial.rst
     api.rst

Then you need to create and populate those files - make sure they have a header!

I put the autocdoc stuff in the api.rst file...

APIdoc
-------

For a substantial package, hand writing all those files and autodoc directives can get pretty tedious.

So you can use APIdoc::

  sphinx-apidoc [options] -o <outputdir> <sourcedir> [pathnames ...]

  $ sphinx-apidoc -o test ../capitalize
  Creating file test/capitalize.rst.
  Creating file test/capitalize.test.rst.
  Creating file test/modules.rst.

This is actually pretty slick....


Sphinx Appearance
-------------------

If you don't like the default looks, there are a number of other options, or you can build your own:

http://sphinx-doc.org/theming.html

In ``conf.py``::

 html_theme = "default"


Of course, this is the primary source of how to use Sphinx itself:

http://sphinx-doc.org/
