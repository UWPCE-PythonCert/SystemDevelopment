#!/usr/bin/env python

"""
Pure python (and not very numpy smart) version of the
Automatic Gain Control function
"""

import numpy as np


def agc(nAGC, amp):
    """
    run an automatic gain control filter onver the input array

    :param nAGC: width of window, number of elements.
    :type nAGC: integer

    :param amp: input amplitude data
    :type amp: 1-d numpy array of float32

    :returns ampAGC: a numpy array of the filtered data.

    """

    # make sure input array is as expected:
    amp = np.asarray(amp, dtype=np.float32)

    if len(amp.shape) != 1:
        raise ValueError("amp must be a rank-1 array")

    npts = amp.shape[0]

    nAGC2 = nAGC / 2
    ampAGC = np.zeros_like(amp)
    absamp = np.zeros_like(amp)

    absamp = np.abs(amp)

    for i in xrange(nAGC2, npts - nAGC2):
        fmax = 0.0
        for j in range(i - nAGC2, i + nAGC2 + 1):
            if absamp[j] > fmax:
                fmax = absamp[j]
        ampAGC[i] = amp[i] / fmax

    return ampAGC
