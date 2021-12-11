#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (64.47%)
# Likes:    7205
# Dislikes: 431
# Total Accepted:    742.1K
# Total Submissions: 1.1M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image, rotate the image by
# 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[1]]
# Output: [[1]]
# 
# 
# Example 4:
# 
# 
# Input: matrix = [[1,2],[3,4]]
# Output: [[3,1],[4,2]]
# 
# 
# 
# Constraints:
# 
# 
# matrix.length == n
# matrix[i].length == n
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000
# 
# 
#
from typing import List

# @lc code=start
class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(A)
        for i in range(n//2):
            for j in range(n - n//2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                         A[~j][i], A[~i][~j], A[j][~i], A[i][j], 

# @lc code=end

sol = Solution()
A = [[5,1,9,11, 12],[2,4,8,10, 13],[13,3,6,7, 88],[15,14,12,16, 32], [1,2,3,4,5]]
a = sol.rotate(A)
print(A)
