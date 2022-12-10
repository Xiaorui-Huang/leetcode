#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (37.10%)
# Likes:    11449
# Dislikes: 796
# Total Accepted:    1.2M
# Total Submissions: 3.4M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
#
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.
#
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
#
#
#


# @lc code=start


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Idea: use a modified binary search to find the smallest element
        (based on the structure of the rotated sorted array)

        then just do normal binary search on the correct half of the rotated
        array
        """
        n = len(nums)
        if not nums:
            return -1
        first = nums[0]

        def binary_search(nums: list[int], left: int, right: int, target: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                val = nums[mid]
                if target == val:
                    return mid
                elif target > val:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        if nums[0] <= nums[-1]:
            return binary_search(nums, 0, n - 1, target)

        # obj: find the smallest index
        left, right = 0, n - 1
        small_pivot = -1
        while left <= right:
            mid = (left + right) // 2
            val = nums[mid]

            # bingo, this value is larger than the next -> the pivot point
            if val > nums[mid + 1]:
                small_pivot = mid + 1
                break

            # we are on the left side, search on the right side
            if val >= first:
                # push the num up first if equal
                left = mid + 1
            else:  # val < k
                # we are on the right side, search on the left side
                right = mid - 1
        if small_pivot == -1:
            return -1  # something is wrong with the input

        # target in the left half
        if target >= first:
            return binary_search(nums, 0, small_pivot - 1, target)
        # target in the right half
        return binary_search(nums, small_pivot, n - 1, target)


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.search(
        # [4, 5, 6, 7, 8, 1, 2, 3],
        # 3,
        # [2, 3, 4, 5, 6, 7, 8, 9, 1],
        # 9,
        # [3, 1],
        # 1,
        [4, 5, 1, 2, 3],
        1,
    )
    print(ans)


if __name__ == "__main__":
    main()
