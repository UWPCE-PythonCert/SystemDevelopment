"""
Cython file to call the C routine
"""

import numpy as np
cimport numpy as cnp

cdef extern:
    void AGC(int nAGC, int npts, float *amp, float *ampAGC)


def agc (int nAGC, float[:] amp):
   
   # create the output array
   cdef cnp.ndarray[float, ndim=1] ampAGC = np.zeros_like(amp)
   
   npts = amp.shape[0]

   # call the C function
   AGC(nAGC, npts, &amp[0], &ampAGC[0])

   return ampAGC
