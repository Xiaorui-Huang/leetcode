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
        def bs_left(nums: list[int], target: int) -> int:
            """ Return the lowest index of the element == target if target exists
            
            if not, return index to element that is just higher than target
            """

            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                # looking for highest number less than target
                # then shift the index to the right, to get to target if it exists, or the index's nums value that is OVER THE TARGET
                if nums[mid] < target:
                    low = mid + 1
                    # ^ low is what we are tracking
                else:
                    # even if they equal, high is set one below
                    # NB: the number that equals target will be in high if target exists
                    high = mid - 1

            # low - 1 would be the highest number less than target
            # and low would be the lowest number equal to target
            # *if target exists
            
            # intuitively, low is pushed down until low and high crosses (low > high)
            return low 

        def bs_right(nums: list[int], target: int) -> int:
            """ Return the highest index of the element == target if target exists
            
            if not, return index to element that is just lower than target
            """
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                # looking for the lowest number higher than target
                # then shift the index to the left, to get to target if it exists, or the index's nums value that is UNDER THE TARGET
                if nums[mid] <= target:
                    # even if they equal, low is set one above
                    low = mid + 1
                else:
                    high = mid - 1
                    # ^ high is what we are tracking
                    
            
            # high + 1 would be the lowest number higher than target
            # and high would be the highest number equal to target
            # *if target exists
            
            # intuitively, high is pushed up until low and high crosses (low > high)
            return high  

        low, high = bs_left(nums, target), bs_right(nums, target)
        
        # if low > high, that means target is not in nums, since the low and high are crossed
        return [low, high] if low <= high else [-1, -1]


# @lc code=end


def main() -> None:
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
