#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (68.50%)
# Likes:    3324
# Dislikes: 101
# Total Accepted:    174.3K
# Total Submissions: 253.9K
# Testcase Example:  '[[2,1,3],[6,5,4],[7,8,9]]'
#
# Given an n x n array of integers matrix, return the minimum sum of any
# falling path through matrix.
#
# A falling path starts at any element in the first row and chooses the element
# in the next row that is either directly below or diagonally left/right.
# Specifically, the next element from position (row, col) will be (row + 1, col
# - 1), (row + 1, col), or (row + 1, col + 1).
#
#
# Example 1:
#
#
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.
#
#
# Example 2:
#
#
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.
#
#
#
# Constraints:
#
#
# n == matrix.length == matrix[i].length
# 1 <= n <= 100
# -100 <= matrix[i][j] <= 100
#
#
#

# @lc code=start
from typing import TypeAlias


Matrix: TypeAlias = list[list[int]]

# some crazy person made (ahh, it's this Hieroglyphs) 5 different approaches... DFS also could work
# https://leetcode.com/problems/minimum-falling-path-sum/solutions/1369046/python-explanation-visuals-5-approaches-dp-dfs-w-memo-dfs-iterative
class Solution:
    def minFallingPathSum(self, matrix: Matrix) -> int:
        n = len(matrix)
        dp = matrix[0]  # covers the base case
        for i in range(1, n):
            dp_temp = [0] * n
            # the two corners
            dp_temp[0] = min(dp[0], dp[1]) + matrix[i][0]
            dp_temp[-1] = min(dp[-1], dp[-2]) + matrix[i][-1]
            # the middles (from index 1 to n - 2)
            for j in range(1, n - 1):
                dp_temp[j] = min(dp[j - 1], dp[j], dp[j + 1]) + matrix[i][j]
            dp = dp_temp
        return min(dp)


# @lc code=end
