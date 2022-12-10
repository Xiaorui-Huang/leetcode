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

from enum import Enum

approaches = Enum("approaches", "LC TWO_SEARCH")
APPROACH = approaches.LC


# @lc code=start
class Solution:
    def searchMatrix(self, A: list[list[int]], target: int) -> bool:
        if APPROACH == approaches.LC:
            return self.searchMatrix_lc(A, target)
        elif APPROACH == approaches.TWO_SEARCH:
            return self.searchMatrix_two_search(A, target)
        return False  # never reached

    def searchMatrix_lc(self, A: list[list[int]], target: int) -> bool:
        if not A or target is None:
            return False

        rows, cols = len(A), len(A[0])
        # note high is row * cols - 1
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) // 2
            num = A[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False

    def searchMatrix_two_search(self, A: list[list[int]], target: int) -> bool:
        if not A or not A[0]:
            return False
        rows = len(A)
        cols = len(A[0])

        def binary_row_search(A: list[list[int]], target: int) -> int:
            """Find the appropriate row to binary search next

            Find the highest number that is less than the target
            refer to problem 34
            https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
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

        def binary_search(nums: list[int], target: int) -> bool:
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


def main() -> None:
    sol = Solution()
    ans = sol.searchMatrix(
        # test examples
        [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
        23,
    )
    print(ans)


if __name__ == "__main__":
    main()
