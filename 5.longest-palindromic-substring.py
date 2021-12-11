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
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        

        # start index and current length of current longest palindrome
        start, cur_len = 1, 1
        
        # each i acts as a endpoint
        # we go back the current longest lengh amount of character from i
        #  [... odd_s/even_s ...(cur_len)... i ...]
        # we consider two cases:
        # 1) the start is odd
        # 2) the start is even
        # Now check if it's a palendrome, where the centre is at (even_s + i)/2 
        #  
        # 1) odd start we went back further therefore cur_len += 2
        # 2) even start a little less therefore cur_len += 1
        # 
        # Note: jumping back may cause -1 index to we want start >= 0

        for i in range(len(s)):
            odd_s = i - cur_len - 1
            even_s = i - cur_len
            endpoint = i + 1
            odd, even = s[odd_s:endpoint], s[even_s:endpoint]
            if odd_s >= 0 and odd == odd[::-1]:
                start = odd_s
                cur_len += 2
            elif even_s >= 0 and even == even[::-1]:
                start = even_s
                cur_len += 1

        return s[start : start + cur_len]


# ==================== DP =======================
# def longestPalindrome(self, s: str) -> str:
#     if s == s[::-1]:
#         return s

#     n = len(s)

#     dp = [[False] * n for i in range(n)]

#     # handles the base case of a single char palindrome
#     ans = s[0]
#     # Running columns from 1 to n
#     for j in range(1, n):
#         # runnng rows from 0 to j
#         for i in range(0, j):
#             # if base case 2 or 3 character substring or the dp is a palindrome
#             # 2 or 3, since we didn't initialize the 2 char case, so we start at 3 character
#             l = j - i + 1
#             if l <= 3 or dp[i + 1][j - 1]:
#                 # check for the second condition
#                 if s[i] == s[j]:
#                     # Then the dp is true
#                     dp[i][j] = True
#                     # if we have a longer palindrome update
#                     if len(ans) < l:
#                         ans = s[i : j + 1]
#     return ans


s = Solution()
m = s.longestPalindrome("babad")
print(m)

# @lc code=end
