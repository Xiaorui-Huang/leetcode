#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (55.29%)
# Likes:    1731
# Dislikes: 1148
# Total Accepted:    133.6K
# Total Submissions: 241.6K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# 
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,2,3,1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,2,3,1,4,2]
# Output: 6
# Explanation: 
# The degree is 3 because the element 2 is repeated 3 times.
# So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
# 
# 
# 
# Constraints:
# 
# 
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
# 
# 
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """Return the shortest subarray of <nums> with the same degree

        Args:
            nums (List[int]): List of numbers

        Returns:
            int: len of shortest subarry with the same degree
        """
        left ,right, count = {},{},{}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1
            
        ans = len(nums)
        degree = max(count.values())
        
        for i in count:
            if count[i] == degree:
                ans = min(ans, right[i] - left[i] + 1)
        return ans



        
# @lc code=end

