#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (39.18%)
# Likes:    9258
# Dislikes: 225
# Total Accepted:    824.2K
# Total Submissions: 2.1M
# Testcase Example:  '[1,2,5]\n11'
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If
# that amount of money cannot be made up by any combination of the coins,
# return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
# Example 1:
#
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Example 3:
#
#
# Input: coins = [1], amount = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= coins.length <= 12
# 1 <= coins[i] <= 2^31 - 1
# 0 <= amount <= 10^4
#
#
#


# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """Return the minimum number of coins used to get the amount using the a given denomination of coins

            With a given amount i, we find the minimum by checking the amount
            that costs for each i - coin amount, find that minimum and +1 for
            using that coin. Lastly store the optimal value for i until we work
            up to amount

            OPT(i) = argmin_coin OPT(i - coin), for coin in coins Conceptually
            this takes amount X len(coins) space. but we can flatten the space
            to O(amount) as we are re-using a lot of previous results

        Args:
            coins (list[int]): denomination of coins
            amount (int): monetary amount needed to make up using coins

        Returns:
            int: the fewest number of coins that you need to make up the amount
        """
        dp = [float("inf")] * (amount + 1)
        # base case a amount of 0 requires 0 coins
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    # take the minimum of itself vs the amount less the coin (+1 for using the coin)
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float("inf") else dp[amount]  # type: ignore


# @lc code=end


def main():
    sol = Solution()
    a = sol.coinChange([2, 5, 10, 1], 27)
    print(a)


if __name__ == "__main__":
    main()
