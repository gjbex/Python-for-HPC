#include <matrices.h>
#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

PYBIND11_MODULE(matrices, module) {
    module.doc() = "pybind11 wrapper module for matrices.h";
    py::class_<Matrix>(module, "Matrix", py::buffer_protocol())
        .def_buffer([](Matrix &m) -> py::buffer_info {
            return py::buffer_info(
                m.data(),                                /* Pointer to buffer */
                sizeof(double),                          /* Size of one scalar */
                py::format_descriptor<double>::format(), /* Python struct-style format descriptor */
                2,                                       /* Number of dimensions */
                {m.rows(), m.cols()},                    /* Buffer dimensions */
                {sizeof(double)*m.cols(),                /* Strides (in bytes) for each index */
                 sizeof(double)});
        })
        .def(py::init<int, int>(), "initialize matrix with given number of rows and columns")
        .def(py::init([](const py::buffer b) {
            py::buffer_info info = b.request();
            if (info.format != py::format_descriptor<double>::format())
                throw std::runtime_error("Incompatible format: expected a double array");
            if (info.ndim != 2)
                throw std::runtime_error("Incompatible buffer dimension!");
            Matrix m(info.shape[0], info.shape[1]);
            std::memcpy(m.data(), info.ptr, sizeof(double)*m.rows()*m.cols());
            return m;
        }), "initialize matrix from a numpy array");
}
