#include <pybind11/pybind11.h>
#include "computations.h"

PYBIND11_MODULE(computations, m) {
    m.doc() = "pybind11 wrapper module for cmoputations.h";
    m.def("add", &add, "function that adds two numbers");
    m.def("mul", &mul, "function that multiplies two numbers");
    m.def("div", &div, "function that divides two numbers"
            py::arg("left_op"), py::arg("right_op"));
}
