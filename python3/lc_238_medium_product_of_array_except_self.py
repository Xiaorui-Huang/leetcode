#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (64.66%)
# Likes:    15308
# Dislikes: 864
# Total Accepted:    1.4M
# Total Submissions: 2.2M
# Testcase Example:  '[1,2,3,4]'
#
# Given an integer array nums, return an array answer such that answer[i] is
# equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
# You must write an algorithm that runs in O(n) time and without using the
# division operation.
#
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
# integer.
#
#
#
# Follow up: Can you solve the problem in O(1) extra space complexity? (The
# output array does not count as extra space for space complexity analysis.)
#
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)

        # keeps a prefix-prod and suffix prod
        # and at each index point multiply the prod value to the index
        # note the we do this left to right and right to left simultaneously
        left_prod, right_prod = 1, 1
        res = [1] * n

        # runs from 1, since at i = 0, the other prod is always empty, which
        # still gives an running-prod of 1*1 = 1
        for i in range(1, n):
            # accumulate the value to the left
            left_prod *= nums[i - 1]

            # accumulate the value to the right
            right_prod *= nums[-i]

            # at i
            res[i] *= left_prod

            # at -i - 1 (pos i from right to left)
            res[-i - 1] *= right_prod

        return res


# @lc code=end


def main() -> None:
    sol = Solution()
    arr = [-1, 1, 0, -3, 3]
    ans = sol.productExceptSelf(arr)
    print(ans)


if __name__ == "__main__":
    main()
