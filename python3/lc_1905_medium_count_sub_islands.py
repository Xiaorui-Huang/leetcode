#
# @lc app=leetcode id=1905 lang=python3
#
# [1905] Count Sub Islands
#
# https://leetcode.com/problems/count-sub-islands/description/
#
# algorithms
# Medium (67.88%)
# Likes:    1509
# Dislikes: 46
# Total Accepted:    56.5K
# Total Submissions: 83.5K
# Testcase Example:  '[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]\n' + '[[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]'
#
# You are given two m x n binary matrices grid1 and grid2 containing only 0's
# (representing water) and 1's (representing land). An island is a group of 1's
# connected 4-directionally (horizontal or vertical). Any cells outside of the
# grid are considered water cells.
#
# An island in grid2 is considered a sub-island if there is an island in grid1
# that contains all the cells that make up this island in grid2.
#
# Return the number of islands in grid2 that are considered sub-islands.
#
#
# Example 1:
#
#
# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]],
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are three sub-islands.
#
#
# Example 2:
#
#
# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]],
# grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid
# on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island.
# There are two sub-islands.
#
#
#
# Constraints:
#
#
# m == grid1.length == grid2.length
# n == grid1[i].length == grid2[i].length
# 1 <= m, n <= 500
# grid1[i][j] and grid2[i][j] are either 0 or 1.
#
#
#

# @lc code=start
LAND = 1
WATER = 0


class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        # determine if island in grid 2 (i2) is a island and record the islands
        # verify with grid1
        rows = len(grid2)
        cols = len(grid2[0])

        def map_the_island(row: int, col: int, cur_map: list[tuple[int, int]]) -> None:
            """Use DFS to map every piece of land of the island"""
            if row < 0 or col < 0 or row >= rows or col >= cols or grid2[row][col] == WATER:
                return None

            cur_map.append((row, col))
            grid2[row][col] = WATER
            map_the_island(row + 1, col, cur_map)
            map_the_island(row - 1, col, cur_map)
            map_the_island(row, col + 1, cur_map)
            map_the_island(row, col - 1, cur_map)

        sub_islands = 0
        for row in range(rows):
            for col in range(cols):
                cur_map: list[tuple[int, int]] = []
                map_the_island(row, col, cur_map)
                map_match = [grid1[x][y] == LAND for x, y in cur_map]
                if map_match and all(map_match):
                    sub_islands += 1
        return sub_islands


# @lc code=end
