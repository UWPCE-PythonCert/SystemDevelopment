#!/usr/bin/env python

import numpy as np
from PIL import Image

image = Image.open('test_image.jpg')
image_array = np.asarray(image)
image_array.setflags(write=True)

h,w,channels = image_array.shape

# zeros = np.zeros((h,w,3), dtype=np.uint8)

# zeros[:,0:-150,:] = image_array[:, 150:w, :]

zeros = image_array[:,150:,:]

for j in xrange(0, w-150-20,20 ):
    for i in xrange(0, h-20, 20):
        slice = zeros[i+10:i+20, j+10:j+20,:]
        slice[:,:,0] = 255
        # zeros[i:i+10,j:j+10,:] = slice[:,:
        # image_array[i:i+10,j:j+10,:] = image_array[i+10:i+20, j+10:j+20,:]

# zeros[:,:,0] = 255

Image.fromarray(zeros).save('out.png')
Image.fromarray(image_array).save('image_array.png')
