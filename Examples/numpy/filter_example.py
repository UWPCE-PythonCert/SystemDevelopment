#!/usr/bin/env python

"""
Example of using stride trick to implement a moving filter
"""

import numpy as np


def convert_2d_window(input, width):
    """
    returns a 2-d array, converted with stride_tricks from the input
    array, to provide a moving window

    The resulting 2-d array is size: (length, width_of_window), so that
    you can do vector math over the window

    :param input: The input array -- should be 1-d
    :width input: the width of the window in number of elements (integer)

    """
    # assure that the input array is as we expect
    input = np.asarray(input).flatten()

    len = input.shape[0]
    itemsize = input.itemsize

    # compute the new shape and strides
    #   final length is the original length minus the window width
    #    -- so we don't drop off the end of the data array
    #   the second dimension is the width of the window
    shape = (len - width + 1, width)

    # The new strides are the item size along the main axis, and also the
    # item size along the cross axis -- so that you gt the next item as the
    # start of the next row.
    strides = (itemsize, itemsize)

    # use as_strided to set up the new shape and strides
    return np.lib.stride_tricks.as_strided(input, shape, strides)


def moving_average(input, width):
    """
    compute the simple moving average of the input series
    """

    expanded = convert_2d_window(input, width)
    avg = expanded.mean(axis=1)

    return avg


def scaled_by_max(input, width):
    """
    compute the time series, scaled by the max of a moving window
    (there is a name for this!)
    """
    expanded = convert_2d_window(input, width)
    max = expanded.max(axis=1)
    filtered = input[:len(expanded)] / max

    return filtered


if __name__ == "__main__":

    # run some examples:
    a = np.arange(25)
    np.random.shuffle(a)

    result = moving_average(a, 3)
    print(result)

    result2 = scaled_by_max(a, 4)
    print(result2)
