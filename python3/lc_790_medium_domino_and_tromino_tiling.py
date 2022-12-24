#
# @lc app=leetcode id=790 lang=python3
#
# [790] Domino and Tromino Tiling
#
# https://leetcode.com/problems/domino-and-tromino-tiling/description/
#
# algorithms
# Medium (48.42%)
# Likes:    1957
# Dislikes: 686
# Total Accepted:    61.1K
# Total Submissions: 123.6K
# Testcase Example:  '3'
#
# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You
# may rotate these shapes.
#
# Given an integer n, return the number of ways to tile an 2 x n board. Since
# the answer may be very large, return it modulo 10^9 + 7.
#
# In a tiling, every square must be covered by a tile. Two tilings are
# different if and only if there are two 4-directionally adjacent cells on the
# board such that exactly one of the tilings has both squares occupied by a
# tile.
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 5
# Explanation: The five different ways are show above.
#
#
# Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 1000
#
#
#

# @lc code=start
from collections import deque

MOD = 10**9 + 7
# the proof is explained here
# https://leetcode.com/problems/domino-and-tromino-tiling/solutions/1620809/python-java-c-c-dp-image-visualized-explanation-100-faster-o-n/
class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
        # max length of 3 so that the leftmost val is automatically popped when pushing on a new value
        #   {dp[i - 3], dp[i - 2], dp[i - 1]}
        dp: deque[int] = deque([1, 2, 5], maxlen=3)
        for _ in range(n - 3):  # runs (n - 3) times since we have the 3 base cases
            # formula: dp[i] = 2 * dp[i - 1] + dp[i - 3]
            dp.append(2 * dp[-1] + dp[0])
        return dp[-1] % MOD


# @lc code=end
