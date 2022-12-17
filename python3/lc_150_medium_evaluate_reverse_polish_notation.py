#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
#
# algorithms
# Medium (44.19%)
# Likes:    5088
# Dislikes: 825
# Total Accepted:    583.6K
# Total Submissions: 1.3M
# Testcase Example:  '["2","1","+","3","*"]'
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.
#
# Note that division between two integers should truncate toward zero.
#
# It is guaranteed that the given RPN expression is always valid. That means
# the expression would always evaluate to a result, and there will not be any
# division by zero operation.
#
#
# Example 1:
#
#
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
#
#
# Example 2:
#
#
# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
#
#
# Example 3:
#
#
# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22
#
#
#
# Constraints:
#
#
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the
# range [-200, 200].
#
#
#

# @lc code=start
from typing import Callable


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops: dict[str, Callable[[int, int], int]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),  # this instead of a//b, is so that we "truncate the answer towards 0"
        }
        stack: list[int] = []
        for token in tokens:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()

                compute = (ops[token])(first, second)
                stack.append(compute)
        return stack[-1]


# @lc code=end
