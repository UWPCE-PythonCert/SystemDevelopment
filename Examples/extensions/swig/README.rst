Simple SWIG Example
===================

This dir has a very, very simple example of using SWIG to generate a
wrapper around a simple C function.

The logic, such as it is, is in the add.i interface file.

To build, siply call:

python ./setup.py build_ext --in_place

distutils understands SWIG, so it will run SWIG for you.

You, of course, need to have SWIG isntalled on your system.

