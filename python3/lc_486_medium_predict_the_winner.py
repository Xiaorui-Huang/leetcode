#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (50.81%)
# Likes:    3514
# Dislikes: 171
# Total Accepted:    127.9K
# Total Submissions: 251.6K
# Testcase Example:  '[1,5,2]'
#
# You are given an integer array nums. Two players are playing a game with this
# array: player 1 and player 2.
#
# Player 1 and player 2 take turns, with player 1 starting first. Both players
# start the game with a score of 0. At each turn, the player takes one of the
# numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1])
# which reduces the size of the array by 1. The player adds the chosen number
# to their score. The game ends when there are no more elements in the array.
#
# Return true if Player 1 can win the game. If the scores of both players are
# equal, then player 1 is still the winner, and you should also return true.
# You may assume that both players are playing optimally.
#
#
# Example 1:
#
#
# Input: nums = [1,5,2]
# Output: false
# Explanation: Initially, player 1 can choose between 1 and 2.
# If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If
# player 2 chooses 5, then player 1 will be left with 1 (or 2).
# So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
# Hence, player 1 will never be the winner and you need to return false.
#
#
# Example 2:
#
#
# Input: nums = [1,5,233,7]
# Output: true
# Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose 233.
# Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 20
# 0 <= nums[i] <= 10^7
#
#

# @lc code=start


# let OPT(i, j) be the number of points player 1 is leading player 2 by in subarray nums[i: j]
# OPT(i, j) = max{nums[i] + OPT(i + 1, j), nums[j] + OPT(i, j - 1))
# dependency is down and left... so i = len(nums) ... 0 and j = i + 1 ... len(nums)
# return OPT(0, len(nums)) >= 0

from enum import Enum

appr = Enum("approaches", "DP DP_SPACE")
APPR = appr.DP_SPACE


class Solution:
    def PredictTheWinner(self, nums: list[int]) -> bool:
        if APPR == appr.DP:
            return self.PredictTheWinner_DP(nums)
        elif APPR == appr.DP_SPACE:
            return self.PredictTheWinner_DP_Space(nums)
        return False  # never reached

    def PredictTheWinner_DP_Space(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [0] * n

        for row in range(n - 1, -1, -1):
            dp[row] = nums[row]  # player 1 gets the only score when there is only one number (base case)
            for col in range(row + 1, n):
                # we basically eliminates the row dimension as it gets sequentially replaced
                front_choice = nums[row] - dp[col]
                back_choice = nums[col] - dp[col - 1]
                dp[col] = max(front_choice, back_choice)
        return dp[n - 1] >= 0

    def PredictTheWinner_DP(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for row in range(n - 1, -1, -1):
            dp[row][row] = nums[row]  # player 1 gets the only score when there is only one number (base case)
            for col in range(row + 1, n):
                front_choice = nums[row] - dp[row + 1][col]
                back_choice = nums[col] - dp[row][col - 1]
                dp[row][col] = max(front_choice, back_choice)

        return dp[0][n - 1] >= 0


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.PredictTheWinner([1, 5, 233, 7])
    print(ans)


if __name__ == "__main__":
    main()
