#!/usr/bin/env python

"""
cython version version of the Automatic Gain Control function

Timings:
  first version (pure python):

In [23]: timeit agc_cython.agc(10, np.arange(1000, dtype=np.float32))
100 loops, best of 3: 10.7 ms per loop

typing inputs:

100 loops, best of 3: 17.3 ms per loop

Typing counters and memoryviews of arrays
1000 loops, best of 3: 1.68 ms per loop

typing loop counters
1000 loops, best of 3: 613 us per loop

forgot to type fmax:
10000 loops, best of 3: 119 us per loop

added boundscheck=False
10000 loops, best of 3: 117 us per loop

use memoryviews of cython arrays
10000 loops, best of 3: 39.4 us per loop

use cython arrays:
100 loops, best of 3: 6.12 ms per loop

c array for temp array:
100 loops, best of 3: 6.34 ms per loop

"""

import cython
import numpy as np
cimport numpy as cnp

#from libc.stdlib cimport malloc, free

@cython.boundscheck(False)
@cython.cdivision(True) 
def agc( int nAGC, cnp.ndarray[float, ndim=1, mode='c'] amp):
   """
   run an automatic gain control filter onver the input array

   :param nAGC: width of window, number of elements.
   :type nAGC: integer

   :param amp: input amplitude data
   :type amp: 1-d numpy array of float32
   
   :returns ampAGC: a numpy array of the filtered data.

   """

   cdef float fmax
   cdef unsigned int i, j

   cdef unsigned int npts = amp.shape[0]

   cdef unsigned int nAGC2 = nAGC / 2

   cdef cnp.ndarray[float, ndim=1, mode='c'] ampAGC = np.zeros_like(amp)
   cdef cnp.ndarray[float, ndim=1, mode='c'] absamp = np.abs(amp)


   for i in range(nAGC2, npts - nAGC2):
      fmax=0.0
      for j in range(i-nAGC2,i+nAGC2+1):
            if absamp[j] > fmax:
                fmax = absamp[j]
      ampAGC[i] = amp[i]/fmax
   
   return ampAGC

