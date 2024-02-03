add_subdirectory(convolution)

add_executable(test_convolution.exe
        test_convolution.cpp)
target_include_directories(test_convolution.exe
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/convolution)
target_link_libraries(test_convolution.exe
    PRIVATE convolution)

add_executable(benchmark_convolution.exe
        benchmark_convolution.cpp)
target_include_directories(benchmark_convolution.exe
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/convolution)
target_link_libraries(benchmark_convolution.exe
    PRIVATE convolution)
