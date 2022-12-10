#
# @lc app=leetcode id=1706 lang=python3
#
# [1706] Where Will the Ball Fall
#
# https://leetcode.com/problems/where-will-the-ball-fall/description/
#
# algorithms
# Medium (66.63%)
# Likes:    867
# Dislikes: 65
# Total Accepted:    31.2K
# Total Submissions: 46.8K
# Testcase Example:  '[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]'
#
# You have a 2-D grid of size m x n representing a box, and you have n balls.
# The box is open on the top and bottom sides.
#
# Each cell in the box has a diagonal board spanning two corners of the cell
# that can redirect a ball to the right or to the left.
#
#
# A board that redirects the ball to the right spans the top-left corner to the
# bottom-right corner and is represented in the grid as 1.
# A board that redirects the ball to the left spans the top-right corner to the
# bottom-left corner and is represented in the grid as -1.
#
#
# We drop one ball at the top of each column of the box. Each ball can get
# stuck in the box or fall out of the bottom. A ball gets stuck if it hits a
# "V" shaped pattern between two boards or if a board redirects the ball into
# either wall of the box.
#
# Return an array answer of size n where answer[i] is the column that the ball
# falls out of at the bottom after dropping the ball from the i^th column at
# the top, or -1 if the ball gets stuck in the box.
#
#
# Example 1:
#
#
#
#
# Input: grid =
# [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
# Output: [1,-1,-1,-1,-1]
# Explanation: This example is shown in the photo.
# Ball b0 is dropped at column 0 and falls out of the box at column 1.
# Ball b1 is dropped at column 1 and will get stuck in the box between column 2
# and 3 and row 1.
# Ball b2 is dropped at column 2 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b3 is dropped at column 3 and will get stuck on the box between column 2
# and 3 and row 0.
# Ball b4 is dropped at column 4 and will get stuck on the box between column 2
# and 3 and row 1.
#
#
# Example 2:
#
#
# Input: grid = [[-1]]
# Output: [-1]
# Explanation: The ball gets stuck against the left wall.
#
#
# Example 3:
#
#
# Input: grid =
# [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
# Output: [0,1,2,3,4,-1]
#
#
#
# Constraints:
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# grid[i][j] is 1 or -1.

# @lc code=start
from ast import For

LEFT = -1
RIGHT = 1


# Could also use DFS to solve
class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        cols = len(grid[0])
        dp = [ball_num for ball_num in range(cols)]
        # dp[i] stores the current balls column position

        # Note: columns starts at 0 and rows start at 1, row 0 is the initial
        # position of the balls
        for i in range(rows):  # 1 to rows
            for j in range(cols):

                prev = dp[j]
                # if the ball is stuck then its stuck
                if prev == -1:
                    continue

                # the current column slant direction of ball j at row i
                direction = grid[i][prev]
                cur = prev + direction

                # check if new column is in bound and it needs to have the same
                # slant direction
                if 0 <= cur < cols and grid[i][prev] == grid[i][cur]:
                    dp[j] = cur
                else:
                    dp[j] = -1

        return dp


# @lc code=end
def main() -> None:
    sol = Solution()
    grid = [
        [1, 1, 1, -1, -1],
        [1, 1, 1, -1, -1],
        [-1, -1, -1, 1, 1],
        [1, 1, 1, 1, -1],
        [-1, -1, -1, -1, -1],
        # [1, 1, 1, 1, 1, 1],
        # [-1, -1, -1, -1, -1, -1],
        # [1, 1, 1, 1, 1, 1],
        # [-1, -1, -1, -1, -1, -1],
        # [-1]
    ]
    ans = sol.findBall(grid)
    print(ans)


if __name__ == "__main__":
    main()
