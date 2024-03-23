#include "lc_122_medium_best_time_to_buy_and_sell_stock_ii.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 122_best_time_to_buy_and_sell_stock_ii_Example1) {
    Solution sol;
    std::vector<int> prices = {7, 1, 5, 3, 6, 4};
    EXPECT_EQ(sol.maxProfit(prices), 7);
}

TEST(LeetCode, 122_best_time_to_buy_and_sell_stock_ii_Example2) {
    Solution sol;
    std::vector<int> prices = {1, 2, 3, 4, 5};
    EXPECT_EQ(sol.maxProfit(prices), 4);
}

TEST(LeetCode, 122_best_time_to_buy_and_sell_stock_ii_Example3) {
    Solution sol;
    std::vector<int> prices = {7, 6, 4, 3, 1};
    EXPECT_EQ(sol.maxProfit(prices), 0);
}

TEST(LeetCode, 122_best_time_to_buy_and_sell_stock_ii_Increasing) {
    Solution sol;
    std::vector<int> prices = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    EXPECT_EQ(sol.maxProfit(prices), 9); // Buy at 1, sell at 10
}

TEST(LeetCode, 122_best_time_to_buy_and_sell_stock_ii_complex) {
    Solution sol;
    std::vector<int> prices = {43, 6,  7,  32, 66, 2,  3, 89, 88, 73, 65,
                               55, 32, 11, 12, 13, 10, 9, 20, 29, 28, 27,
                               0,  4,  2,  3,  66, 3,  2, 1,  1,  3,  7};
    EXPECT_EQ(sol.maxProfit(prices), 243);
}

TEST(LeetCode, 122_best_time_to_buy_and_sell_stock_ii_Random) {
    Solution sol;
    std::vector<int> prices = {3, 2, 6, 5, 0, 3};
    EXPECT_EQ(sol.maxProfit(prices),
              7); // Buy at 2, sell at 6; Buy at 0, sell at 3
}
