#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#
# https://leetcode.com/problems/make-sum-divisible-by-p/description/
#
# algorithms
# Medium (29.20%)
# Likes:    2389
# Dislikes: 165
# Total Accepted:    137.8K
# Total Submissions: 348.2K
# Testcase Example:  '[3,1,4,2]\n6'
#
# Given an array of positive integers nums, remove the smallest subarray
# (possibly empty) such that the sum of the remaining elements is divisible by
# p. It is not allowed to remove the whole array.
# 
# Return the length of the smallest subarray that you need to remove, or -1 if
# it's impossible.
# 
# A subarray is defined as a contiguous block of elements in the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,1,4,2], p = 6
# Output: 1
# Explanation: The sum of the elements in nums is 10, which is not divisible by
# 6. We can remove the subarray [4], and the sum of the remaining elements is
# 6, which is divisible by 6.
# 
# 
# Example 2:
# 
# 
# Input: nums = [6,3,5,2], p = 9
# Output: 2
# Explanation: We cannot remove a single element to get a sum divisible by 9.
# The best way is to remove the subarray [5,2], leaving us with [6,3] with sum
# 9.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3], p = 3
# Output: 0
# Explanation: Here the sum is 6. which is already divisible by 3. Thus we do
# not need to remove anything.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= p <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = 0
        total = sum(nums)
            
        target = total % p
        if target == 0:
            return 0
        
        cur_mod_sum = 0
        min_len = len(nums)
        mod_map = {0:-1}

        for i, num in enumerate(nums):
            cur_mod_sum = (cur_mod_sum + num) % p
            needed = (cur_mod_sum - target + p) % p
            
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            mod_map[cur_mod_sum] = i 
            
        if min_len == len(nums):
            return -1
        
        return min_len
            
    
# @lc code=end

