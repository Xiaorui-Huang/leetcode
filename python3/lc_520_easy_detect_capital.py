#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (55.56%)
# Likes:    2843
# Dislikes: 419
# Total Accepted:    351K
# Total Submissions: 617.9K
# Testcase Example:  '"USA"'
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
#
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
#
#
# Given a string word, return true if the usage of capitals in it is right.
#
#
# Example 1:
# Input: word = "USA"
# Output: true
# Example 2:
# Input: word = "FlaG"
# Output: false
#
#
# Constraints:
#
#
# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.
#
#
#

# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            return word[1:].islower() or word.isupper()
        else:
            return word.islower()


# @lc code=end
