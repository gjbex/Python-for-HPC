#include <convolution.h>
#include <iostream>

int main() {
    // Create a 10x10 image
    Matrix image(10, 10);
    for (int i = 0; i < image.rows(); ++i) {
        for (int j = 0; j < image.cols(); ++j) {
            image(i, j) = i*image.cols() + j;
        }
    }

    // Print the image
    std::cout << image << std::endl;

    // Create a 3x3 kernel
    Matrix kernel(3, 3);
    for (int i = 0; i < kernel.rows(); ++i) {
        for (int j = 0; j < kernel.cols(); ++j) {
            kernel(i, j) = 1.0/(kernel.rows()*kernel.cols());
        }
    }

    // Print the kernel
    std::cout << kernel << std::endl;

    // Create a convolution object
    auto new_image = convolve(image, kernel);

    // Print the result
    std::cout << new_image << std::endl;

    return 0;
}
