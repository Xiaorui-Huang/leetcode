#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (45.49%)
# Likes:    2347
# Dislikes: 236
# Total Accepted:    157.2K
# Total Submissions: 343.4K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# Given an array of strings words (without duplicates), return all the
# concatenated words in the given list of words.
#
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
#
#
# Example 1:
#
#
# Input: words =
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#
# Example 2:
#
#
# Input: words = ["cat","dog","catdog"]
# Output: ["catdog"]
#
#
#
# Constraints:
#
#
# 1 <= words.length <= 10^4
# 1 <= words[i].length <= 30
# words[i] consists of only lowercase English letters.
# All the strings of words are unique.
# 1 <= sum(words[i].length) <= 10^5
#
#
#

# @lc code=start
from enum import Enum

# TODO: implement trie approach
appr = Enum("approaches", "DP trie")
APPR = appr.DP


class Solution:
    def findAllConcatenatedWordsInADict(self, words: list[str]) -> list[str]:
        # if APPR == appr.DP:
        return self.findAllConcatenatedWordsInADict_DP(words)

    def findAllConcatenatedWordsInADict_DP(self, words: list[str]) -> list[str]:
        # sort the words so that the shorter primitive words comes first
        words.sort(key=len)
        word_dict = set(words)
        concat = []

        for word in words:
            if self.word_break(word, word_dict):
                concat.append(word)
        return concat

    def word_break(self, s: str, word_dict: set[str]) -> bool:
        """Check if `s` can be broken up by words in `word_dict`

        Args:
            s (str): the string to check
            word_dict (set[str]): list of primitive words

        Returns:
            bool: if `s` can be broken up by words in word_dict
        """
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            prevent_checking_self = i == n
            start = 1 if prevent_checking_self else 0
            dp[i] = any(((dp[j] and s[j:i] in word_dict) for j in range(start, i)))

        return dp[-1]


# @lc code=end


def main():
    sol = Solution()
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    ans = sol.findAllConcatenatedWordsInADict(words)
    print(ans)


if __name__ == "__main__":
    main()
