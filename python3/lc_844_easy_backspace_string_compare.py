#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (47.46%)
# Likes:    3316
# Dislikes: 153
# Total Accepted:    359.6K
# Total Submissions: 757.3K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings s and t, return true if they are equal when both are typed
# into empty text editors. '#' means a backspace character.
#
# Note that after backspacing an empty text, the text will continue empty.
#
#
# Example 1:
#
#
# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
#
#
# Example 2:
#
#
# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
#
#
# Example 3:
#
#
# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".
#
#
#
# Constraints:
#
#
# 1 <= s.length, t.length <= 200
# s and t only contain lowercase letters and '#' characters.
#
#
#
# Follow up: Can you solve it in O(n) time and O(1) space?
#
#

# @lc code=start
from enum import Enum

approaches = Enum("approaches", "LAZY_LST POINTERS")
APPROACH = approaches.POINTERS


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        if APPROACH == approaches.LAZY_LST:
            return self.backspaceCompare_lazy_lst(s, t)
        elif APPROACH == approaches.POINTERS:
            return self.backspaceCompare_pointers(s, t)
        return False  # never reached

    def backspaceCompare_pointers(self, s: str, t: str) -> bool:
        i = len(s) - 1  # Traverse from the end of the strings
        j = len(t) - 1

        skipS = 0  # The number of backspaces required till we arrive at a valid character
        skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:  # Ensure that we are comparing a valid character in S
                if s[i] == "#":
                    skipS += 1  # If not a valid character, keep times we must backspace.
                    i = i - 1

                elif skipS > 0:
                    skipS -= 1  # Backspace the number of times calculated in the previous step
                    i = i - 1

                else:
                    break

            while j >= 0:  # Ensure that we are comparing a valid character in T
                if t[j] == "#":
                    skipT += 1  # If not a valid character, keep times we must backspace.
                    j = j - 1

                elif skipT > 0:
                    skipT -= 1  # Backspace the number of times calculated in the previous step
                    j = j - 1

                else:
                    break

            print("Comparing", s[i], t[j])  # Print out the characters for better understanding.

            if i >= 0 and j >= 0 and s[i] != t[j]:  # Compare both valid characters. If not the same, return False.
                return False

            if (i >= 0) != (j >= 0):  # Also ensure that both the character indices are valid. If it is not valid,
                return False  #  it means that we are comparing a "#" with a valid character.

            i = i - 1
            j = j - 1

        return True  # This means both the strings are equivalent.

    def backspaceCompare_lazy_lst(self, s: str, t: str) -> bool:
        def actual_string(s: str):
            char_lst: list = []
            for c in s:
                if c != "#":
                    char_lst.append(c)
                else:
                    char_lst.pop() if char_lst else ""
            return "".join(char_lst)

        return actual_string(s) == actual_string(t)


# @lc code=end
def main():
    sol = Solution()
    ans = sol.backspaceCompare("a#c", "b")
    print(ans)


if __name__ == "__main__":
    main()
