#
# @lc app=leetcode id=2707 lang=python3
#
# [2707] Extra Characters in a String
#
# https://leetcode.com/problems/extra-characters-in-a-string/description/
#
# algorithms
# Medium (52.56%)
# Likes:    2398
# Dislikes: 124
# Total Accepted:    141.7K
# Total Submissions: 252.9K
# Testcase Example:  '"leetscode"\n["leet","code","leetcode"]'
#
# You are given a 0-indexed string s and a dictionary of words dictionary. You
# have to break s into one or more non-overlapping substrings such that each
# substring is present in dictionary. There may be some extra characters in s
# which are not present in any of the substrings.
#
# Return the minimum number of extra characters left over if you break up s
# optimally.
#
#
# Example 1:
#
#
# Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
# Output: 1
# Explanation: We can break s in two substrings: "leet" from index 0 to 3 and
# "code" from index 5 to 8. There is only 1 unused character (at index 4), so
# we return 1.
#
#
#
# Example 2:
#
#
# Input: s = "sayhelloworld", dictionary = ["hello","world"]
# Output: 3
# Explanation: We can break s in two substrings: "hello" from index 3 to 7 and
# "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in
# any substring and thus are considered as extra characters. Hence, we return
# 3.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 50
# 1 <= dictionary.length <= 50
# 1 <= dictionary[i].length <= 50
# dictionary[i] and s consists of only lowercase English letters
# dictionary contains distinct words
#
#
#


# @lc code=start
from functools import cache


class Solution:

    def minExtraChar(self, s: str, dictionary: list[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans
            
        return dp(0)


# @lc code=end
