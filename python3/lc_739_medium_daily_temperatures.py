#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (66.61%)
# Likes:    9736
# Dislikes: 224
# Total Accepted:    550.4K
# Total Submissions: 828.1K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
#
#
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
#
#
# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "monotonic_stack direct_address_tables")
APPR = appr.monotonic_stack


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        if APPR == appr.monotonic_stack:
            return self.dailyTemperatures_monotonic_stack(temperatures)
        return []  # Never Reached

    def dailyTemperatures_monotonic_stack(self, temperatures: list[int]) -> list[int]:
        ans = [0] * len(temperatures)  # important for the last few values to have a value of 0
        stack: list[int] = []
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                # pop all values that are smaller out and calculate the distance
                cur_i = stack.pop()
                ans[cur_i] = i - cur_i
            stack.append(i)
        return ans


# @lc code=end
