#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (41.47%)
# Likes:    7654
# Dislikes: 857
# Total Accepted:    769.4K
# Total Submissions: 1.8M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
#
# Example 1:
#
#
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
#
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
# Constraints:
#
#
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "recursion dfs count")
# count should basically just traverse in a spiral until the count is done.
APPR = appr.dfs

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if APPR == appr.recursion:
            return self.spiralOrder_recursion(matrix)
        if APPR == appr.dfs:
            return self.spiralOrder_dfs(matrix)

    # using the natural organization of dfs and "momentum" to simulate spiral order
    # does not change direction until it has to 
    def spiralOrder_dfs(self, matrix: List[List[int]]) -> List[int]:
        MARK = "*"
        spiral = []
        rows = len(matrix)
        cols = len(matrix[0])
        
        #             right,  down,   left,     up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        global direction
         
        def dfs(i = 0, j = 0, direction = 0) -> None: 
            spiral.append(matrix[i][j])
            matrix[i][j] = MARK

            for _ in range(len(directions)):
                row_offset, col_offset = directions[direction]
                row = i + row_offset
                col = j + col_offset
                if row < 0 or row >= rows or col < 0  or col >= cols or matrix[row][col] == MARK: 
                    direction = (direction + 1) % len(directions)
                    continue
                dfs(row, col, direction)
        
        dfs()
        return spiral 
        
    def spiralOrder_recursion(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        rows = len(matrix)
        cols = len(matrix[0])

        # go right, down, left, up just before start
        # constrain the border and recurse till base case

        # base cases in order:
        # case 1: col_start > col_end
        # case 2: row_start > row_end
        def traverse_border(row_start, row_end, col_start, col_end) -> None:
            col_width = col_end - col_start
            row_width = row_end - row_start
                
            if col_width < 1 or row_width < 1:
                return

            # left to right (whole row)
            for col in range(col_start, col_end):
                spiral.append(matrix[row_start][col])

            if row_width < 2:
                return

            # top to bottom (column except first element)
            for row in range(row_start + 1, row_end):
                spiral.append(matrix[row][col_end - 1])

            # right to left (row except first element and last element)
            for col in range(col_end - 2, col_start, -1):
                spiral.append(matrix[row_end - 1][col])

            if col_width < 2:
                return
            # bottom to top just before the start
            for row in range(row_end - 1, row_start, -1):
                spiral.append(matrix[row][col_start])

            traverse_border(row_start + 1, row_end - 1, col_start + 1, col_end - 1)

        traverse_border(0, rows, 0, cols)
        return spiral


# @lc code=end


def main():
    sol = Solution()
    matrix = [
        # [1,2,3],
        # [4,5,6],
        # [7,8,9],
        #
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        #
        # [7,2],
        # [9,100],
        # [6,34],
        #
        # [1,2,3],
        # [1,2,3]
    ]
    ans = sol.spiralOrder(matrix)
    print(ans)


if __name__ == "__main__":
    main()
