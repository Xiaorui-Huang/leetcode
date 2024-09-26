#
# @lc app=leetcode id=2405 lang=python3
#
# [2405] Optimal Partition of String
#
# https://leetcode.com/problems/optimal-partition-of-string/description/
#
# algorithms
# Medium (75.10%)
# Likes:    515
# Dislikes: 23
# Total Accepted:    34.2K
# Total Submissions: 45.5K
# Testcase Example:  '"abacaba"'
#
# Given a string s, partition the string into one or more substrings such that
# the characters in each substring are unique. That is, no letter appears in a
# single substring more than once.
#
# Return the minimum number of substrings in such a partition.
#
# Note that each character should belong to exactly one substring in a
# partition.
#
#
# Example 1:
#
#
# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
#
#
# Example 2:
#
#
# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only English lowercase letters.
#
#
#


# @lc code=start
class Solution:
    def partitionString(self, s: str) -> int:
        parts = 1
        seen: list[bool] = 26 * [False]
        for c in s:
            if seen[pos := ord(c) - ord("a")]:
                seen = 26 * [False]
                parts += 1
            seen[pos] = True
        return parts


# @lc code=end
def main() -> None:
    sol = Solution()
    ans = sol.partitionString("ssssss")
    print(ans)


if __name__ == "__main__":
    main()
