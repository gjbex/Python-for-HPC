import convolution
import numpy as np
import pytest

def test_4x4_kernel_error():
    image_size, kernel_size = 5, 4
    image = np.ones((image_size, image_size))
    kernel = np.ones((kernel_size, kernel_size))
    with pytest.raises(ValueError):
        new_image = convolution.convolve(image, kernel)

def test_3x3_kernel():
    image_size, kernel_size = 5, 3
    image = np.ones((image_size, image_size))
    kernel = np.ones((kernel_size, kernel_size))
    new_image = convolution.convolve(image, kernel)
    target = np.array([
        [4, 6, 6, 6, 4,],
        [6, 9, 9, 9, 6,],
        [6, 9, 9, 9, 6,],
        [6, 9, 9, 9, 6,],
        [4, 6, 6, 6, 4,],
    ], dtype=np.float64)
    assert (new_image == target).all()

def test_5x5_kernel():
    image_size, kernel_size = 6, 5
    image = np.ones((image_size, image_size))
    kernel = np.ones((kernel_size, kernel_size))
    new_image = convolution.convolve(image, kernel)
    target = np.array([
        [9, 12, 15, 15, 12, 9,],
        [12, 16, 20, 20, 16, 12,],
        [15, 20, 25, 25, 20, 15,],
        [15, 20, 25, 25, 20, 15,],
        [12, 16, 20, 20, 16, 12,],
        [9, 12, 15, 15, 12, 9,],
    ], dtype=np.float64)
    assert (new_image == target).all()

