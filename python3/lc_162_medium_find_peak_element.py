#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# https://leetcode.com/problems/find-peak-element/description/
#
# algorithms
# Medium (45.17%)
# Likes:    4783
# Dislikes: 3315
# Total Accepted:    660.4K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,1]'
#
# A peak element is an element that is strictly greater than its neighbors.
#
# Given an integer array nums, find a peak element, and return its index. If
# the array contains multiple peaks, return the index to any of the peaks.
#
# You may imagine that nums[-1] = nums[n] = -∞.
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index
# number 2.
#
# Example 2:
#
#
# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak
# element is 2, or index number 5 where the peak element is 6.
#
#
# Constraints:
#
#
# 1 <= nums.length <= 1000
# -2^31 <= nums[i] <= 2^31 - 1
# nums[i] != nums[i + 1] for all valid i.
#
#
#


# @lc code=start
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        # strict <, as we maintain a 2 sized search space at least
        while left < right:
            mid = (left + right) // 2

            # sloping downwards
            if nums[mid] > nums[mid + 1]:
                right = mid  # not mid - 1, as we don't know the values of that
            else:  # sloping upwards

                left = mid + 1

        # since we are comparing to the left [mid + 1] we thus return the final left
        return left


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.findPeakElement([1, 2, 1, 3, 5, 6, 4])
    print(ans)


if __name__ == "__main__":
    main()
