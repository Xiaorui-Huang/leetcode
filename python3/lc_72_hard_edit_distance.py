#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#
# https://leetcode.com/problems/edit-distance/description/
#
# algorithms
# Hard (52.98%)
# Likes:    11200
# Dislikes: 127
# Total Accepted:    585.1K
# Total Submissions: 1.1M
# Testcase Example:  '"horse"\n"ros"'
#
# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
#
# Insert a character
# Delete a character
# Replace a character
#
#
#
# Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
# Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#
# Constraints:
#
#
# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "recursion dp_bottom_up")
APPR = appr.dp_bottom_up


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        match APPR:
            case appr.recursion:
                return self.minDistance_recursion(word1, word2)
            case appr.dp_bottom_up:
                return self.minDistance_dp_bottom_up(word1, word2)
        # Never Reached
        return 0  # type: ignore

    def minDistance_recursion(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0

        def min_dist_at_index(len1: int, len2: int) -> int:
            if len1 == 0:
                return len2
            if len2 == 0:
                return len1

            # compare the char at the last index
            if word1[len1 - 1] != word2[len2 - 1]:
                return (
                    min(
                        min_dist_at_index(len1 - 1, len2),  # deletion operation, word1 deletes, word2 unaffected
                        min_dist_at_index(len1, len2 - 1),  # insertion operation, word1 inserts, move word2
                        min_dist_at_index(len1 - 1, len2 - 1),  # replace operation, replaced, move both
                    )
                    + 1
                )
            return min_dist_at_index(len1 - 1, len2 - 1)

        return min_dist_at_index(len(word1), len(word2))

    def minDistance_dp_bottom_up(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        cols, rows = len(word1), len(word2)
        cur = 0

        dp = [0] * (cols + 1)
        for len2 in range(rows + 1):
            for len1 in range(cols + 1):
                if len2 == 0:
                    dp[len1] = len1
                    continue
                if len1 == 0:
                    cur = len2
                    continue

                prev = cur
                if word1[len1 - 1] != word2[len2 - 1]:
                    cur = min(prev, dp[len1 - 1], dp[len1]) + 1
                else:
                    cur = dp[len1 - 1]

                # override the prev dp value only when it is safe
                dp[len1 - 1] = prev

            # fill in the last dp value when the current row is done
            # (since we only filled the prev dp value during the inner loop)
            dp[cols] = cur
        return dp[-1]


# @lc code=end
