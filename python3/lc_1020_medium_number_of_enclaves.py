#
# @lc app=leetcode id=1020 lang=python3
#
# [1020] Number of Enclaves
#
# https://leetcode.com/problems/number-of-enclaves/description/
#
# algorithms
# Medium (64.77%)
# Likes:    1933
# Dislikes: 39
# Total Accepted:    84.1K
# Total Submissions: 129.4K
# Testcase Example:  '[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]'
#
# You are given an m x n binary matrix grid, where 0 represents a sea cell and
# 1 represents a land cell.
#
# A move consists of walking from one land cell to another adjacent
# (4-directionally) land cell or walking off the boundary of the grid.
#
# Return the number of land cells in grid for which we cannot walk off the
# boundary of the grid in any number of moves.
#
#
# Example 1:
#
#
# Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 3
# Explanation: There are three 1s that are enclosed by 0s, and one 1 that is
# not enclosed because its on the boundary.
#
#
# Example 2:
#
#
# Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
# Output: 0
# Explanation: All 1s are either on the boundary or can reach the boundary.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 500
# grid[i][j] is either 0 or 1.
#
#
#

# @lc code=start
WATER = 0
LAND = 1


class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def walk(row: int, col: int) -> tuple[bool, int]:
            """return if you walked off the edge of the world and if not walked for how much"""
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return False, 0  # dead

            if grid[row][col] == WATER:
                return True, 0  # touched waaater, but that don't count as effort

            grid[row][col] = WATER  # turn land into water so other slaves can't claim land again

            land_area = 1
            for alive, area in [walk(row + 1, col), walk(row - 1, col), walk(row, col + 1), walk(row, col - 1)]:
                # if you walked off the edge of the world, report that you are dead and you're efforts are useless
                if not alive:
                    return False, 0
                land_area += area
            # yay, you made it out alive! (for now... who knows)
            return True, land_area

        total_area = 0
        for row in range(rows):
            for col in range(cols):
                alive, cur_area = walk(row, col)
                if alive:
                    total_area += cur_area

        return total_area


# @lc code=end
