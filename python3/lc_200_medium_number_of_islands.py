#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (56.15%)
# Likes:    18064
# Dislikes: 410
# Total Accepted:    2M
# Total Submissions: 3.5M
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and
# '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are all
# surrounded by water.
#
#
# Example 1:
#
#
# Input: grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# Output: 1
#
#
# Example 2:
#
#
# Input: grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# Output: 3
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.
#
#
#

# @lc code=start


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        seen: set[tuple[int, int]] = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        islands = 0

        def conquered_island(row: int, col: int) -> bool:
            if grid[row][col] == "0" or (row, col) in seen:
                return False

            stack: list[tuple[int, int]] = []
            stack.append((row, col))
            while stack:
                cur_row, cur_col = stack.pop()
                seen.add((cur_row, cur_col))
                for row_offset, col_offset in directions:
                    x = cur_row + row_offset
                    y = cur_col + col_offset

                    if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == "0" or (x, y) in seen:
                        continue

                    stack.append((x, y))

            return True

        for row in range(rows):
            for col in range(cols):
                if conquered_island(row, col):
                    islands += 1
        return islands


# @lc code=end


def main() -> None:
    sol = Solution()
    grid = [  #
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]

    ans = sol.numIslands(grid)
    print(ans)


if __name__ == "__main__":
    main()
