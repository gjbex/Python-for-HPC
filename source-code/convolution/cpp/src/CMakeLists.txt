add_subdirectory(convolution)

find_package(Catch2)

if(Catch2_FOUND)
    add_executable(test_convolution.exe
        test_convolution.cpp)
    target_link_libraries(test_convolution.exe
        PRIVATE Catch2::Catch2WithMain)
    target_include_directories(test_convolution.exe
        PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/convolution)
    target_link_libraries(test_convolution.exe
        PRIVATE convolution)
else()
    message(STATUS "Catch2 not found, tests will not be built")
endif()

add_executable(benchmark_convolution.exe
        benchmark_convolution.cpp)
target_include_directories(benchmark_convolution.exe
    PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/convolution)
target_link_libraries(benchmark_convolution.exe
    PRIVATE convolution)
