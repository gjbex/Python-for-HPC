#ifndef CONVOLUTION_HDR
#define CONVOLUTION_HDR

#include "matrices.h"

/**
 * @brief Compute the convolution of an image with a kernel.
 * @param image The image to convolve.  This is a 2D matrix with m rows and n columns.
 * @param kernel The kernel to convolve with. This is a 2D matrix with k rows and l columns,
 *               where k and l ard odd integers.
 * @return The result of the convolution. This is a 2D matrix with m + k - 1 rows
 *         and n + l -1 columns.
 */
Matrix convolve(const Matrix& image, const Matrix& kernel);

#endif
