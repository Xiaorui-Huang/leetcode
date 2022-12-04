#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (71.64%)
# Likes:    8298
# Dislikes: 183
# Total Accepted:    649.3K
# Total Submissions: 905.6K
# Testcase Example:  '[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]'
#
# You are given an m x n binary matrix grid. An island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# The area of an island is the number of cells with a value 1 in the island.
#
# Return the maximum area of an island in grid. If there is no island, return
# 0.
#
#
# Example 1:
#
#
# Input: grid =
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected
# 4-directionally.
#
#
# Example 2:
#
#
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.
#
#
#


# @lc code=start
from enum import Enum

appr = Enum("approaches", "DFS_classic DFS_fast_modify")
APPR = appr.DFS_fast_modify


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if APPR == appr.DFS_classic:
            return self.maxAreaOfIsland_DFS_classic(grid)
        if APPR == appr.DFS_fast_modify:
            return self.maxAreaOfIsland_DFS_fast_modify(grid)
        return 0  # Never Reached

    def maxAreaOfIsland_DFS_fast_modify(self, grid: list[list[int]]) -> int:
        # Note: this method is fast but modifies the input
        big_island, rows, cols = 0, len(grid), len(grid[0])

        def conquer_land(x: int, y: int) -> int:
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0:
                return 0  # "water" -> no area
            grid[x][y] = 0  # mark as "water" (seen)
            return (
                1 + conquer_land(x + 1, y) + conquer_land(x - 1, y) + conquer_land(x, y + 1) + conquer_land(x, y - 1)
            )

        for row in range(rows):
            for col in range(cols):
                big_island = max(big_island, conquer_land(row, col))

        return big_island

    def maxAreaOfIsland_DFS_classic(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen: set[tuple[int, int]] = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def conquered_island(row: int, col: int) -> int:
            if grid[row][col] == 0 or (row, col) in seen:
                return 0

            stack: list[tuple[int, int]] = []
            stack.append((row, col))
            smalll_island = 0
            while stack:
                cur_row, cur_col = stack.pop()
                if (cur_row, cur_col) not in seen:
                    seen.add((cur_row, cur_col))
                    smalll_island += 1

                for row_offset, col_offset in directions:
                    x = cur_row + row_offset
                    y = cur_col + col_offset

                    if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0 or (x, y) in seen:
                        continue

                    stack.append((x, y))

            return smalll_island

        biiig_island = 0
        for row in range(rows):
            for col in range(cols):
                biiig_island = max(biiig_island, conquered_island(row, col))

        return biiig_island


# @lc code=end


def main():
    sol = Solution()
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    ]
    ans = sol.maxAreaOfIsland(grid)
    print(ans)


if __name__ == "__main__":
    main()
