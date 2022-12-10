#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (47.46%)
# Likes:    5392
# Dislikes: 358
# Total Accepted:    773.7K
# Total Submissions: 1.6M
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array of length n sorted in ascending order is rotated between 1
# and n times. For example, the array nums = [0,1,2,4,5,6,7] might
# become:
#
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
#
#
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum
# element of this array.
#
# You must write an algorithm that runs in O(log n) time.
#
#
# Example 1:
#
#
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
#
#
# Example 2:
#
#
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4
# times.
#
#
# Example 3:
#
#
# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4
# times.
#
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.
#
#
#

# @lc code=start
from bisect import bisect
from enum import Enum

approaches = Enum("approaches", "BS TRICK")
APPROACH = approaches.TRICK


class Solution:
    if APPROACH == approaches.BS:

        def findMin(self, nums: list[int]) -> int:
            if nums[0] <= nums[-1]:
                return nums[0]
            first = nums[0]

            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                val = nums[mid]
                if val > nums[mid + 1]:
                    # the bingo
                    return nums[mid + 1]
                # we are on the left half, search the right half
                if val >= first:  # need to round up, in the case that the first mid is the min
                    low = mid + 1
                else:  # vice versa
                    high = mid - 1
            return 0  # never reached

    elif APPROACH == approaches.TRICK:

        def findMin(self, nums: list[int]) -> int:
            """Use binary search to find the first number that's less than or equal to the last.

            bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
            Note: key argument is added since 3.10

            Locate the insertion point for x in a to maintain sorted order. The
            parameters lo and hi may be used to specify a subset of the list
            which should be considered; by default the entire list is used. If x
            is already present in a, the insertion point will be before (to the
                    left of) any existing entries. The return value is suitable for use as the first parameter to list.insert() assuming that a is
            already sorted.

            The returned insertion point i partitions the array a into two
            halves so that all(val <= x for val in a[lo : i]) for the left side
            and all(val > x for val in a[i : hi]) for the right side."""
            self.nums = nums
            return nums[bisect(self, False, 0, len(nums))]  # type: ignore

    def __getitem__(self, i: int) -> bool:
        return self.nums[i] <= self.nums[-1]


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.findMin(
        # test examples
        # [4, 5, 6, 7, 0, 1, 2]
        [1]
        # [4, 5, 1, 2, 3]
    )
    print(ans)


if __name__ == "__main__":
    main()
