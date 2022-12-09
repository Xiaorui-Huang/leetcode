#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.59%)
# Likes:    17063
# Dislikes: 891
# Total Accepted:    2.9M
# Total Submissions: 7.1M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for bracket in s:
            if bracket in paren_map:
                stack.append(bracket)
                continue
            if not stack:  # no opening bracket to match closing bracket
                return False
            opening_bracket = stack.pop()
            closing_bracket = paren_map[opening_bracket]
            if bracket != closing_bracket:
                return False

        return len(stack) == 0


# @lc code=end
