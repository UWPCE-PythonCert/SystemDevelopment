.. _installing_wxpython:

===================
Installing wxPython
===================

As of this writing (Spring 2016), wxPython is in a state of Flux.

This makes it a bit harder to figure out how to get it running.

Hopefully, these notes will help.

Phoenix
=======

.. rst-class:: left

  There are now two versions of wxPython available:

  * "classic"
  * "Phoenix":

  http://wiki.wxpython.org/ProjectPhoenix (information)

  and

  https://github.com/wxWidgets/Phoenix (source)

  "Phoenix" is a refactor of the wxPython code, and currently in a pre-release state.

  But it's the only version that works with py3, and it's pretty solid at this point, at least for the core functionality.

Installing Phoenix
------------------

While not officially released, there are regular "snapshot" builds made available for Windows and OS-X:

http://wxpython.org/Phoenix/snapshot-builds/

These are "binary wheels" -- i.e. complete, ready to install by pip packages

You can either:

Find the one you need (not so easy!), download it, and and then::

  python -m pip install wxPython_Phoenix-3.0.3.dev2022+b85bcd3-cp35-cp35m-macosx_10_6_intel.whl

or:

point pip to that location::

  python -m pip install --no-index --find-links=http://wxpython.org/Phoenix/snapshot-builds/ --trusted-host wxpython.org wxPython_Phoenix

pip should find the one that matches your OS and Python version.

(and yes, it took me a while to figure out all those flags)

Once you've done that (hopefully without errors) you should be able to do::

  import wx

in Python without error.

Linux
-----

There are no pre-built Linux wheels available (there are way too many flavors of Linux to do that). And as it's "preview" version, none of the Linux distros provide packages. So you will need to build from source. The best way to do that is to clone the repo from gitHub, and follow the directions here:

https://github.com/wxWidgets/Phoenix/blob/master/README.rst#how-to-build-phoenix

I don't have a Linux system to test on, so I have no idea how straightforward this is :-(

There was a tutorial posted recently to the wxPython mailing list:

http://wxpython-users.1045709.n5.nabble.com/Problem-when-Installing-wxPython-Phoenix-td5725474.html#a5725492

I've re-posted it here:


How to install wxPython Phoenix on Ubuntu
=========================================

From Damien Ruiz, on the wxpython-users list.

About
-----

Last update : Monday the 21st, January 2016.

This tutorial deals with wxPython Phoenix installation on Ubuntu.

I am using Ubuntu 12.04 LTS - 64 bits.

Note:

Ubuntu 12.04 LTS comes with Python 2.7.3. You might have to make sure
that Python 3 is installed on your computer:

- Type ``python3`` in the console to run the python interpreter.
  You will also see the current version.

If you don't have python3 -- you may need to install it. Here is Ubuntu's Python info page:

https://wiki.ubuntu.com/Python


--- Let's go ---
----------------

1. Install some modules:

    - dpkg-dev
    - build-essential
    - python3.5-dev # use appropriate Python version
    - libwebkitgtk-dev
    - libjpeg-dev
    - libtiff-dev
    - libgtk2.0-dev
    - libsdl1.2-dev
    - libgstreamer-plugins-base0.10-dev
    - libnotify-dev
    - freeglut3
    - freeglut3-dev


2. Go to:

http://wxpython.org/Phoenix/snapshot-builds/ and download the latest .tar.gz

Example: ``wxPython_Phoenix-3.0.3-dev1836+f764b32.tar.gz``

Note:  A .tar.gz file is called a tarball.

3. Untar the tarball::

  tar -xvzf wxPython_Phoenix-3.0.3-dev1836+f764b32.tar.gz


4. Go into the directory::

  cd wxPython_Phoenix-3.0.3-dev1836+f764b32.tar.gz

Note : You can/should use the tab key for auto-completing.

5. Install:

  sudo python setup.py install

Note: Your password will be asked to copy files.


6. Check if the module works :

    6.1 Make sure your current folder is your home folder : type cd

    6.2 Do as follows :

Example::

   damien@Ubuntu1204VB:~$ python
        Python 3.5.4 (default, Jun 22 2015, 19:33:41)
             [GCC 4.6.3] on linux2
        Type "help", "copyright", "credits" or "license" for more information.
        >>> import wx
        >>> wx.version()
        '3.0.3.dev1836+f764b32 gtk2 (phoenix)'

You should then be able to run the examples in:

``Examples/wxpython``

::

  python3 CalculatorDemo.py


Author:

    Damien Ruiz





