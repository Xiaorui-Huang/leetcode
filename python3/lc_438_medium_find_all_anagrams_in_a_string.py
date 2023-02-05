#
# @lc app=leetcode id=438 lang=python3
#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Medium (46.78%)
# Likes:    5520
# Dislikes: 222
# Total Accepted:    431.2K
# Total Submissions: 919K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given two strings s and p, return an array of all the start indices of p's
# anagrams in s. You may return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
#
#
# Example 1:
#
#
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
# Example 2:
#
#
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#
#
# Constraints:
#
#
# 1 <= s.length, p.length <= 3 * 10^4
# s and p consist of lowercase English letters.
#
#
#

# @lc code=start
from collections import Counter

from enum import Enum

approaches = Enum("approaches", "NAIVE SLIDING_WINDOW key_hole")
APPROACH = approaches.key_hole


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if APPROACH == approaches.NAIVE:
            return self.findAnagrams_naive(s, p)
        elif APPROACH == approaches.SLIDING_WINDOW:
            return self.findAnagrams_naive(s, p)
        elif APPROACH == approaches.key_hole:
            return self.findAnagrams_key_hole(s, p)
        return []  # never reached

    def findAnagrams_key_hole(self, s: str, p: str) -> list[int]:
        m, n = len(p), len(s)
        if m > n:
            return []

        key_hole = Counter(p)
        key: Counter[str] = Counter([])
        pins = left = 0
        indices = []

        for right, ch_right in enumerate(s):
            # pins leaving the key hole - update the key
            if m < right - left + 1:
                ch_left = s[left]
                if key[ch_left] == key_hole[ch_left]:
                    pins -= 1
                key[ch_left] -= 1
                left += 1

            # new pin for keyhole - update the key
            key[ch_right] += 1
            if key[ch_right] == key_hole[ch_right]:
                pins += 1

            # key hole matched, record it
            if pins == len(key_hole):
                indices.append(left)
        return indices

    def findAnagrams_sliding_window(self, s: str, p: str) -> list[int]:
        m, n = len(p), len(s)
        if m > n:
            return []
        p_count = Counter(p)
        s_count = Counter(s[:m])
        l, r = 0, m - 1
        indices = []
        for i in range(n - m + 1):
            if p_count == s_count:
                indices.append(i)

            if s_count[s[l]] == 1:
                s_count.pop(s[l])
            else:
                s_count[s[l]] -= 1

            s_count[s[r]] = s_count.get(s[r], 0) + 1
            l, r = l + 1, r + 1
        return indices

    def findAnagrams_naive(self, s: str, p: str) -> list[int]:
        """Complexity: O(mn)"""
        indices = []
        n = len(s)
        m = len(p)
        p_count = Counter(p)
        # print(f"p_set: {p_set}")
        for i in range(n - m + 1):
            # print(f"i:{i} -> {Counter(s[i : i + m])}")
            if Counter(s[i : i + m]) == p_count:
                indices.append(i)
        return indices


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.findAnagrams(
        #
        "cbaebabacd",
        "abc",
    )
    print(ans)


if __name__ == "__main__":
    main()
