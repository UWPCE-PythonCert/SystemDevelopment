#!/usr/bin/env python

"""
test code for the "agc_subroutine" extension, generated from fortran by f2py
"""
import numpy as np
import matplotlib.pyplot as plt

import agc_subroutine
import agc_python

print "the doctring for agc:"
print agc_subroutine.agc.__doc__

# to call it:
# create a noisy array:

t = np.linspace(0,20,100).astype(np.float32)

signal = np.sin(t)

# add some noise
signal += (np.random.random(signal.shape)-0.5) * 0.3

# create an array for the result:
#filtered = np.zeros_like(signal)

# run it through the AGC filter:
filtered = agc_subroutine.agc(10, signal)

# try the python version
filtered2 = agc_python.agc(10, signal)

if np.allclose(filtered2, filtered2):
	print "the same"
else:
	print "not the same"

## plot the results

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(1,1,1)
ax.plot(t, signal, t, filtered, t, filtered2)

plt.show()




