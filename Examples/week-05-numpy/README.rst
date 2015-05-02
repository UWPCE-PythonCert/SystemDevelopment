=====================
Assorted numpy Demos
=====================

This is an assortment of code that demonstrates various aspects of numpy.

iPython notebooks
=================

The *.ipynb files are ipython notebook files. To use them, cd to this directory, and start up ipython::

    $ cd numpy/code
    $ ipython notebook

This should bring up your browser with a page with links to each of the enclosed notebooks.

Other files
============

``start.py`` has a couple utilites used by the other demos

``sudoku-chb.py`` is a suduko game. The GUI is written with wxPython. But the interesting part (in this context) is the game board, which is represented by a numpy array, with each sub part of the board as views on that same array.

