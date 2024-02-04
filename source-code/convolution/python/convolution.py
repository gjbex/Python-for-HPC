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
        output matrix, shape is the same as input

    Raises
    ------
    ValueError
        if dimensions of kernel are not odd
    '''
    if kernel.shape[0] % 2 != 1 or kernel.shape[1] % 2 != 1:
        raise ValueError("Only odd dimensions on filter supported")
    # kernel_row_mid and kernel_col_mid are number of elements between the
    # center elements # and the edge, i.e., for a 5x5 filter they will be 2.
    kernel_row_mid = kernel.shape[0]//2
    kernel_col_mid = kernel.shape[1]//2
    # Allocate result input.
    output = np.empty_like(input)
    # Do convolution.
    for row in range(input.shape[0]):
        min_kernel_row = max(0, kernel_row_mid - row)
        max_kernel_row = min(kernel.shape[0],
                             kernel_row_mid + input.shape[0] - row)
        for col in range(input.shape[1]):
            min_kernel_col = max(0, kernel_col_mid - col)
            max_kernel_col = min(kernel.shape[1],
                                 kernel_col_mid + input.shape[1] - col)
            value = 0.0
            # i and j are the kernel images
            for i in range(min_kernel_row, max_kernel_row):
                for j in range(min_kernel_col, max_kernel_col):
                    # k and l are the image indices
                    k = row - kernel_row_mid + i
                    l = col - kernel_col_mid + j
                    value += kernel[i, j]*input[k, l]
            output[row, col] = value
    return output
