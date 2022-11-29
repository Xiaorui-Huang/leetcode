#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (43.54%)
# Likes:    8834
# Dislikes: 403
# Total Accepted:    938.5K
# Total Submissions: 2.2M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
#
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
#
#
#

from enum import Enum
from typing import List

approaches = Enum("approaches", "DP DP_TRIE")
APPROACH = approaches.DP_TRIE


# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if APPROACH == approaches.DP:
            return self.wordBreak_DP(s, wordDict)
        elif APPROACH == approaches.DP_TRIE:
            return self.wordBreak_trie(s, wordDict)

    def wordBreak_DP(self, s: str, wordDict: List[str]) -> bool:
        """
        Idea: define dp[i] as if we can separate string s[:1]
        dp[i] = dp[j] and remaining string is in wordDict; for some j, 0 <= j < i
        dp[0] = True; trivially true a empty string can be separated always
        """
        dp = [True]
        for i in range(1, len(s) + 1):
            dp.append(
                any((dp[j] and (s[j:i] in wordDict) for j in range(i)))  # using a generator instead to save memory
            )  # basically dp[i] = True if any combination of split before i are valid

        return dp[-1]

    def wordBreak_trie(self, s: str, wordDict: List[str]) -> bool:
        """Idea: Same ideas as pure DP, but we change how we loop up a match of
        substring and a word in wordDict

        Complexity: O(len(s) * max len of word inf wordDict) + O(sum of word len in wordDict)

        """
        # construct a regular trie from all the words
        trie = {}

        for w in wordDict:
            root = trie

            for c in w:
                root = root.setdefault(c, {})

            root[None] = None  # use None *key* as end of word marker

        # set up base case with dp, from end to beginning of word;
        # for a word to match a part of s, we require that the start
        # of the next word was a successful True match in dp.
        # so, we start with an additional True value at end of dp,
        # so when we begin by matching a word to the end of s,
        # the "next word after" is True as a base case
        dp = [False] * len(s) + [True]

        # do dp in reverse
        for i in range(len(s) - 1, -1, -1):
            if s[i] in trie:
                # we can start matching our trie with char at position i
                root = trie
                j = i  # j is a separate iterator for the word match

                # loop through characters in s while they
                # are also present in the trie
                while j < len(s) and s[j] in root:
                    root = root[s[j]]

                    # if at any point we jump to a matching character,
                    # and that character marks the end of the word (None in root),
                    # and the following character in dp marks the start of
                    # a successful word (dp[j+1] == True), then we can mark the
                    # start of the current word at position i as True and be done;
                    # we just need to set this word at i once, so we don't
                    # need to continue looping
                    if None in root and dp[j + 1]:
                        dp[i] = 1
                        break

                    j += 1

        # returns if we can match words from end to beginning of s
        return dp[0]


# @lc code=end


def main():
    sol = Solution()
    ans = sol.wordBreak("applepenapple", ["apple", "pen"])
    print(ans)


if __name__ == "__main__":
    main()
