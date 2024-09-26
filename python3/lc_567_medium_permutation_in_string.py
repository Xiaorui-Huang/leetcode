#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (43.52%)
# Likes:    8089
# Dislikes: 267
# Total Accepted:    545.7K
# Total Submissions: 1.3M
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, return true if s2 contains a permutation of s1,
# or false otherwise.
#
# In other words, return true if one of s1's permutations is the substring of
# s2.
#
#
# Example 1:
#
#
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
#
#
# Example 2:
#
#
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s1.length, s2.length <= 10^4
# s1 and s2 consist of lowercase English letters.
#
#
#


# @lc code=start
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        key_hole = Counter(s1)
        key: Counter[str] = Counter([])
        n = len(s1)
        pins = left = 0

        for right, ch_right in enumerate(s2):
            if n < right - left + 1:
                ch_left = s2[left]
                if key[ch_left] == key_hole[ch_left]:
                    pins -= 1
                key[ch_left] -= 1
                left += 1

            key[ch_right] += 1
            if key[ch_right] == key_hole[ch_right]:
                pins += 1

            if pins == len(key_hole):
                return True
        return False


# @lc code=end
def main() -> None:
    sol = Solution()
    ans = sol.checkInclusion("abbaio", "adcoibab")
    print(ans)


if __name__ == "__main__":
    main()
