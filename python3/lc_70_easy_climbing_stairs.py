#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (51.78%)
# Likes:    15718
# Dislikes: 477
# Total Accepted:    2M
# Total Submissions: 3.9M
# Testcase Example:  '2'
#
# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
#
#
# Example 1:
#
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
#
#
# Constraints:
#
#
# 1 <= n <= 45
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "iterative DP_mem")
APPR = appr.DP_mem


class Solution:
    def __init__(self) -> None:
        self.mem: dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        if APPR == appr.DP_mem:
            return self.climbStairs_DP_mem(n)
        if APPR == appr.iterative:
            return self.climbStairs_iterative(n)
        return 0  # Never Reached

    def climbStairs_DP_mem(self, n: int) -> int:
        if 1 <= n <= 2:
            return n
        if n in self.mem:
            return self.mem[n]
        compute = self.climbStairs_DP_mem(n - 1) + self.climbStairs_DP_mem(n - 2)
        self.mem[n] = compute
        return compute

    def climbStairs_iterative(self, n: int) -> int:

        if n == 1:
            return 1
        this_step = 0

        prev_one_steps, prev_two_steps = 1, 1
        for _ in range(n - 1):
            this_step = prev_one_steps + prev_two_steps
            prev_two_steps, prev_one_steps = prev_one_steps, this_step
        return this_step

    # this step = prev step + two step before
    # 1 step  - 1
    # 2 step  - 1 + 1
    # 3 steps - 2 + 1
    # 4 steps - 3 + 2
    # 5 steps - 5 + 3


# @lc code=end
