#
# @lc app=leetcode id=879 lang=python3
#
# [879] Profitable Schemes
#
# https://leetcode.com/problems/profitable-schemes/description/
#
# algorithms
# Hard (40.65%)
# Likes:    1636
# Dislikes: 111
# Total Accepted:    55.5K
# Total Submissions: 112.1K
# Testcase Example:  '5\n3\n[2,2]\n[2,3]'
#
# There is a group of n members, and a list of various crimes they could
# commit. The i^th crime generates a profit[i] and requires group[i] members to
# participate in it. If a member participates in one crime, that member can't
# participate in another crime.
#
# Let's call a profitable scheme any subset of these crimes that generates at
# least minProfit profit, and the total number of members participating in that
# subset of crimes is at most n.
#
# Return the number of schemes that can be chosen. Since the answer may be very
# large, return it modulo 10^9 + 7.
#
#
# Example 1:
#
#
# Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
# Output: 2
# Explanation: To make a profit of at least 3, the group could either commit
# crimes 0 and 1, or just crime 1.
# In total, there are 2 schemes.
#
# Example 2:
#
#
# Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
# Output: 7
# Explanation: To make a profit of at least 5, the group could commit any
# crimes, as long as they commit one.
# There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and
# (0,1,2).
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= minProfit <= 100
# 1 <= group.length <= 100
# 1 <= group[i] <= 100
# profit.length == group.length
# 0 <= profit[i] <= 100
#
#
#

# @lc code=start
"""
Suppose we have taken some crimes from range 0 ≤ j < i , used m
members to execute them, and made a profit of p from them. We used m
members, so n - m are left for future crimes. As we have made a profit of
p already, we need to make at least minProfit - p more
from future crimes. So now,

n = n - m
minProfit = minProfit - p
Let's denote this by f(i , n, minProfit)
"""

from enum import Enum

appr = Enum("approaches", "top_down bottom_up top_down_general")
APPR = appr.bottom_up

MOD = 10**9 + 7


class Solution:
    def profitableSchemes(self, n: int, min_profit: int, group: list[int], profit: list[int]) -> int:
        match APPR:
            case appr.top_down:
                return self.profitableSchemes_top_down(n, min_profit, group, profit)
            case appr.bottom_up:
                return self.profitableSchemes_bottom_up(n, min_profit, group, profit)
            case appr.top_down_general:
                return self.profitableSchemes_top_down_general(n, min_profit, group, profit)
        # Never Reached
        return 0  # type: ignore

    def profitableSchemes_bottom_up(self, n: int, min_profit: int, group: list[int], profit: list[int]) -> int:
        dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]

        # Initializing the base case.
        for members_used in range(n + 1):
            dp[len(group)][members_used][min_profit] = 1

        for pos in range(len(group) - 1, -1, -1):
            for members_used in range(n + 1):
                for cur_profit in range(min_profit + 1):
                    # Ways to get a profitable scheme without this crime.
                    dp[pos][members_used][cur_profit] = dp[pos + 1][members_used][cur_profit]
                    if members_used + group[pos] <= n:
                        # Adding ways to get profitable schemes, including this crime.
                        dp[pos][members_used][cur_profit] = (
                            dp[pos][members_used][cur_profit]
                            + dp[pos + 1][members_used + group[pos]][min(min_profit, cur_profit + profit[pos])]
                        ) % MOD

        return dp[0][0][0]

    def profitableSchemes_top_down(self, n: int, min_profit: int, group: list[int], profit: list[int]) -> int:
        group_len = len(group)

        # since group_len <= 100 and n <= 100, minProfit <= 100
        mem = [[[-1] * (101) for _ in range(101)] for _ in range(101)]

        def scheme(pos: int, members_used: int, cur_profit: int) -> int:
            if pos == group_len:  # processed all the possible crimes
                # return if the crime was profitable
                return int(cur_profit >= min_profit)

            if mem[pos][members_used][cur_profit] != -1:
                return mem[pos][members_used][cur_profit]

            profitable_schemes = scheme(pos + 1, members_used, cur_profit)
            if group[pos] + members_used <= n:
                # we use min() because if cur_profit is more than min_profit, all that matter is min_profit and we can cut down on the possible cases
                profitable_schemes += scheme(
                    pos + 1, members_used + group[pos], min(min_profit, cur_profit + profit[pos])
                )

            mem[pos][members_used][cur_profit] = profitable_schemes % MOD
            return mem[pos][members_used][cur_profit]

        return scheme(0, 0, 0)

    def profitableSchemes_top_down_general(self, n: int, min_profit: int, group: list[int], profit: list[int]) -> int:
        group_len = len(group)
        mem: dict[tuple[int, int, int], int] = {}

        def scheme(pos: int, available_members: int, cur_profit: int) -> int:
            if pos == group_len:
                return int(cur_profit >= min_profit)

            if (pos, available_members, cur_profit) in mem:
                return mem[(pos, available_members, cur_profit)]

            profitable_schemes = scheme(pos + 1, available_members, cur_profit)

            if available_members - group[pos] >= 0:
                profitable_schemes += scheme(pos + 1, available_members - group[pos], cur_profit + profit[pos])

            ret = profitable_schemes % MOD
            mem[(pos, available_members, cur_profit)] = ret
            return ret

        return scheme(0, n, 0)


# @lc code=end
