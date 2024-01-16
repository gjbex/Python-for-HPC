#include "convolution.h"
#include <exception>

Matrix convolve(const Matrix& image, const Matrix& kernel) {
    if (kernel.rows() % 2 != 1 || kernel.cols() % 2 != 1) {
        throw std::invalid_argument("Only odd dimensions on kernel supported");
    }
    /*
      s_mid and t_mid are number of pixels between the center pixel
      and the edge, ie for a 5x5 filter they will be 2.
      
      The output size is calculated by adding s_mid, t_mid to each
      side of the dimensions of the input image.
    */
    auto s_mid {kernel.rows()/2};
    auto t_mid {kernel.cols()/2};
    auto x_max {image.rows() + 2*s_mid};
    auto y_max {image.cols() + 2*t_mid};
    // Allocate result image.
    Matrix new_image(x_max, y_max);
    // Do convolution
    for (int x = 0; x < x_max; ++x) {
        for (int y = 0; y < y_max; ++y) {
            // Calculate pixel value for h at (x,y). Sum one component
            // for each pixel (s, t) of the filter kernel.
            auto s_from {std::max(s_mid - x, -s_mid)};
            auto s_to {std::min((x_max - x) - s_mid, s_mid + 1)};
            auto t_from {std::max(t_mid - y, -t_mid)};
            auto t_to {std::min((y_max - y) - t_mid, t_mid + 1)};
            double value {0.0};
            for (int s = s_from; s < s_to; ++s) {
                for (int t = t_from; t < t_to; ++t) {
                    auto v {x - s_mid + s};
                    auto w {y - t_mid + t};
                    value += kernel(s_mid - s, t_mid - t)*image(v, w);
                }
            }
            new_image(x, y) = value;
        }
    }
    return new_image;
}
