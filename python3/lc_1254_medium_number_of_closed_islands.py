#
# @lc app=leetcode id=1254 lang=python3
#
# [1254] Number of Closed Islands
#
# https://leetcode.com/problems/number-of-closed-islands/description/
#
# algorithms
# Medium (64.21%)
# Likes:    2571
# Dislikes: 59
# Total Accepted:    118.3K
# Total Submissions: 184.3K
# Testcase Example:  '[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]'
#
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island
# totally (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.
#
#
# Example 1:
#
#
#
#
# Input: grid =
# [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
# Output: 2
# Explanation:
# Islands in gray are closed because they are completely surrounded by water
# (group of 1s).
#
# Example 2:
#
#
#
#
# Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
# Output: 1
#
#
# Example 3:
#
#
# Input: grid = [[1,1,1,1,1,1,1],
# [1,0,0,0,0,0,1],
# [1,0,1,1,1,0,1],
# [1,0,1,0,1,0,1],
# [1,0,1,1,1,0,1],
# [1,0,0,0,0,0,1],
# ⁠              [1,1,1,1,1,1,1]]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= grid.length, grid[0].length <= 100
# 0 <= grid[i][j] <=1
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "DFS_classic DFS_fast_modify")
APPR = appr.DFS_classic

LAND = 0
WATER = 1


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        if APPR == appr.DFS_fast_modify:
            return self.closedIsland_DFS_fast_modify(grid)
        if APPR == appr.DFS_classic:
            return self.closedIsland_DFS_classic(grid)
        return 0  # Never Reached

    def closedIsland_DFS_fast_modify(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def is_closed(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= rows or y >= cols:
                return False  # if not surrounded by water
            if grid[x][y] == WATER:
                return True  # this small piece of land is surrounded by water

            grid[x][y] = WATER  # mark as "water" so as to not visit again

            # make sure that all surrounding land are also surrounded by water
            # Note: we need to call is_closed first and on all four connections since we are modifying land to water inside the is_closed() call
            is_surrounded = True
            for x_offset, y_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                is_surrounded = is_closed(x + x_offset, y + y_offset) and is_surrounded
            return is_surrounded

        closed_islands = 0
        for row in range(rows):
            for col in range(cols):
                # only verify land
                if grid[row][col] == LAND and is_closed(row, col):
                    closed_islands += 1
        return closed_islands

    def closedIsland_DFS_classic(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        seen: set[tuple[int, int]] = set()

        def is_closed(x: int, y: int) -> bool:
            if x < 0 or y < 0 or x >= rows or y >= cols:
                return False

            if grid[x][y] == WATER or (x, y) in seen:
                return True

            seen.add((x, y))

            is_surrounded = True
            for x_offset, y_offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                is_surrounded = is_closed(x + x_offset, y + y_offset) and is_surrounded

            return is_surrounded

        closed_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == LAND and (row, col) not in seen and is_closed(row, col):
                    closed_islands += 1
        return closed_islands


# @lc code=end
def main():
    sol = Solution()
    grid = [
        #
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
    ]

    ans = sol.closedIsland(grid)
    print(ans)


if __name__ == "__main__":
    main()
