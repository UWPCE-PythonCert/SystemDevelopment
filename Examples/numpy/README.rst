=====================
Assorted numpy Demos
=====================

This is an assortment of code that demonstrates various aspects of numpy.

Jupyter notebooks
=================

The *.ipynb files are jupyter notebook (formerly known as ipython notebook) files.

To run them, you need the jupyter notebook installed::

    $ python -m pip install -U jupyter


( -U means "upgrade" which should ensure that all the dependecies get upgraded, too)

or, if you are running anaconda:

    $ conda install jupyter

Once jupyter is installed, you can run it:

To use these notebooks, cd to this directory, and start up the notebook::

    $ cd Examples/numpy
    $ jupyter notebook

This should bring up your browser with a page with links to each of the enclosed notebooks.

NOTE: If you have problems like "kernel stopped, trying to restart" you may have a version incompatiblily issue (I did April 24, 2016). There error message ends with somethign like:

File "/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages/ipywidgets/widgets/widget.py", line 154, in Widget in which to find _model_name. If empty, look in the global registry.""").tag(sync=True)

AttributeError: 'Unicode' object has no attribute 'tag'


In that case try::

  python -m pip install -U traitlets

That will update traitlets, which is the source of the problem.

Other files
============

``start.py`` has a couple utilites used by the other demos

``sudoku-chb.py`` is a suduko game. The GUI is written with wxPython. But the interesting part (in this context) is the game board, which is represented by a numpy array, with each sub part of the board as views on that same array.

