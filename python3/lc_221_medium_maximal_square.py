#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (41.61%)
# Likes:    5924
# Dislikes: 130
# Total Accepted:    421.4K
# Total Submissions: 1M
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given an m x n binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
#
#
# Example 1:
#
#
# Input: matrix =
# [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
#
#
# Example 2:
#
#
# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
#
#
# Example 3:
#
#
# Input: matrix = [["0"]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 300
# matrix[i][j] is '0' or '1'.
#
#
#

# @lc code=start
from enum import Enum

approaches = Enum("approaches", "DP DP_OPT")
APPROACH = approaches.DP


class Solution:
    # Don't fully understand especially the dp[j] = 0 part
    def maximalSquare(self, A: list[list[str]]) -> int:
        if APPROACH == approaches.DP:
            return self.maximalSquare_DP(A)
        elif APPROACH == approaches.DP_OPT:
            return self.maximalSquare_DP_OPT(A)
        return 0  # never reached

    def maximalSquare_DP(self, A: list[list[str]]) -> int:
        # if not A or not A[0]:
        #     return 0

        m = len(A)
        n = len(A[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        size = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    size = max(size, dp[i][j])
        return size**2

    def maximalSquare_DP_OPT(self, A: list[list[str]]) -> int:

        if not A or not A[0]:
            return 0
        rows = len(A)
        cols = len(A[0])
        size = 0
        prev = 0  # the old value of dp[j-1]

        dp = [0] * (cols + 1)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if A[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    size = max(size, dp[j])
                # reset to 0, since in the original question, we ignore such
                # value, but here we are reusing values
                else:
                    dp[j] = 0

                prev = temp
        return size**2


# @lc code=end


def main():
    pass


if __name__ == "__main__":
    main()
