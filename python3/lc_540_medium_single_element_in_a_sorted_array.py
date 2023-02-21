#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (58.44%)
# Likes:    7109
# Dislikes: 117
# Total Accepted:    366.3K
# Total Submissions: 626.6K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
#
#
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """Intuition: since len(nums) is always odd, after a bisect, we choose
        to search the one that is odd"""
        n = len(nums)
        lo, hi = 0, n - 1

        while lo < hi:
            mid = (lo + hi) // 2
            
            # base case when the final range has only three numbers
            if hi - lo == 2:
                if nums[mid] == nums[mid + 1]:
                    return nums[mid - 1]
                return nums[mid + 1]

            if mid % 2 == 1:  # ensure the front partition has even elements
                mid -= 1

            if nums[mid] == nums[mid + 1]:  # the first partition only have doubles
                lo = mid
            else:
                hi = mid

        return nums[lo]

        # lo, hi = 0, len(nums) - 1
        # while lo < hi:
        #     mid = 2 * ((lo + hi) // 4)
        #     if nums[mid] == nums[mid+1]:
        #         lo = mid+2
        #     else:
        #         hi = mid
        # return nums[lo]

# @lc code=end
