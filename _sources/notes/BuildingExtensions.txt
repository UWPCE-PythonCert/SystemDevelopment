.. _building_extensions:

==============================
Building Extensions to Python
==============================

To build extensions to Python, you need a C (and maybe C++) compiler that is compatible with your Python build.

Linux
======

Linux is pretty straightforward -- most systems are set up to build stuff out of the box. If not, you'll need to install the development tools. In Ubuntu, that's::

   sudo apt-get install build-essential

Other systems will have something similar.

To make sure it's working, you can make sure gcc is there with::

  gcc --version

at the command line, and make sure you get something!

To compile Python extensions, you'll need the some extra files that come with python. Most distros have an extra package, called something like "python-dev" that you'll need to get the headers, etc. required to build extensions::

  apt-get install python-dev

That should do it.

Windows:
========

The easiest way is to use the same MS compiler as the ``python.org`` build.

With Python2.7, that's MS Visual Studio 2008.

MS has recently started distributing a version of the compiler set up specifically to build Python extensions:

http://www.microsoft.com/en-us/download/details.aspx?id=44266

The trick is that this installs things a bit differently than distutils expects. But newer versions of setuptools do support it. So make sure you have an updated setuptools::

  pip install --upgrade setuptools

and that the extension you are trying to compile is using setuptools, rather than raw distutils.

OS-X:
=====

Apple moves fast with its upgrades, so it's a bit of a trick. The latest version of XCode is free, but does not support older systems, and thus won't work (at least not easily) for the python.org python builds.

python.org python
------------------

For python.org Python2.7, you need XCode 4.* (I've got 4.6.3)

for Lion (10.7 and above) -- you'll need to download it. Apple makes it a bit hard to find the older versions, but they can be found at:

[developer.apple.com](https://developer.apple.com/downloads)

You need to login with an AppleID (or create one), then select "Developer Tools", and search for Xcode -- poke around a bit, and you'll eventually find:

XCode 4.6.3

Download and install it (do it with a fast connection -- it's huge)

After installing it, you may need to install the "command line tools". Select preferences, the Downloads, and install the "Command Line Tools" if they are not already installed.

Apple's Python
---------------

For Apple's built-in python, you should be able to use the latest XCode for your system (should!). You can get it from the App Store (the App store only has the latest, as far as I know). After installing it, make sure you got the command line tools:

To install these tools, go to the Downloads tab within the Xcode Preferences menu and click "Install" next to the Command Line Tools entry.

(https://developer.apple.com/support/xcode/)

Macports / Homebrew
--------------------

If you installed python with Macports or Homebrew, it should be all set up to compile extensions. If not, then you may need to install a python-dev package, or something like that.

Testing if it works:
======================

In the code dir for the week-08 class, you'll find a number of samples.

Go to the: ``week-08/extensions/code/c-api`` dir.

type::

   python setup.py build_ext --inplace

This should spew out a bunch of stuff while it builds the extension, then hopefully finish without an error. On Linux and the Mac, you should get an add.so file, on Windows, an add.pyd file.

Try::

    py.test

and hopefully 3 tests will pass.



