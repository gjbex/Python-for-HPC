#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <convolution.h>

TEST_CASE("3x3 kernel", "[convolution]") {
    const int input_size {5};
    const int kernel_size {3};

    Matrix input(input_size, input_size);
    for (int i = 0; i < input.rows(); ++i) {
        for (int j = 0; j < input.cols(); ++j) {
            input(i, j) = 1.0;
        }
    }

    Matrix kernel(kernel_size, kernel_size);
    for (int i = 0; i < kernel.rows(); ++i) {
        for (int j = 0; j < kernel.cols(); ++j) {
            kernel(i, j) = 1.0;
        }
    }

    Matrix target(input_size, input_size);
    target(0, 0) = 4.0;
    target(0, 1) = 6.0;
    target(0, 2) = 6.0;
    target(0, 3) = 6.0;
    target(0, 4) = 4.0;
    target(1, 0) = 6.0;
    target(1, 1) = 9.0;
    target(1, 2) = 9.0;
    target(1, 3) = 9.0;
    target(1, 4) = 6.0;
    target(2, 0) = 6.0;
    target(2, 1) = 9.0;
    target(2, 2) = 9.0;
    target(2, 3) = 9.0;
    target(2, 4) = 6.0;
    target(3, 0) = 6.0;
    target(3, 1) = 9.0;
    target(3, 2) = 9.0;
    target(3, 3) = 9.0;
    target(3, 4) = 6.0;
    target(4, 0) = 4.0;
    target(4, 1) = 6.0;
    target(4, 2) = 6.0;
    target(4, 3) = 6.0;
    target(4, 4) = 4.0;

    auto result = convolve(input, kernel);

    REQUIRE(result == target);
}

TEST_CASE("5x5 kernel", "[convolution]") {
    const int input_size {6};
    const int kernel_size {5};

    Matrix input(input_size, input_size);
    for (int i = 0; i < input.rows(); ++i) {
        for (int j = 0; j < input.cols(); ++j) {
            input(i, j) = 1.0;
        }
    }

    Matrix kernel(kernel_size, kernel_size);
    for (int i = 0; i < kernel.rows(); ++i) {
        for (int j = 0; j < kernel.cols(); ++j) {
            kernel(i, j) = 1.0;
        }
    }

    Matrix target(input_size, input_size);
    target(0, 0) = 9.0;
    target(0, 1) = 12.0;
    target(0, 2) = 15.0;
    target(0, 3) = 15.0;
    target(0, 4) = 12.0;
    target(0, 5) = 9.0;
    target(1, 0) = 12.0;
    target(1, 1) = 16.0;
    target(1, 2) = 20.0;
    target(1, 3) = 20.0;
    target(1, 4) = 16.0;
    target(1, 5) = 12.0;
    target(2, 0) = 15.0;
    target(2, 1) = 20.0;
    target(2, 2) = 25.0;
    target(2, 3) = 25.0;
    target(2, 4) = 20.0;
    target(2, 5) = 15.0;
    target(3, 0) = 15.0;
    target(3, 1) = 20.0;
    target(3, 2) = 25.0;
    target(3, 3) = 25.0;
    target(3, 4) = 20.0;
    target(3, 5) = 15.0;
    target(4, 0) = 12.0;
    target(4, 1) = 16.0;
    target(4, 2) = 20.0;
    target(4, 3) = 20.0;
    target(4, 4) = 16.0;
    target(4, 5) = 12.0;
    target(5, 0) = 9.0;
    target(5, 1) = 12.0;
    target(5, 2) = 15.0;
    target(5, 3) = 15.0;
    target(5, 4) = 12.0;
    target(5, 5) = 9.0;
    auto result = convolve(input, kernel);

    REQUIRE(result == target);
}

TEST_CASE("even-sized kernel error", "[convolution]") {
    const int input_size {5};
    const int kernel_size {4};

    Matrix input(input_size, input_size);
    for (int i = 0; i < input.rows(); ++i) {
        for (int j = 0; j < input.cols(); ++j) {
            input(i, j) = 1.0;
        }
    }

    Matrix kernel(kernel_size, kernel_size);
    for (int i = 0; i < kernel.rows(); ++i) {
        for (int j = 0; j < kernel.cols(); ++j) {
            kernel(i, j) = 1.0;
        }
    }
    REQUIRE_THROWS_AS(convolve(input, kernel), std::invalid_argument);
}

