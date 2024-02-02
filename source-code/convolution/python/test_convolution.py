#!/usr/bin/env python

import convolution
import numpy as np


image = np.arange(0.0, 100.0, 1.0).reshape(10, 10)
print(f'{image}\n')
kernel = np.ones((3, 3))/(3*3)
print(f'{kernel}\n')

print(convolution.convolve(image, kernel))
