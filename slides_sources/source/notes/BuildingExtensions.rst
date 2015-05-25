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

Apple provides a free compiler, as part of the "XCode" IDE.
You can get it for free from the App store, but be prepared, it is a big download!

Just the command line tools:


It looks like you can just get the command line tools by running this command on the command line::

    xcode-select --install

see: http://osxdaily.com/2014/02/12/install-command-line-tools-mac-os-x/

for more detail.

If you opt for the full package, after you install XCode, you STILL need to install the command line tools. To install these tools, go to the Downloads tab within the Xcode Preferences menu and click "Install" next to the Command Line Tools entry.

(https://developer.apple.com/support/xcode/)

Macports / Homebrew
--------------------

If you installed python with Macports or Homebrew, it should be all set up to compile extensions. If not, then you may need to install a python-dev package, or something like that.

Testing if it works:
======================

In the ``Examples\week-08 class``, you'll find a number of samples.

Go to the: ``Examples\week-08-extensions/c-api`` dir.

type::

   python setup.py build_ext --inplace

This should spew out a bunch of stuff while it builds the extension, then hopefully finish without an error. On Linux and the Mac, you should get an add.so file, on Windows, an add.pyd file.

Try::

    py.test

and hopefully 3 tests will pass.

