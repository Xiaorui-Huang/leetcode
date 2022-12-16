cmake_minimum_required(VERSION 3.25) 
project(leetcode)

# Avoid warning about DOWNLOAD_EXTRACT_TIMESTAMP in CMake 3.24:
if (CMAKE_VERSION VERSION_GREATER_EQUAL "3.24.0")
		cmake_policy(SET CMP0135 NEW)
endif()

set(CMAKE_CXX_STANDARD 17)

# include files for leetcode tests imports
include_directories("include/")
include_directories("cpp/")
include_directories("cpp/utils/")
file(GLOB SRCFILES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/*.cpp) # souce code for LeetCode solutions
file(GLOB MAINFILES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/mains/*.cpp) # main function entry point for each LeetCode problem
file(GLOB UTILFILES ${CMAKE_CURRENT_SOURCE_DIR}/cpp/utils/*.cpp) # utility classes & functions for common LeetCode datastructures

# create libraries for tests from source
add_library(core ${SRCFILES})
add_library(utils ${UTILFILES})
foreach(FILE ${SRCFILES})
    #get_filename_component(FILENAME ${FILE} NAME_WLE) # this get the filename without the extension
    #add_executable(${FILENAME} ${FILE})
    string(REGEX MATCH "[0-9]+" PROBLEM_ID ${FILE}) # match only up to the problem id
    string(REPLACE "lc" "mains/main" MAIN ${FILE}) # use the file name to get path to main file
    # if there is a main file then create executable & library then link lib to exe
    if(EXISTS ${MAIN})
         add_executable(${PROBLEM_ID} ${FILE}) # e.g. add executable 124 <- lc_124_hard_binary_tree_maximum_path_sum.cpp
         add_library(${PROBLEM_ID}_LIB ${MAIN}) # e.g. add library 124_LIB <- main_124_hard_binary_tree_maximum_path_sum.cpp
         target_link_libraries(${PROBLEM_ID} utils ${PROBLEM_ID}_LIB) # e.g. link 124 <- 124_LIB 
    endif()
endforeach()

## temporary: for utils library development and testing
#foreach(UTIL ${UTILFILES})
    #get_filename_component(FILENAME ${UTIL} NAME_WLE) # this get the filename without the extension
    #add_executable(${FILENAME} ${UTIL})
#endforeach()


# Load Google Test
option(PACKAGE_TESTS "Build the tests" ON)
if(PACKAGE_TESTS AND PROJECT_NAME STREQUAL CMAKE_PROJECT_NAME)
    MESSAGE(STATUS "Setting Up Tests")
    enable_testing()
    include(GoogleTest)
    add_subdirectory(cpp_tests)
endif()
