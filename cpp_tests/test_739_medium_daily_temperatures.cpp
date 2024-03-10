#include "lc_739_medium_daily_temperatures.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 739_medium_daily_temperatures) {
    std::vector<int> temps{73, 74, 75, 71, 69, 72, 76, 73};
    auto sol = Solution().dailyTemperatures(temps);
    std::vector<int> ans = {1, 1, 4, 2, 1, 1, 0, 0};
    EXPECT_TRUE(sol == ans);
}
