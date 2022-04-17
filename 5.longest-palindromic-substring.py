#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (31.51%)
# Likes:    14592
# Dislikes: 855
# Total Accepted:    1.6M
# Total Submissions: 5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
#
#
# Example 1:
#
#
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: s = "cbbd"
# Output: "bb"
#
#
# Example 3:
#
#
# Input: s = "a"
# Output: "a"
#
#
# Example 4:
#
#
# Input: s = "ac"
# Output: "a"
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "CENTER DP")
APPR = appr.DP

class Solution:
    if APPR == appr.CENTER:
        def longestPalindrome(self, s: str) -> str:
            if s == s[::-1]:
                return s
            

            # start index and current length of current longest palindrome
            start, cur_len = 1, 1
            
            # each i acts as a endpoint
            # we go back the current longest length amount of character from i
            #  [... odd_s/even_s ...(cur_len)... i ...]
            #      <------------------------------
            # we consider two cases:
            # 1) the start is odd
            # 2) the start is even
            # Now check if it's a palendrome, where the centre is at (even_s + i)/2 
            #  
            # 1) odd start - we went back further therefore cur_len += 2
            # 2) even start - a little less therefore cur_len += 1
            # 
            # Note: jumping back may cause -1 index to we want start >= 0

            for i in range(len(s)):
                odd_s = i - cur_len - 1
                even_s = i - cur_len
                endpoint = i + 1
                # length of odd: endpoint - odd_s = i + 1 - (i - cur_len - 1) = cur_len + 2
                # length of even: endpoint - even_s = i + 1 - (i - cur_len) = cur_len + 1
                odd, even = s[odd_s:endpoint], s[even_s:endpoint]
                if odd_s >= 0 and odd == odd[::-1]:
                    start = odd_s
                    cur_len += 2
                elif even_s >= 0 and even == even[::-1]:
                    start = even_s
                    cur_len += 1

            return s[start : start + cur_len]
    elif APPR == appr.DP:
        # ==================== DP =======================
        def longestPalindrome(self, s: str) -> str:
            if s == s[::-1]:
                return s

            n = len(s)

            # dp[i][j] === s[i:j+1] is a palentrome
            dp = [[False] * n for i in range(n)]

            # handles the base case of a single char palindrome
            # ans = s[0]
            start_max, end_max = 0, 1
            # Running columns from 1 to n
            for start in range(1, n):
                # runing rows from 0 to j
                for end in range(0, start):
                    # if base case: 2 or 3 character substring or the dp is a palindrome
                    # 2 or 3, since we didn't initialize the 2 char case, so we start at 3 character
                    cur_length = (start + 1) - end 
                    if cur_length <= 3 or dp[end + 1][start - 1]:
                        # check for the second condition
                        if s[start] == s[end]:
                            # Then the dp is true
                            dp[end][start] = True
                            # if we have a longer palindrome update
                            if (end_max - start_max) < cur_length:
                                start_max, end_max = end, start + 1
            return s[start_max: end_max]


s = Solution()
m = s.longestPalindrome("babad")
print(m)

# @lc code=end
