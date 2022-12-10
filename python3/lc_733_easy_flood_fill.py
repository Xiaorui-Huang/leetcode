#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (60.34%)
# Likes:    6058
# Dislikes: 584
# Total Accepted:    610.9K
# Total Submissions: 1M
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.
#
# You are also given three integers sr, sc, and color. You should perform a
# flood fill on the image starting from the pixel image[sr][sc].
#
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of the
# aforementioned pixels with color.
#
# Return the modified image after performing the flood fill.
#
#
# Example 1:
#
#
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1)
# (i.e., the red pixel), all pixels connected by a path of the same color as
# the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected to the starting pixel.
#
#
# Example 2:
#
#
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0, so no changes are made
# to the image.
#
#
#
# Constraints:
#
#
# m == image.length
# n == image[i].length
# 1 <= m, n <= 50
# 0 <= image[i][j], color < 2^16
# 0 <= sr < m
# 0 <= sc < n
#
#
#


# @lc code=start
from collections import deque
from enum import Enum

appr = Enum("approaches", "recursion stack")
APPR = appr.stack


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if APPR == appr.stack:
            return self.floodFill_stack(image, sr, sc, color)
        if APPR == appr.recursion:
            return self.floodFill_recursion(image, sr, sc, color)
        return image  # never reaches

    def floodFill_stack(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        stack: list[tuple[int, int]] = []
        stack.append((sr, sc))
        seen: set[tuple[int, int]] = set()

        source_color = image[sr][sc]
        while len(stack):
            row, col = stack.pop()
            image[row][col] = color
            seen.add((row, col))
            for row_offset, col_offset in directions:
                x = row + row_offset
                y = col + col_offset

                if x < 0 or y < 0 or x >= rows or y >= cols or (x, y) in seen or image[x][y] != source_color:
                    continue

                stack.append((x, y))
        return image

    def floodFill_recursion(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows = len(image)
        cols = len(image[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        source_color = image[sr][sc]
        seen: set[tuple[int, int]] = set()

        def dfs(row: int, col: int) -> None:
            image[row][col] = color
            seen.add((row, col))
            for row_offset, col_offset in directions:
                x = row + row_offset
                y = col + col_offset

                if x < 0 or y < 0 or x >= rows or y >= cols or (x, y) in seen or image[x][y] != source_color:
                    continue
                dfs(x, y)

        dfs(sr, sc)
        return image


# @lc code=end
def main() -> None:
    sol = Solution()
    # grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    sr = 1
    sc = 1
    color = 0
    ans = sol.floodFill(grid, sr, sc, color)
    print(ans)


if __name__ == "__main__":
    main()
