#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (39.10%)
# Likes:    8429
# Dislikes: 259
# Total Accepted:    919.7K
# Total Submissions: 2.3M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
#
# If target is not found in the array, return [-1, -1].
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def bs_left(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                # looking for highest number less than target
                if nums[mid] < target:
                    low = mid + 1
                else:
                    # even if they equal, high is set one below
                    high = mid - 1
            return low  # the higher of the two

        def bs_right(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                # looking for the lowest number higher than target
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    # even if they equal, high is set one below
                    high = mid - 1
            return high  # the higher of the two

        low, high = bs_left(nums, target), bs_right(nums, target)
        return [low, high] if low <= high else [-1, -1]


# @lc code=end


def main():
    sol = Solution()
    ans = sol.searchRange(
        # [5, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 10], 8
        # [1,3], 1
        [1, 2, 3],
        1,
    )
    print(ans)


if __name__ == "__main__":
    main()
