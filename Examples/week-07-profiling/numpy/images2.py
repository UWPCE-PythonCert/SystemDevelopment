#!/usr/bin/env python

import sys

import numpy as np
from PIL import Image


image = Image.open(sys.argv[1])
image_array = np.asarray(image)
image_array.setflags(write=True)

# glitch data
image_array -= 100
h,w,channels = image_array.shape

image_array2 = image_array[:,:,:]
# image_array2 = image_array[h:0:-1, w:0:-1, :]

# swap square slices of image
for i in xrange(0, h-20, 20):
    for j in xrange(0, w-20, 20):
        pass
        # slices = image_array2[i+10:i+20, j+10:j+20,:]
        # slices[:,:,0] += 200 
        # image_array2[i:i+10,j:j+10,:] = slices
# Image.fromarray(image_array).save('out.png')
image_array2[:,:,1:3] = (0,0)

Image.fromarray(image_array2).save('out2.png')
