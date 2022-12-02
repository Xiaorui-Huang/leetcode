#
# @lc app=leetcode id=994 lang=python3
#
# [994] Rotting Oranges
#
# https://leetcode.com/problems/rotting-oranges/description/
#
# algorithms
# Medium (51.74%)
# Likes:    7218
# Dislikes: 283
# Total Accepted:    420.7K
# Total Submissions: 809.7K
# Testcase Example:  '[[2,1,1],[1,1,0],[0,1,1]]'
#
# You are given an m x n grid where each cell can have one of three
# values:
#
#
# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
#
#
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten
# orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a
# fresh orange. If this is impossible, return -1.
#
#
# Example 1:
#
#
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
#
#
# Example 2:
#
#
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never
# rotten, because rotting only happens 4-directionally.
#
#
# Example 3:
#
#
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer
# is just 0.
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.
#
#
#

# @lc code=start
from collections import deque

EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        locations = self.scan_grid(grid)
        minute = 0

        rotten_count = len(locations["rotten"])
        total = len(locations["fresh"]) + rotten_count

        # multi-source bfs from the rotten oranges

        q = deque(locations["rotten"])  # represent the queue at this minute

        def process_minute(cur_q):
            next_q = deque()  # represent the queue at next minute
            while cur_q:
                x, y = cur_q.popleft()
                for x_offset, y_offset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    row, col = x + x_offset, y + y_offset
                    if row < 0 or row >= rows or col < 0 or col >= cols:
                        continue

                    if grid[row][col] == FRESH:
                        next_q.append((row, col))
                        grid[row][col] = 2
                        nonlocal rotten_count
                        rotten_count += 1
                    # skip if EMPTY or ROTTEN
            return next_q

        q = process_minute(q)
        while q:
            minute += 1  # some other orange has rotten in that minute
            q = process_minute(q)

        if rotten_count == total:
            return minute
        return -1

    def scan_grid(self, grid: list[list[int]]) -> dict[str, list[tuple[int, int]]]:
        """Scan the orange grid and return the location information of empty, fresh and rotten oranges initial location

        Args:
            grid (list[list[int]]): grid of fresh/rotten oranges and empty spaces

        Returns:
            dict[str, list[tuple[int, int]]]: Dictionary containing a list of initial positions for the 3 types of items
        """
        rows = len(grid)
        cols = len(grid[0])
        locations: dict[str, list[tuple[int, int]]] = {"empty": [], "fresh": [], "rotten": []}

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == EMPTY:
                    locations["empty"].append((x, y))
                elif grid[x][y] == FRESH:
                    locations["fresh"].append((x, y))
                else:  # grid[x][y] == 2
                    locations["rotten"].append((x, y))
        return locations


# @lc code=end


def main():
    sol = Solution()
    grid = [
        # [2, 1, 0],
        # [0, 1, 2],
        # [0, 1, 0],
        #
        # [0, 2]
        #
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    ans = sol.orangesRotting(grid)
    print(ans)


if __name__ == "__main__":
    main()
