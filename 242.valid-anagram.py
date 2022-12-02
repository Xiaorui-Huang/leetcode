#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (60.40%)
# Likes:    3698
# Dislikes: 192
# Total Accepted:    1M
# Total Submissions: 1.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
#
#
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
#
#
#
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
#
#

# @lc code=start
from enum import Enum

approaches = Enum("approaches", "DICT SORT")
approach = approaches.DICT


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if approach == approaches.DICT:
            return self.anagram_hash(s, t)
        elif approach == approaches.SORT:
            return self.anagram_sort(s, t)
        print("You fucked up the settings")
        return False  # never reached

    def anagram_hash(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def build_hash(s: str) -> dict:
            s_hash: dict[str, int] = {}
            for c in s:
                s_hash[c] = s_hash.get(c, 0) + 1
            return s_hash

        t_hash, s_hash = build_hash(t), build_hash(s)

        for c in s:
            if c not in t_hash or t_hash[c] != s_hash[c]:
                return False
        return True

    def anagram_sort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# @lc code=end

sol = Solution()
a = sol.isAnagram("rat", "cat")
print(a)
