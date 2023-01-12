#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (34.05%)
# Likes:    9684
# Dislikes: 305
# Total Accepted:    628.8K
# Total Submissions: 1.8M
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.
#
# The test cases are generated so that the answer will fit in a 32-bit
# integer.
#
# A subarray is a contiguous subsequence of the array.
#
#
# Example 1:
#
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        min_cur = max_cur = max_prod = 1

        for num in nums:
            if num < 0:
                min_cur, max_cur = max_cur, min_cur

            min_cur = min(num, min_cur * num)
            max_cur = max(num, max_cur * num)

            max_prod = max(max_prod, max_cur)

        return max_prod


# @lc code=end
