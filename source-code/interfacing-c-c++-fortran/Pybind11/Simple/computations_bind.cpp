#include <pybind11/pybind11.h>
#include "computations.h"

namespace py = pybind11;

PYBIND11_MODULE(computations, m) {
    m.doc() = "pybind11 wrapper module for cmoputations.h";
    m.def("add", &add, "function that adds two numbers");
    m.def("mul", &mul, "function that multiplies two numbers");
    m.def("div", &divide, "function that divides two numbers",
            py::arg("num"), py::arg("denom"));
}
