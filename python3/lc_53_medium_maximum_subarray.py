#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Medium (50.11%)
# Likes:    27567
# Dislikes: 1220
# Total Accepted:    3M
# Total Submissions: 5.9M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the subarray with the largest sum, and
# return its sum.
#
#
# Example 1:
#
#
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#
#
# Example 3:
#
#
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: If you have figured out the O(n) solution, try coding another
# solution using the divide and conquer approach, which is more subtle.
#
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        nums_iter = iter(nums)
        max_sum = cur_sum = next(nums_iter)
        for num in nums_iter:
            # basically if adding another continuous number is not contributing to the max_sum, we start anew
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum


# @lc code=end
