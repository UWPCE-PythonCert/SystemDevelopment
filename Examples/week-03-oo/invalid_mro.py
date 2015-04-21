#!/usr/bin/env python

O = object

class X(O): pass
class Y(O): pass

class A(X,Y): pass
class B(Y,X): pass

class C(A,B): pass
