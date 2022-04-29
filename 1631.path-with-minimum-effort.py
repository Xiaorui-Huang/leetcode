#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#
# https://leetcode.com/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (51.96%)
# Likes:    2449
# Dislikes: 106
# Total Accepted:    84K
# Total Submissions: 158.2K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D
# array of size rows x columns, where heights[row][col] represents the height
# of cell (row, col). You are situated in the top-left cell, (0, 0), and you
# hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,
# 0-indexed). You can move up, down, left, or right, and you wish to find a
# route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the
# bottom-right cell.
#
#
# Example 1:
#
#
#
#
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2
# in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute
# difference is 3.
#
#
# Example 2:
#
#
#
#
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1
# in consecutive cells, which is better than route [1,3,5,3,5].
#
#
# Example 3:
#
#
# Input: heights =
# [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
#
#
#
# Constraints:
#
#
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6
#
#

from typing import List

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_effort = float("inf")
        rows = len(heights)

        if not rows:
            return min_effort
        cols = len(heights[0])

        # backtracking expolores all possible route combination
        def backtrack(i: int, j: int, path_max: int) -> None:
            cur_height = heights[i][j]
            # mark as visited
            heights[i][j] = "#"

            if i == rows - 1 and j == cols - 1:
                nonlocal min_effort
                min_effort = min(min_effort, path_max)

            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + row_offset, j + col_offset

                # skip invalid traversal
                if (
                    row < 0
                    or rows <= row
                    or col < 0
                    or cols <= col
                    or heights[row][col] == "#"
                ):
                    continue

                effort = abs(cur_height - heights[row][col])

                # skip the routes with some effort more than the current min_effort
                if effort < min_effort:
                    backtrack(row, col, max(path_max, effort))
            heights[i][j] = cur_height

        # start at 0, 0 with initial effort of 0
        backtrack(0, 0, 0)
        return min_effort


# @lc code=end


def main():
    sol = Solution()
    matrix = [
        [8, 3, 2, 5, 2, 10, 7, 1, 8, 9],
        [1, 4, 9, 1, 10, 2, 4, 10, 3, 5],
        [4, 10, 10, 3, 6, 1, 3, 9, 8, 8],
        [4, 4, 6, 10, 10, 10, 2, 10, 8, 8],
        [9, 10, 2, 4, 1, 2, 2, 6, 5, 7],
        [2, 9, 2, 6, 1, 4, 7, 6, 10, 9],
        [8, 8, 2, 10, 8, 2, 3, 9, 5, 3],
        [2, 10, 9, 3, 5, 1, 7, 4, 5, 6],
        [2, 3, 9, 2, 5, 10, 2, 7, 1, 8],
        [9, 10, 4, 10, 7, 4, 9, 3, 1, 6],
    ]
    ans = sol.minimumEffortPath(matrix)
    print(ans)


if __name__ == "__main__":
    main()
