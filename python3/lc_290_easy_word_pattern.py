#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (40.43%)
# Likes:    5536
# Dislikes: 632
# Total Accepted:    472.1K
# Total Submissions: 1.1M
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in s.
#
#
# Example 1:
#
#
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
#
#
# Example 2:
#
#
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
#
#
# Example 3:
#
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.
#
#
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mem = {}
        words = s.split()
        seen = set()
        if len(words) != len(pattern):
            return False

        for letter, word in zip(pattern, words):
            if letter not in mem:
                if word in seen:
                    return False
                mem[letter] = word
                seen.add(word)
            elif mem[letter] != word:
                return False

        return True


# @lc code=end
