#include "lc_486_medium_predict_the_winner.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, lc_486_medium_predict_the_winner) {
    auto sol = Solution();
    std::vector<int> arr{1, 5, 233, 7};
    EXPECT_TRUE(sol.PredictTheWinner(arr));
}
