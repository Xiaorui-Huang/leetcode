#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (41.18%)
# Likes:    5336
# Dislikes: 236
# Total Accepted:    595.2K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
#
# Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
# Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
#
#
#

from typing import List


# @lc code=start
class Solution:
    def searchMatrix(self, A: List[List[int]], target: int) -> bool:
        if not A or not A[0]:
            return False
        rows = len(A)
        cols = len(A[0])

        def binary_row_search(A: List[List[int]], target: int) -> int:
            """Find the appropriate row to binary search next

            Find the highest number that is less than the target
            refer to problem 33
            """
            up, down = 0, rows - 1
            while up <= down:
                mid = (up + down) // 2
                val = A[mid][0]
                if val <= target:
                    # the ultimate bingo
                    up = mid + 1
                else:
                    down = mid - 1

            return up - 1



        def binary_search(nums: List[int], target: int) -> int:
            left, right = 0, cols - 1
            while left <= right:
                mid = (left + right) // 2
                val = nums[mid]
                if val == target:
                    # the ultimate bingo
                    return True
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        row = binary_row_search(A, target)

        if row >= 0:
            return binary_search(A[row], target)
        return False


# @lc code=end


def main():
    sol = Solution()
    ans = sol.searchMatrix(
        # test examples
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        20,
    )
    print(ans)


if __name__ == "__main__":
    main()
