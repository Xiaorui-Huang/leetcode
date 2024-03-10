#ifndef LC_122_BEST_TIME_TO_BUY_AND_SELL_STOCK_II_H
#define LC_122_BEST_TIME_TO_BUY_AND_SELL_STOCK_II_H
/*
 * @lc app=leetcode id=122 lang=cpp
 *
 *
 * https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
 *
 * 122. Best Time to Buy and Sell Stock II
Medium
You are given an integer array prices where prices[i] is the price of a given
stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at
most one share of the stock at any time. However, you can buy it then
immediately sell it on the same day.

Find and return the maximum profit you can achieve.



Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 7

    Explanation:
    Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
    Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3=3.

    Total profit is 4 + 3 = 7.

actions:
    buy (if no stock)    -> (stock)
    sell (if stock)      -> (no stock)
    do nothing           -> (carry over)

    * stupid idea...
    buy, sell (makes no sense, just do nothing then)
    sell, buy (if stock) -> (stock) (still makes no sense, do nothing)


--------------------------------------|
day | stock           | no stock      |
--------------------------------------|
1   | max(-7)         | 0             | max = 0 // base case
2   | max(0-1, -7)    | max(-7 + 1, 0) | max = 0
3   | max(0-5, -1)    | max(-1 + 5, 0)
4   | max(4-3, -1)    | max(-1 + 3, 4)
5   | max(4-6, 1)     | max(1 + 6, 4)
6   | max(7-4, 1)     | max(1 + 4, 7)
max = 7

Example 2:

    Input: prices = [1,2,3,4,5]
    Output: 4

    Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit
= 5-1 = 4. Total profit is 4.

Example 3:

    Input: prices = [7,6,4,3,1]
    Output: 0

    Explanation: There is no way to make a positive profit, so we never buy the
    stock to achieve the maximum profit of 0.

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

#define BOTTOM_UP_DP 0
#define BOTTOM_UP_DP_OPT 1
#define GREEDY 2

// #define APPROACH BOTTOM_UP_DP
// #define APPROACH BOTTOM_UP_DP_OPT
#define APPROACH GREEDY

class Solution {
  public:
    int maxProfit(vector<int> &prices) {
#if APPROACH == BOTTOM_UP_DP
        size_t stock_idx, no_stock_idx, prev_stock_idx = 0,
                                        prev_no_stock_idx = 1;
        std::vector<int> dp(2 * prices.size());
        // base case
        dp[prev_stock_idx] = -prices[0];
        dp[prev_no_stock_idx] = 0;

        for (size_t day = 1; day < prices.size(); day++) {
            stock_idx = 2 * day;
            no_stock_idx = stock_idx + 1;
            // do nothing or buy (-prices[day])
            dp[stock_idx] = std::max(
                {dp[prev_stock_idx], dp[prev_no_stock_idx] - prices[day]});
            // do nothing or sell (+prices[day])
            dp[no_stock_idx] = std::max(
                {dp[prev_no_stock_idx], dp[prev_stock_idx] + prices[day]});

            prev_stock_idx = stock_idx;
            prev_no_stock_idx = no_stock_idx;
        }

        return std::max(dp[dp.size() - 1], dp[dp.size() - 2]);
#elif APPROACH == BOTTOM_UP_DP_OPT
        int profit_stock = -prices[0];
        int profit_no_stock = 0;

        int prev_stock, prev_no_stock;

        for (size_t day = 1; day < prices.size(); day++) {
            prev_stock = profit_stock;
            prev_no_stock = profit_no_stock;

            profit_stock = std::max(prev_stock, prev_no_stock - prices[day]);
            profit_no_stock = std::max(prev_no_stock, prev_stock + prices[day]);
        }
        return std::max(profit_no_stock, profit_stock);
#elif APPROACH == GREEDY
        int profit_today, profit = 0;

        for (size_t day = 1; day < prices.size(); day++) {
            profit_today = prices[day] - prices[day - 1];
            if (profit_today > 0)
                profit += profit_today;
        }
        return profit;
#endif
    }
};
#endif
