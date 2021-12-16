#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (32.51%)
# Likes:    19474
# Dislikes: 891
# Total Accepted:    2.8M
# Total Submissions: 8.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
# Example 2:
#
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
# Example 3:
#
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
#
#
# Example 4:
#
#
# Input: s = ""
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
#
#
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        leng = 1

        # a dictionary storing the last position we saw the letter
        mem = {}
        # left and right pointer for the shifting window
        l = 0
        for r in range(n):
            cur = s[r]
            
            # if we have seen the letter in our current substirng
            # then move the left pointer the shorten the current substring so there is no duplicates
            if cur in mem and mem[cur] >= l:
                l = mem[cur] + 1

            mem[cur] = r
            leng = max(leng, r - l + 1)
            r += 1

        return leng


# @lc code=end
def main():
    sol = Solution()
    a = sol.lengthOfLongestSubstring("dvdf")
    print(a)


if __name__ == "__main__":
    main()
