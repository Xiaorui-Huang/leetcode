#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (41.47%)
# Likes:    3522
# Dislikes: 5117
# Total Accepted:    1.2M
# Total Submissions: 3M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
class Solution:
    # use two pointer to achieve O(1) space instead of O(n)
    def isPalindrome(self, s: str) -> bool:
        # convert string to all lower and remove non-alpha characters
        s_new = [letter for letter in s.lower() if letter.isalnum() ]
        n = len(s_new)
        for i in range(n):
            if s_new[i] != s_new[-i - 1]:
                return False
        return True


# @lc code=end
def main():
    sol = Solution()
    s = "0P"
    ans = sol.isPalindrome(s)
    print(ans)


if __name__ == "__main__":
    main()
