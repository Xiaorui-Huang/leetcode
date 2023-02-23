#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#
# https://leetcode.com/problems/ipo/description/
#
# algorithms
# Hard (45.10%)
# Likes:    1362
# Dislikes: 109
# Total Accepted:    49.3K
# Total Submissions: 105.7K
# Testcase Example:  '2\n0\n[1,2,3]\n[0,1,1]'
#
# Suppose LeetCode will start its IPO soon. In order to sell a good price of
# its shares to Venture Capital, LeetCode would like to work on some projects
# to increase its capital before the IPO. Since it has limited resources, it
# can only finish at most k distinct projects before the IPO. Help LeetCode
# design the best way to maximize its total capital after finishing at most k
# distinct projects.
#
# You are given n projects where the i^th project has a pure profit profits[i]
# and a minimum capital of capital[i] is needed to start it.
#
# Initially, you have w capital. When you finish a project, you will obtain its
# pure profit and the profit will be added to your total capital.
#
# Pick a list of at most k distinct projects from given projects to maximize
# your final capital, and return the final maximized capital.
#
# The answer is guaranteed to fit in a 32-bit signed integer.
#
#
# Example 1:
#
#
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project
# indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project
# indexed 2.
# Since you can choose at most 2 projects, you need to finish the project
# indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= k <= 10^5
# 0 <= w <= 10^9
# n == profits.length
# n == capital.length
# 1 <= n <= 10^5
# 0 <= profits[i] <= 10^4
# 0 <= capital[i] <= 10^9
#
#
#


# @lc code=start
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort(key=lambda x: x[0])

        max_heap: list[int] = []
        feasible_i = 0

        for _ in range(k):
            for i in range(feasible_i, n):
                cur_capital, cur_profit = projects[i]

                if cur_capital > w:  # cannot do this project
                    break

                # since heapq is min heap, we negate it to use as max heap
                heapq.heappush(max_heap, -cur_profit)
                feasible_i += 1

            # no feasible project to start
            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w


# @lc code=end
