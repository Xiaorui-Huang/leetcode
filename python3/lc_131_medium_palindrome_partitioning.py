#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (62.91%)
# Likes:    9208
# Dislikes: 299
# Total Accepted:    564.4K
# Total Submissions: 893.8K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
#
#
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
#
#
# Constraints:
#
#
# 1 <= s.length <= 16
# s contains only lowercase English letters.
#
#
#


# @lc code=start
# TODO: understand this this...
class Solution:
    def __init__(self) -> None:
        self.res: list[list[str]] = []

    def partition(self, s: str) -> list[list[str]]:
        self.dfs(s, [])
        return self.res

    def dfs(self, prev_suffix: str, path: list[str]) -> None:
        # base case: the prev_suffix is null so we have finished the search
        if not prev_suffix:
            self.res.append(path)
            return
        # for every possible ending point check the prefix
        for i in range(1, len(prev_suffix) + 1):
            prefix = prev_suffix[:i]
            if self.isPal(prefix):
                # only if prefix is a palindrome, then we keep going and repeat
                # this for the suffix (s[i:]) and record the path
                self.dfs(prev_suffix[i:], path + [prefix])

    def isPal(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


# @lc code=end
