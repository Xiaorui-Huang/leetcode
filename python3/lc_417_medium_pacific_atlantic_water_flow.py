#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (46.89%)
# Likes:    2854
# Dislikes: 681
# Total Accepted:    157.3K
# Total Submissions: 334.8K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# There is an m x n rectangular island that borders both the Pacific Ocean and
# Atlantic Ocean. The Pacific Ocean touches the island's left and top edges,
# and the Atlantic Ocean touches the island's right and bottom edges.
#
# The island is partitioned into a grid of square cells. You are given an m x n
# integer matrix heights where heights[r][c] represents the height above sea
# level of the cell at coordinate (r, c).
#
# The island receives a lot of rain, and the rain water can flow to neighboring
# cells directly north, south, east, and west if the neighboring cell's height
# is less than or equal to the current cell's height. Water can flow from any
# cell adjacent to an ocean into the ocean.
#
# Return a 2D list of grid coordinates result where result[i] = [ri, ci]
# denotes that rain water can flow from cell (ri, ci) to both the Pacific and
# Atlantic oceans.
#
#
# Example 1:
#
#
# Input: heights =
# [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
#
#
# Example 2:
#
#
# Input: heights = [[2,1],[1,2]]
# Output: [[0,0],[0,1],[1,0],[1,1]]
#
#
#
# Constraints:
#
#
# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 10^5
#
#
#

# @lc code=start

from enum import Enum
from queue import Queue

approaches = Enum("app", "BFS DFS DFS_STACK")
APPROACH = approaches.BFS
APPROACH = approaches.DFS
APPROACH = approaches.DFS_STACK

""" Idea: We are not gods. We can't let it rain and see where the water goes.

But as humans we can search from the beach up the mountains, and only travel to
mountains where water can go down, i.e higher mountains than the current ones.
and if starting from some beach of the pacific and some beach of the atlantic
and ultimately land you on the same mountain then rain fall on that mountian
will go to both oceans """


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[tuple[int, int]]:
        if not heights or not heights[0]:
            return []

        if APPROACH == approaches.BFS:
            return self.pacificAtlantic_BFS(heights)
        elif APPROACH == approaches.DFS:
            return self.pacificAtlantic_DFS(heights)
        elif APPROACH == approaches.DFS_STACK:
            return self.pacificAtlantic_DFS_STACK(heights)
        return [(0, 0)]  # never reached

    def pacificAtlantic_DFS_STACK(self, heights: list[list[int]]) -> list[tuple[int, int]]:
        # initialization of beaches near the ocean to start searching
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific_beaches, atlantic_beaches = [], []

        for i in range(num_cols):
            pacific_beaches.append((0, i))
            atlantic_beaches.append((num_rows - 1, i))

        for i in range(num_rows):
            pacific_beaches.append((i, 0))
            atlantic_beaches.append((i, num_cols - 1))

        def dfs(stack: list[tuple[int, int]]) -> set:
            flowed = set()
            while stack:
                cur = stack.pop()
                flowed.add(cur)

                row, col = cur
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + x, col + y

                    if (
                        next_row < 0
                        or num_rows <= next_row
                        or next_col < 0
                        or num_cols <= next_col
                        or (next_row, next_col) in flowed
                    ):
                        continue
                    if heights[next_row][next_col] >= heights[row][col]:
                        stack.append((next_row, next_col))

            # Note usually the stack implementation should loop through all node
            # that is not visited, in case there are unconected parts of the
            # graph that should be searched. But here we have initialize all the
            # nodes to care about in the stack so we don't need to loop agian.
            return flowed

        pacific_flowed = dfs(pacific_beaches)
        atlantic_flowed = dfs(atlantic_beaches)
        return list(pacific_flowed.intersection(atlantic_flowed))

    def pacificAtlantic_DFS(self, heights: list[list[int]]) -> list[tuple[int, int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])
        pacific_beaches, atlantic_beaches = [], []

        for i in range(num_cols):
            pacific_beaches.append((0, i))
            atlantic_beaches.append((num_rows - 1, i))

        for i in range(num_rows):
            pacific_beaches.append((i, 0))
            atlantic_beaches.append((i, num_cols - 1))

        def dfs(beaches: list[tuple[int, int]]) -> set:
            flowed = set()

            def dfs_util(cur: tuple) -> None:
                flowed.add(cur)
                row, col = cur
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + x, col + y

                    if (
                        next_row < 0
                        or num_rows <= next_row
                        or next_col < 0
                        or num_cols <= next_col
                        or (next_row, next_col) in flowed
                    ):
                        continue
                    if heights[next_row][next_col] >= heights[row][col]:
                        dfs_util((next_row, next_col))

            for beach in beaches:
                if beach not in flowed:
                    dfs_util(beach)

            return flowed

        pacific_flowed = dfs(pacific_beaches)
        atlantic_flowed = dfs(atlantic_beaches)
        return list(pacific_flowed.intersection(atlantic_flowed))

    def pacificAtlantic_BFS(self, heights: list[list[int]]) -> list[tuple[int, int]]:
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific_q: Queue = Queue()
        atlantic_q: Queue = Queue()

        # initializing all the node from the ocean
        for i in range(num_cols):
            pacific_q.put((0, i))
            atlantic_q.put((num_rows - 1, i))

        for i in range(num_rows):
            pacific_q.put((i, 0))
            atlantic_q.put((i, num_cols - 1))

        def bfs(queue: Queue) -> set:
            flowed = set()
            while not queue.empty():
                row, col = queue.get()
                flowed.add((row, col))

                # check for all four directions
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    next_row, next_col = row + x, col + y

                    if (
                        next_row < 0
                        or num_rows <= next_row
                        or next_col < 0
                        or num_cols <= next_col
                        or (next_row, next_col) in flowed
                    ):
                        continue

                    if heights[next_row][next_col] >= heights[row][col]:
                        queue.put((next_row, next_col))
            return flowed

        pacific_flowed = bfs(pacific_q)
        atlantic_flowed = bfs(atlantic_q)

        return list(pacific_flowed.intersection(atlantic_flowed))


def main():
    sol = Solution()
    a = sol.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
    print(a)


if __name__ == "__main__":
    main()
# @lc code=end
