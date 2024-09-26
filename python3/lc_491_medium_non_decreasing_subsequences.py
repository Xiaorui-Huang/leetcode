#
# @lc app=leetcode id=491 lang=python3
#
# [491] Non-decreasing Subsequences
#
# https://leetcode.com/problems/non-decreasing-subsequences/description/
#
# algorithms
# Medium (52.31%)
# Likes:    2015
# Dislikes: 171
# Total Accepted:    93.9K
# Total Submissions: 175.1K
# Testcase Example:  '[4,6,7,7]'
#
# Given an integer array nums, return all the different possible non-decreasing
# subsequences of the given array with at least two elements. You may return
# the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#
#
# Example 2:
#
#
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 15
# -100 <= nums[i] <= 100
#
#
#


# @lc code=start
from typing import Any


class Solution:
    def findSubsequences(self, nums: list[int]) -> set[tuple[int, ...]]:
        n = len(nums)
        subseq_set: set[tuple[int, ...]] = set()
        cur_sequence: list[int] = []

        def backtracking(index: int) -> None:
            # we have checked all the elements
            if index == n:
                if len(cur_sequence) >= 2:
                    subseq_set.add(tuple(cur_sequence))
                return

            # if we can add it to the increasing subsequence
            num = nums[index]
            if not cur_sequence or cur_sequence[-1] <= num:
                cur_sequence.append(num)
                backtracking(index + 1)
                cur_sequence.pop()  # here is the backtracking

            # if we skip the cur num
            backtracking(index + 1)

        backtracking(0)
        return subseq_set


# @lc code=end
