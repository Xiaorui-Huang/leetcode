#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (58.70%)
# Likes:    7323
# Dislikes: 270
# Total Accepted:    804.4K
# Total Submissions: 1.4M
# Testcase Example:  '3\n7'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Example 1:
#
#
# Input: m = 3, n = 7
# Output: 28
#
#
# Example 2:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#
#
# Example 3:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#
# Example 4:
#
#
# Input: m = 3, n = 3
# Output: 6
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10^9.
#
#
#

# @lc code=start
from enum import Enum
approaches = Enum('Approaches', 'RECURSION NAIVE_DP DP')
approach = approaches.DP
class Solution:
    # ===== recursion ====
    def uniquePaths(self, m: int, n: int) -> int:
        if approach == approaches.RECURSION:
            if m == 1 or n == 1:
                return 1

            # go right - one less columns
            right_paths = self.uniquePaths(m, n - 1)

            # go down - one less row
            left_paths = self.uniquePaths(m - 1, n)
            return right_paths + left_paths

    # ====== naive bottom up dp =========
    # handles edge cases when there is a straight path, but loop doesn't run
    # or just change the dp to all 1 instead of 0
        elif approach == approaches.NAIVE_DP:
            if m == 1 or n == 1:
                return 1
            dp = [[1] * n for _ in range(m)]

            for j in range(n - 2, -1, -1):
                for i in range(m - 2, -1, -1):
                    # base cases - when there is a straight path, or on the perimiter
                    if j == n - 2:
                        dp[i][n - 1] = 1
                    if i == m - 2:
                        dp[m - 1][j] = 1

                    dp[i][j] = dp[i][j + 1] + dp[i + 1][j]

            return dp[0][0]

    # ====== linear space bottom up dp =========
    # Note: constant space with dp is not possible... I tried
        elif approach == approaches.DP:
            if m == 1 or n == 1:
                return 1

            # handles base case, by setting everything to 1 initially
            dp = [[1, 1] for _ in range(m)]

            for j in range(n - 2, -1, -1):
                for i in range(m - 2, -1, -1):

                    dp[i][0] = dp[i][1] + dp[i + 1][0]
                # swaps the two columns of dp...
                for row in dp:
                    row[0], row[1] = row[1], row[0]

            # usually its dp[0][0], but because of the column swap its dp[0][1]
            return dp[0][1]


# @lc code=end

sol = Solution()
a = sol.uniquePaths(3, 3)
print(a)
