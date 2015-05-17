#!/usr/bin/env python

import numpy as np
from PIL import Image

image = Image.open('test_image.jpg')
image_array = np.asarray(image)
image_array.setflags(write=True)

# glitch data
image_array -= 200
w,h,channels = image_array.shape

# insert black bands
for x in xrange(0,h,20):
    image_array[:, x:x+5, :] = 0

# swap square slices of image
for i in xrange(0, w-20, 20):
	for j in xrange(0, h-20, 20):
		image_array[i:i+10,j:j+10,:] = image_array[i+10:i+20, j+10:j+20,:]
Image.fromarray(image_array).save('out.png')
