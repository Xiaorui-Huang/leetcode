#include "lc_1700_easy_number_of_students_unable_to_eat_lunch.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 1700_easy_number_of_students_unable_to_eat_lunch) {
    auto sol = Solution();
    vector<int> students = {1, 1, 0, 0};
    vector<int> sandwiches = {0, 1, 0, 1};
    EXPECT_EQ(sol.countStudents(students, sandwiches), 0);
}

TEST(LeetCode, 1700_easy_number_of_students_unable_to_eat_lunch_2) {
    auto sol = Solution();
    vector<int> students = {1, 1, 1, 0, 0, 1};
    vector<int> sandwiches = {1, 0, 0, 0, 1, 1};
    EXPECT_EQ(sol.countStudents(students, sandwiches), 3);
}
