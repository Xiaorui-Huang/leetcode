# google test setup 
# reference: https://cliutils.gitlab.io/modern-cmake/chapters/testing/googletest.html 
add_subdirectory("${PROJECT_SOURCE_DIR}/extern/googletest" "extern/googletest")

mark_as_advanced(
    BUILD_GMOCK BUILD_GTEST BUILD_SHARED_LIBS
    gmock_build_tests gtest_build_samples gtest_build_tests
    gtest_disable_pthreads gtest_force_shared_crt gtest_hide_internal_symbols
)
set_target_properties(gtest PROPERTIES FOLDER extern)
set_target_properties(gtest_main PROPERTIES FOLDER extern)
set_target_properties(gmock PROPERTIES FOLDER extern)
set_target_properties(gmock_main PROPERTIES FOLDER extern)

macro(package_add_test TESTNAME)
    # create an exectuable in which the tests will be stored
    add_executable(${TESTNAME} ${ARGN})
    # link the Google test infrastructure, mocking library, and a default main fuction to
    # the test executable.  Remove g_test_main if writing your own main function.
    target_link_libraries(${TESTNAME} gtest gmock gtest_main)
    # gtest_discover_tests replaces gtest_add_tests,
    # see https://cmake.org/cmake/help/v3.10/module/GoogleTest.html for more options to pass to it
    gtest_discover_tests(${TESTNAME}
        # set a working directory so your project root so that you can find test data via paths relative to the project root
        WORKING_DIRECTORY ${PROJECT_DIR}
        PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${PROJECT_DIR}"
    )
    set_target_properties(${TESTNAME} PROPERTIES FOLDER cpp_tests)
endmacro()

macro(package_add_test_with_libraries TESTNAME)
    add_executable(${TESTNAME} ${TESTNAME}.cpp )
    target_link_libraries(${TESTNAME} gtest gmock gtest_main ${ARGN})
    gtest_discover_tests(${TESTNAME}
        WORKING_DIRECTORY ${PROJECT_DIR}
        PROPERTIES VS_DEBUGGER_WORKING_DIRECTORY "${PROJECT_DIR}"
    )
    set_target_properties(${TESTNAME} PROPERTIES FOLDER cpp_tests)
endmacro()

# Set up dependencies
SET(REQUIRED_LIBRARIES core)

# list of tests
file(GLOB TESTFILES ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
foreach(TESTFILE ${TESTFILES})
    get_filename_component(FILENAME ${TESTFILE} NAME_WLE) # this get the filename without the extension
    #string(REGEX MATCH "[0-9]+" PROBLEM_ID ${TEST}) # match only up to the problem id
    package_add_test_with_libraries(${FILENAME} ${REQUIRED_LIBRARIES})
    # package_add_test(${FILENAME} ${FILENAME}.cpp)
endforeach()

