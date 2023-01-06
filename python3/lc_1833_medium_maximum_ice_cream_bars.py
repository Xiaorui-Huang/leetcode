#
# @lc app=leetcode id=1833 lang=python3
#
# [1833] Maximum Ice Cream Bars
#
# https://leetcode.com/problems/maximum-ice-cream-bars/description/
#
# algorithms
# Medium (65.69%)
# Likes:    1644
# Dislikes: 583
# Total Accepted:    113.8K
# Total Submissions: 153.6K
# Testcase Example:  '[1,3,2,4,1]\n7'
#
# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
#
# At the store, there are n ice cream bars. You are given an array costs of
# length n, where costs[i] is the price of the i^th ice cream bar in coins. The
# boy initially has coins coins to spend, and he wants to buy as many ice cream
# bars as possible.
#
# Return the maximum number of ice cream bars the boy can buy with coins
# coins.
#
# Note: The boy can buy the ice cream bars in any order.
#
#
# Example 1:
#
#
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total
# price of 1 + 3 + 2 + 1 = 7.
#
#
# Example 2:
#
#
# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.
#
#
# Example 3:
#
#
# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 +
# 6 + 3 + 1 + 2 + 5 = 18.
#
#
#
# Constraints:
#
#
# costs.length == n
# 1 <= n <= 10^5
# 1 <= costs[i] <= 10^5
# 1 <= coins <= 10^8
#
#

# @lc code=start
from heapq import heappush, heapreplace


class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        heap: list[int] = []  # a max heap implemented with min heap using -1 of it's values
        count = 0
        spending = 0
        for cost in costs:
            if spending + cost <= coins:
                spending += cost
                count += 1
                heappush(heap, -cost)  # use -cost, since we want to use a max heap instead of the default min heap
                continue
            # the cost of this new ice cream is more than the most costly ice cream we can give up for it... so just skip it.
            if not heap or cost >= -heap[0]:
                continue
            # since the current ice cream is cheaper than the most costly ice cream we currently have, take it
            # since we swapped ice cream, count is not changed
            # pop then push
            spending += heapreplace(heap, -cost) + cost  # remember heappop give a negative number

        return count


# @lc code=end
