#include "lc_1143_medium_longest_common_subsequence.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 1143_medium_longest_common_subsequence) {
    auto sol = Solution();
    EXPECT_EQ(sol.longestCommonSubsequence("abcde", "ace"), 3);
    EXPECT_EQ(sol.longestCommonSubsequence("abc", "abc"), 3);
    EXPECT_EQ(sol.longestCommonSubsequence("abc", "def"), 0);
}
