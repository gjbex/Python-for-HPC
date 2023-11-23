cmake_minimum_required(VERSION 3.22)

project(HelloWorld LANGUAGE C)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(Cython REQUIRED)
find_package(PythonExtensions REQUIRED)
# include_directories(${PYTHON_INCLUDE_DIRS})

add_cython_target(hello_world hello_world.pyx PY3 OUTPUT_VAR hello_world_src)
add_library(hello_world MODULE ${hello_world_src})
target_include_directories(hello_world PRIVATE ${PYTHON_INCLUDE_DIRS})
set_target_properties(hello_world PROPERTIES PREFIX "")

install(TARGETS hello_world DESTINATION .)
install(FILES say_hello.py
    DESTINATION .
    RENAME say_hello
    PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
)
