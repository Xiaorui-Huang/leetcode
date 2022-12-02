#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.com/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (58.81%)
# Likes:    8560
# Dislikes: 98
# Total Accepted:    542.6K
# Total Submissions: 922.6K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
#
#
# For example, "ace" is a subsequence of "abcde".
#
#
# A common subsequence of two strings is a subsequence that is common to both
# strings.
#
#
# Example 1:
#
#
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
#
# Example 2:
#
#
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
#
# Example 3:
#
#
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
#
#
# Constraints:
#
#
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
#
#
#

# @lc code=start
from cgitb import text
from enum import Enum
from functools import lru_cache

appr = Enum("approaches", "DP DP_SPACE DP_top_down")
APPR = appr.DP_SPACE


"""
let LCS(i,j) = LCS for s1[0...i] and s2[0...j]

LCS(i,j) = 
        # base cases
        1.  I(s1 == s2)                               , if i = j = 0         
        2.  I(s1[0] in s2[0...1])                     , if i = 0 and j = 1         
        3.  I(s2[0] in s1[0...1])                     , if i = 1 and j = 0

        4.  LCS(i - 1, j - 1) + 1                     , if s[i] == s[j]      
        5.  max{LCS(i, j - 1) + 1, LCS(i - 1, j)      , if s[i] != s[j]      
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if APPR == appr.DP_SPACE:
            return self.longestCommonSubsequence_DP_space(text1, text2)
        if APPR == appr.DP_top_down:
            return self.longestCommonSubsequence_DP_top_down(text1, text2)
        return self.longestCommonSubsequence_DP(text1, text2)

    def longestCommonSubsequence_DP(self, s1: str, s2: str) -> int:
        rows = len(s2)
        cols = len(s1)
        # construct (n + 1) x (m + 1) matrix for bottom up with padding
        LCS = [([0] * (cols + 1)) for _ in range(rows + 1)]

        # take a column and go down by the rows
        for col in range(cols):
            for row in range(rows):
                # base cases is generalized and implemented by python's wrapping and padding

                if s1[col] == s2[row]:
                    # prevent rows from wrapping around
                    LCS[row][col] = LCS[row - 1][col - 1] + 1
                else:
                    top_value = LCS[row - 1][col]
                    left_value = LCS[row][col - 1]
                    LCS[row][col] = max(top_value, left_value)

        return LCS[rows - 1][cols - 1]

    def longestCommonSubsequence_DP_space(self, s1: str, s2: str) -> int:
        cols = len(s1)
        rows = len(s2)

        # Just need two columns to do space optimized bottom up DP
        # with padding
        prev_LCS = [0] * (rows + 1)
        curr_LCS = [0] * (rows + 1)
        for col in range(cols):
            for row in range(rows):
                if s1[col] == s2[row]:
                    # equiv. LCS[row][col] = LCS[row - 1][col - 1] + 1
                    curr_LCS[row] = prev_LCS[row - 1] + 1
                else:
                    # equiv. LCS[row][col] = max(LCS[row - 1][col], LCS[row][col - 1])
                    curr_LCS[row] = max(curr_LCS[row - 1], prev_LCS[row])
            # move over the columns
            prev_LCS = curr_LCS
            curr_LCS = [0] * (rows + 1)

        # use pre_LCS since we move the columns over
        return prev_LCS[rows - 1]

    # i didn't write this shit... it's works the opposite way around...
    # always been told to use bottom up... just need to worry about the structure
    def longestCommonSubsequence_DP_top_down(self, s1: str, s2: str) -> int:
        @lru_cache(maxsize=None)
        def memo_solve(p1: int, p2: int):

            # Base case: If either string is now empty, we can't match
            # up anymore characters.
            if p1 == len(s1) or p2 == len(s2):
                return 0

            # Recursive case 1.
            if s1[p1] == s2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)

            # Recursive case 2.
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))

        return memo_solve(0, 0)


# @lc code=end
def main():
    sol = Solution()
    # s1 = "dknkdizqxkdczafixidorgfcnkrirmhmzqbcfuvojsxwraxe"  # 4,5
    # s2 = "dulixqfgvipenkfubgtyxujixspoxmhgvahqdmzmlyhajerqz"  # 6,7
    s1 = "abcde"
    s2 = "ace"
    ans = sol.longestCommonSubsequence(s1, s2)
    print(ans)


if __name__ == "__main__":
    main()
