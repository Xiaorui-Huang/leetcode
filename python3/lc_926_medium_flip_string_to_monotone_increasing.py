#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (59.59%)
# Likes:    2500
# Dislikes: 111
# Total Accepted:    116.2K
# Total Submissions: 193.8K
# Testcase Example:  '"00110"'
#
# A binary string is monotone increasing if it consists of some number of 0's
# (possibly none), followed by some number of 1's (also possibly none).
#
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or
# from 1 to 0.
#
# Return the minimum number of flips to make s monotone increasing.
#
#
# Example 1:
#
#
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
#
#
# Example 2:
#
#
# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
#
#
# Example 3:
#
#
# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s[i] is either '0' or '1'.
#
#
#


# @lc code=start
from collections import Counter
from enum import Enum

appr = Enum("approaches", "prefix_count linear")
APPR = appr.linear


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        match APPR:
            case appr.linear:
                return self.minFlipsMonoIncr_linear(s)
            case appr.prefix_count:
                return self.minFlipsMonoIncr_prefix_count(s)
        return ""  # type: ignore

    def minFlipsMonoIncr_linear(self, s: str) -> int:
        min_flips = cost = Counter(s)["0"]
        for c in s:
            if c == "0":
                cost -= 1
            else:
                cost += 1
            min_flips = min(min_flips, cost)
        return min_flips

    def minFlipsMonoIncr_prefix_count(self, s: str) -> int:
        n = len(s)
        prefix_counts: list[tuple[int, int]] = [(0, 0)] * n
        for i, c in enumerate(s):
            ones, zeros = prefix_counts[i - 1]
            if c == "1":
                ones += 1
            else:
                zeros += 1
            prefix_counts[i] = (ones, zeros)

        ones_count, zeros_count = prefix_counts[-1]
        min_flips: int = min(ones_count, zeros_count)

        for i, (ones_left, zeros_left) in enumerate(prefix_counts):
            zeros_right = zeros_count - zeros_left
            min_flips = min(min_flips, ones_left + zeros_right)

        return min_flips


# @lc code=end
