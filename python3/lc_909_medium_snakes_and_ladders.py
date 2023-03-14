#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#
# https://leetcode.com/problems/snakes-and-ladders/description/
#
# algorithms
# Medium (40.87%)
# Likes:    1440
# Dislikes: 389
# Total Accepted:    99.9K
# Total Submissions: 237K
# Testcase Example:  '[[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]'
#
# You are given an n x n integer matrix board where the cells are labeled from
# 1 to n^2 in a Boustrophedon style starting from the bottom left of the board
# (i.e. board[n - 1][0]) and alternating direction each row.
#
# You start on square 1 of the board. In each move, starting from square curr,
# do the following:
#
#
# Choose a destination square next with a label in the range [curr + 1,
# min(curr + 6, n^2)].
#
#
# This choice simulates the result of a standard 6-sided die roll: i.e., there
# are always at most 6 destinations, regardless of the size of the
# board.
#
#
# If next has a snake or ladder, you must move to the destination of that snake
# or ladder. Otherwise, you move to next.
# The game ends when you reach the square n^2.
#
#
# A board square on row r and column c has a snake or ladder if board[r][c] !=
# -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n^2
# do not have a snake or ladder.
#
# Note that you only take a snake or ladder at most once per move. If the
# destination to a snake or ladder is the start of another snake or ladder, you
# do not follow the subsequent snake or ladder.
#
#
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move,
# your destination square is 2. You follow the ladder to square 3, but do not
# follow the subsequent ladder to 4.
#
#
# Return the least number of moves required to reach the square n^2. If it is
# not possible to reach the square, return -1.
#
#
# Example 1:
#
#
# Input: board =
# [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
# Output: 4
# Explanation:
# In the beginning, you start at square 1 (at row 5, column 0).
# You decide to move to square 2 and must take the ladder to square 15.
# You then decide to move to square 17 and must take the snake to square 13.
# You then decide to move to square 14 and must take the ladder to square 35.
# You then decide to move to square 36, ending the game.
# This is the lowest possible number of moves to reach the last square, so
# return 4.
#
#
# Example 2:
#
#
# Input: board = [[-1,-1],[-1,3]]
# Output: 1
#
#
#
# Constraints:
#
#
# n == board.length == board[i].length
# 2 <= n <= 20
# grid[i][j] is either -1 or in the range [1, n^2].
# The squares labeled 1 and n^2 do not have any ladders or snakes.
#
#
#


# @lc code=start
from collections import deque
from math import ceil

NO_JUMP = -1


class Solution:
    """_summary_
    BFS complexity:
        Time: O(n^2)
        Space: O(n^2)

    We run BFS on a graph whose vertices are the board cells, and the edges are
    moves between them. There are n2n^2n 2 vertices and no more than 6n^2=O(n^2)
    edges. The time complexity of BFS is O(|V| + |E|),

    where |V| is the number of vertices and |E| is the number of
    edges. We have |V|=n^2 and |E| < 6 n^2 , thus
    the total time complexity for BFS is O(7n^2) = O(n^2)

    We also spend some time associating each (row, col) with a label, but this
    also costs.

    Space-wise we take n^2 space for visited array"""

    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        n_sq = n * n

        # O(1) per call
        def label2board_val(label: int) -> int:
            """label to board values conversion

            Args:
                label (int): label for the square

            Returns:
                int: the value on the board (-1 or some other label within the board)
            """
            # reverse the order as the label starts at the bottom left
            row = ceil(label / n)
            is_forward = row % 2 == 1
            row = n - row

            # odd row from bottom goes left to right, even goes right to left
            col = label % n
            col = col - 1 if col != 0 else n - 1
            if not is_forward:  # reverse the index if row is even
                col = (n - 1) - col

            return board[row][col]

        visited = [False] * (n_sq + 1)
        visited[1] = True

        q: deque[int] = deque([1])
        steps = 0
        while q:
            for _ in range(len(q)):
                if (cur := q.popleft()) == n_sq:
                    return steps

                for label in range(cur + 1, min(cur + 6, n_sq) + 1):
                    label = label if (jump_label := label2board_val(label)) == -1 else jump_label

                    if not visited[label]:
                        visited[label] = True
                        q.append(label)
            steps += 1

        return steps if visited[n_sq] else -1


# @lc code=end
def main() -> None:
    sol = Solution()
    board = [
        [-1, -1, -1, 135, -1, -1, -1, -1, -1, 185, -1, -1, -1, -1, 105, -1],
        [-1, -1, 92, -1, -1, -1, -1, -1, -1, 201, -1, 118, -1, -1, 183, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 179, -1, -1, -1, -1, -1, -1],
        [-1, 248, -1, -1, -1, -1, -1, -1, -1, 119, -1, -1, -1, -1, -1, 192],
        [-1, -1, 104, -1, -1, -1, -1, -1, -1, -1, 165, -1, -1, 206, 104, -1],
        [145, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 229, -1],
        [-1, -1, 75, 140, -1, -1, -1, -1, -1, -1, -1, -1, 43, -1, 34, -1],
        [-1, -1, -1, -1, -1, -1, 169, -1, -1, -1, -1, -1, -1, 188, -1, -1],
        [-1, -1, -1, -1, -1, -1, 92, -1, 171, -1, -1, -1, -1, -1, -1, 66],
        [-1, -1, -1, 126, -1, -1, 68, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, 109, -1, 86, 28, 228, -1, -1, 144, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 59, -1, -1, -1, -1, -1, 51, -1, -1, -1, 62, -1],
        [-1, 71, -1, -1, -1, 63, -1, -1, -1, -1, -1, -1, 212, -1, -1, -1],
        [-1, -1, -1, -1, 174, -1, 59, -1, -1, -1, -1, -1, -1, 133, -1, -1],
        [-1, -1, 62, -1, 5, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 59, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    ]

    ans = sol.snakesAndLadders(board)
    print(ans)


if __name__ == "__main__":
    main()
