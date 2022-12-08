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
        max_len = 0
        # a dictionary storing the last position we saw the letter
        last_pos: dict[str, int] = {}
        # left and right pointer for the shifting window
        left_pt = 0
        for right_pt in range(len(s)):
            char = s[right_pt]

            last_seen: int = last_pos.get(char, -1)  # let -1 indicate not seen

            # if we have seen the letter in our current substring
            # then move the left pointer to shorten the current substring so there is no duplicates
            # use >= since, being equal to the left pointer is still a duplicate and needs to be removed
            if last_seen >= left_pt:
                left_pt = last_seen + 1

            last_pos[char] = right_pt
            max_len = max(max_len, right_pt - left_pt + 1)

        return max_len


# @lc code=end
def main():
    sol = Solution()
    a = sol.lengthOfLongestSubstring("abcabcbb")
    print(a)


if __name__ == "__main__":
    main()
