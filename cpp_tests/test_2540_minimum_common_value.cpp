#include "lc_2540_easy_minimum_common_value.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 2540_minimum_common_value_1) {
    auto sol = Solution();
    vector<int> vec1 = {1, 2, 3};
    vector<int> vec2 = {2, 4};
    EXPECT_EQ(sol.getCommon(vec1, vec2), 2);
}

TEST(LeetCode, 2540_minimum_common_value_2) {
    auto sol = Solution();
    vector<int> vec1 = {1, 2, 3, 6};
    vector<int> vec2 = {2, 3, 4, 5};
    EXPECT_EQ(sol.getCommon(vec1, vec2), 2);
}

TEST(LeetCode, 2540_minimum_common_value_3) {
    auto sol = Solution();
    vector<int> vec1 = {4, 5, 6};
    vector<int> vec2 = {1, 2, 3};
    EXPECT_EQ(sol.getCommon(vec1, vec2), -1);
}

TEST(LeetCode, 2540_minimum_common_value_4) {
    auto sol = Solution();
    vector<int> vec1 = {1, 3, 5, 7};
    vector<int> vec2 = {2, 4, 6, 8};
    EXPECT_EQ(sol.getCommon(vec1, vec2), -1);
}

TEST(LeetCode, 2540_minimum_common_value_5) {
    auto sol = Solution();
    vector<int> vec1 = {1, 1, 2, 2, 3, 4};
    vector<int> vec2 = {2, 3, 3, 4, 4, 5};
    EXPECT_EQ(sol.getCommon(vec1, vec2), 2);
}

TEST(LeetCode, 2540_minimum_common_value_6) {
    auto sol = Solution();
    vector<int> vec1 = {10, 20, 30, 40};
    vector<int> vec2 = {15, 25, 35, 45};
    EXPECT_EQ(sol.getCommon(vec1, vec2), -1);
}

TEST(LeetCode, 2540_minimum_common_value_7) {
    auto sol = Solution();
    vector<int> vec1 = {1, 2, 3, 4, 5};
    vector<int> vec2 = {5, 6, 7, 8, 9};
    EXPECT_EQ(sol.getCommon(vec1, vec2), 5);
}


