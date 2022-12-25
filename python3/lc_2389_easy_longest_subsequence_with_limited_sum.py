#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
#
# algorithms
# Easy (65.01%)
# Likes:    613
# Dislikes: 69
# Total Accepted:    36K
# Total Submissions: 53.1K
# Testcase Example:  '[4,5,2,1]\n[3,10,21]'
#
# You are given an integer array nums of length n, and an integer array queries
# of length m.
#
# Return an array answer of length m where answer[i] is the maximum size of a
# subsequence that you can take from nums such that the sum of its elements is
# less than or equal to queries[i].
#
# A subsequence is an array that can be derived from another array by deleting
# some or no elements without changing the order of the remaining elements.
#
#
# Example 1:
#
#
# Input: nums = [4,5,2,1], queries = [3,10,21]
# Output: [2,3,4]
# Explanation: We answer the queries as follows:
# - The subsequence [2,1] has a sum less than or equal to 3. It can be proven
# that 2 is the maximum size of such a subsequence, so answer[0] = 2.
# - The subsequence [4,5,1] has a sum less than or equal to 10. It can be
# proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
# - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be
# proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,3,4,5], queries = [1]
# Output: [0]
# Explanation: The empty subsequence is the only subsequence that has a sum
# less than or equal to 1, so answer[0] = 0.
#
#
# Constraints:
#
#
# n == nums.length
# m == queries.length
# 1 <= n, m <= 1000
# 1 <= nums[i], queries[i] <= 10^6
#
#
#


# @lc code=start
from bisect import bisect


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # we sort the list first to compact all the values together
        # then use prefix sum to binary search on the point of query
        nums.sort()
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        max_subsequences = []
        for query in queries:
            max_subsequences.append(bisect(nums, query))

        return max_subsequences


# @lc code=end
