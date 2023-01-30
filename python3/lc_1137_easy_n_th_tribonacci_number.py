#
# @lc app=leetcode id=1137 lang=python3
#
# [1137] N-th Tribonacci Number
#
# https://leetcode.com/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (63.26%)
# Likes:    2917
# Dislikes: 143
# Total Accepted:    412.9K
# Total Submissions: 648.8K
# Testcase Example:  '4'
#
# The Tribonacci sequence Tn is defined as follows:
#
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
#
# Given n, return the value of Tn.
#
#
# Example 1:
#
#
# Input: n = 4
# Output: 4
# Explanation:
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# Example 2:
#
#
# Input: n = 25
# Output: 1389537
#
#
#
# Constraints:
#
#
# 0 <= n <= 37
# The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 -
# 1.
#
#


# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        num_prev_2 = 0
        num_prev_1 = 1
        num = 1

        for _ in range(n - 2):
            num, num_prev_1, num_prev_2 = num + num_prev_1 + num_prev_2, num, num_prev_1

        return num


# @lc code=end
