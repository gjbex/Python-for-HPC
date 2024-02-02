#include <convolution.h>
#include <chrono>
#include <iostream>
#include <numeric>
#include <random>

Matrix create_image(int rows, int cols) {
    std::mt19937 gen(1234);
    std::uniform_real_distribution<double> dis(0.0, 1.0);
    Matrix image(rows, cols);
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            image(i, j) = dis(gen);
        }
    }
    return image;
}

Matrix create_kernel(int rows, int cols) {
    Matrix kernel(rows, cols);
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            kernel(i, j) = 1.0/(rows*cols);
        }
    }
    return kernel;
}

double element_sum(const Matrix& matrix) {
    return std::accumulate(matrix.data(), matrix.data() + matrix.rows()*matrix.cols(), 0.0);
}

int main(int argc, char** argv) {
    int rows = 1000;
    int cols = 1000;
    int kernel_rows = 7;
    int kernel_cols = 7;
    if (argc > 1) {
        rows = atoi(argv[1]);
        cols = atoi(argv[1]);
    }
    if (argc > 2) {
        kernel_rows = atoi(argv[2]);
        kernel_cols = atoi(argv[2]);
    }
    std::cout << "Image size: " << rows << "x" << cols << "\n";
    std::cout << "Kernel size: " << kernel_rows << "x" << kernel_cols << "\n";
    Matrix image = create_image(rows, cols);
    Matrix kernel = create_kernel(kernel_rows, kernel_cols);
    auto start = std::chrono::high_resolution_clock::now();
    auto result = convolve(image, kernel);
    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff = end - start;
    std::cout << "Time: " << diff.count() << " s\n";
    std::cout << "Sum: " << element_sum(result) << "\n";
    return 0;
}
