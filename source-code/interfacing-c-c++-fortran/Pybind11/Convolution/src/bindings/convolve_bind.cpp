#include <convolution.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

void convolve_func(py::buffer image_buffer, py::buffer kernel_buffer,
        py::buffer new_image_buffer) {
    py::buffer_info image_info = image_buffer.request();
    if (image_info.format != py::format_descriptor<double>::format())
        throw std::runtime_error("Incompatible format: expected a double array");
    if (image_info.ndim != 2)
        throw std::runtime_error("Incompatible buffer dimension");
    py::buffer_info kernel_info = kernel_buffer.request();
    if (kernel_info.format != py::format_descriptor<double>::format())
        throw std::runtime_error("Incompatible format: expected a double array");
    if (kernel_info.ndim != 2)
        throw std::runtime_error("Incompatible buffer dimension");
    py::buffer_info result_info = new_image_buffer.request();
    if (result_info.format != py::format_descriptor<double>::format())
        throw std::runtime_error("Incompatible format: expected a double array");
    if (result_info.ndim != 2)
        throw std::runtime_error("Incompatible buffer dimension");
    if (result_info.shape[0] != image_info.shape[0] + kernel_info.shape[0] - 1 ||
            result_info.shape[1] != image_info.shape[1] + kernel_info.shape[1] - 1)
        throw std::runtime_error("Incompatible result buffer shape");
    Matrix image(image_info.shape[0], image_info.shape[1]);
    Matrix kernel(kernel_info.shape[0], kernel_info.shape[1]);
    std::memcpy(image.data(), image_info.ptr, sizeof(double)*image.rows()*image.cols());
    std::memcpy(kernel.data(), kernel_info.ptr, sizeof(double)*kernel.rows()*kernel.cols());
    Matrix result = convolve(image, kernel);
    std::memcpy(result_info.ptr, result.data(), sizeof(double)*result.rows()*result.cols());
}

PYBIND11_MODULE(convolve, module) {
    module.doc() = "pybind11 wrapper module for convolution.h";
    module.def("convolve", &convolve_func, "compute convolution of image with kernel");
}
