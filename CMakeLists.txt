# NB: This is a CMake file for building the LeetCode solutions in C++.
cmake_minimum_required(VERSION 3.24) 
project(leetcode)

if(MSVC)
    # https://learn.microsoft.com/en-us/cpp/error-messages/compiler-warnings/compiler-warning-level-1-c4312?view=msvc-170
    # Windows is doing some weired intermediate casting, idk
    add_compile_options(/wd4312) # disable warning C4312: 'type cast': conversion from 'type1' to 'type2' of greater size
endif()

# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP in CMake 3.24:
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
		cmake_policy(SET CMP0135 NEW)
endif()

set(CMAKE_CXX_STANDARD 17)

# include files for leetcode tests imports
include_directories("include/")
include_directories("cpp/")
include_directories("cpp/libs/")

include_directories("c/")  # Include C files directory

# Cpp files
file(GLOB SRCFILES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/*.cpp) # souce code for LeetCode solutions
file(GLOB MAINFILES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/mains/*.cpp) # main function entry point for each LeetCode problem
file(GLOB UTILFILES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/libs/*.cpp) # utility classes & functions for common LeetCode datastructures

# Add C files from the c directory
file(GLOB CFILES ${CMAKE_CURRENT_SOURCE_DIR}/c/*.c)

# create libraries for tests from source
add_library(core ${SRCFILES})
add_library(libs ${UTILFILES})
add_library(c_library ${CFILES})  # Add a library for the C files

foreach(MAINFILE ${MAINFILES})
    get_filename_component(MAIN ${MAINFILE} NAME_WLE) # this get the filename without the extension
    string(REGEX MATCH "[0-9]+" PROBLEM_ID ${MAIN}) # match only up to the problem id
    string(REPLACE "mains/main" "lc" FILE ${MAINFILE}) # use the file name to get path to main file
    # if there is a main file then create executable & library then link lib to exe
    add_executable(${PROBLEM_ID} ${MAINFILE}) # e.g. add executable 124 <- lc_124_hard_binary_tree_maximum_path_sum.cpp
    add_library(${PROBLEM_ID}_LIB ${FILE}) # e.g. add library 124_LIB <- main_124_hard_binary_tree_maximum_path_sum.cpp
    target_link_libraries(${PROBLEM_ID} libs ${PROBLEM_ID}_LIB) # e.g. link 124 <- 124_LIB 
endforeach()

## temporary: for libs library development and testing
#foreach(UTIL ${UTILFILES})
    #get_filename_component(FILENAME ${UTIL} NAME_WLE) # this get the filename without the extension
    #add_executable(${FILENAME} ${UTIL})
#endforeach()

# suppress warnings for Google Test in gtest-port.h for undefined macros 
add_definitions(-DGTEST_CREATE_SHARED_LIBRARY=0)
add_definitions(-DGTEST_LINKED_AS_SHARED_LIBRARY=0)

# Load Google Test
option(PACKAGE_TESTS "Build the tests" ON)
if(PACKAGE_TESTS AND PROJECT_NAME STREQUAL CMAKE_PROJECT_NAME)
    MESSAGE(STATUS "Setting Up Tests")
    enable_testing()
    include(GoogleTest)
    add_subdirectory(cpp_tests)
endif()
