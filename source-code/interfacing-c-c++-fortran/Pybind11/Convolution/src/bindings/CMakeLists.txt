find_package(pybind11 REQUIRED)

pybind11_add_module(matrices matrix_bind.cpp)
target_include_directories(matrices PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../convolution)
target_link_libraries(matrices PUBLIC convolution)

pybind11_add_module(convolve convolve_bind.cpp)
target_include_directories(convolve PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/../convolution)
target_link_libraries(convolve PUBLIC convolution)
