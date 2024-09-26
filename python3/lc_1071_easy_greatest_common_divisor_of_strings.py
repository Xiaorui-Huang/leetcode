#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (51.02%)
# Likes:    2786
# Dislikes: 428
# Total Accepted:    133.9K
# Total Submissions: 240.6K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t
# (i.e., t is concatenated with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x
# divides both str1 and str2.
#
#
# Example 1:
#
#
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
#
#
# Example 2:
#
#
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
#
#
# Example 3:
#
#
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
#
#
#
# Constraints:
#
#
# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.
#
#
#

# @lc code=start
from math import gcd
from enum import Enum

appr = Enum("approaches", "brute_force gcd")
APPR = appr.gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        match APPR:
            case appr.gcd:
                return self.gcdOfStrings_gcd(str1, str2)
            case appr.brute_force:
                return self.gcdOfStrings_brute_force(str1, str2)
        return "" """Never Reached"""  # type: ignore

    def gcdOfStrings_gcd(self, str1: str, str2: str) -> str:
        # quite a elegant and advanced solution:
        # refer to this https://leetcode.com/problems/greatest-common-divisor-of-strings/solutions/3024822/greatest-common-divisor-of-strings/
        # if a common divisor exists then the concatenation regardless of order should be the same string
        if str1 + str2 != str2 + str1:
            return ""

        # if a common divisor exists then, it would be the gcd of the length
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]

    def gcdOfStrings_brute_force(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)

        def valid(length: int) -> bool:
            if len1 % length or len2 % length:
                return False
            n1, n2 = len1 // length, len2 // length
            base = str1[:length]
            return str1 == n1 * base and str2 == n2 * base

        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]

        return ""


# @lc code=end
