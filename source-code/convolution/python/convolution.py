import numpy as np


def convolve(input, kernel):
    '''Naive convolution of matrices input and kernel

    Parameters
    ----------
    input : numpy.ndarray
        input matrix
    kernel : numpy.ndarray
        filter kernel matrix, dimensions must be odd

    Returns
    -------
    output : numpy.ndarray
        output matrix, it is not cropped

    Raises
    ------
    ValueError
        if dimensions of kernel are not odd
    '''
    if kernel.shape[0] % 2 != 1 or kernel.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")
    # s_mid and t_mid are number of pixels between the center pixel
    # and the edge, ie for a 5x5 filter they will be 2.
    #
    # The output size is calculated by adding s_mid, t_mid to each
    # side of the dimensions of the input image.
    s_mid = kernel.shape[0] // 2
    t_mid = kernel.shape[1] // 2
    x_max = input.shape[0] + 2 * s_mid
    y_max = input.shape[1] + 2 * t_mid
    # Allocate result image.
    output = np.zeros([x_max, y_max], dtype=input.dtype)
    # Do convolution
    for x in range(x_max):
        for y in range(y_max):
            # Calculate pixel value for h at (x,y). Sum one component
            # for each pixel (s, t) of the filter kernel.
            s_from = max(s_mid - x, -s_mid)
            s_to = min((x_max - x) - s_mid, s_mid + 1)
            t_from = max(t_mid - y, -t_mid)
            t_to = min((y_max - y) - t_mid, t_mid + 1)
            value = 0
            for s in range(s_from, s_to):
                for t in range(t_from, t_to):
                    v = x - s_mid + s
                    w = y - t_mid + t
                    value += kernel[s_mid - s, t_mid - t]*input[v, w]
            output[x, y] = value
    return output
