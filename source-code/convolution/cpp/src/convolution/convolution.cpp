#include "convolution.h"
#include <exception>

Matrix convolve(const Matrix& input, const Matrix& kernel) {
    if (kernel.rows() % 2 != 1 || kernel.cols() % 2 != 1) {
        throw std::invalid_argument("Only odd dimensions on kernel supported");
    }
    /*
      kernel_row_mid and kernel_col_mid are number of pixels between the center pixel
      and the edge, ie for a 5x5 filter they will be 2.
      
      The output size is calculated by adding kernel_row_mid, kernel_col_mid to each
      side of the dimensions of the input input.
    */
    auto kernel_row_mid {kernel.rows()/2};
    auto kernel_col_mid {kernel.cols()/2};
    // Allocate result input.
    Matrix output(input.rows(), input.cols());
    // Do convolution.
    for (int row = 0; row < input.rows(); ++row) {
        auto min_kernel_row {std::max(0, kernel_row_mid - row)};
        auto max_kernel_row {std::min(kernel.cols(), kernel_row_mid + input.rows() - row)};
        for (int col = 0; col < input.cols(); ++col) {
            auto min_kernel_col {std::max(0, kernel_col_mid - col)};
            auto max_kernel_col {std::min(kernel.cols(), kernel_col_mid + input.cols() - col)};
            double value {0.0};
            // i and j are the kernel images.
            for (int i = min_kernel_row; i < max_kernel_row; ++i) {
                for (int j = min_kernel_col; j < max_kernel_col; ++j) {
                    // k and l are the image indices.
                    auto k {row - kernel_row_mid + i};
                    auto l {col - kernel_col_mid + j};
                    value += kernel(i, j)*input(k, l);
                }
            }
            output(row, col) = value;
        }
    }
    return output;
}
