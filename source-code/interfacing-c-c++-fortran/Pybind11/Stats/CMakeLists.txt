cmake_minimum_required(VERSION 3.0)
project(statistics LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

find_package(pybind11 REQUIRED)
add_subdirectory(src)
