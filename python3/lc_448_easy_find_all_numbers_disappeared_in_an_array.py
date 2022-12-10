#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (58.55%)
# Likes:    5902
# Dislikes: 357
# Total Accepted:    515.3K
# Total Submissions: 879.8K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in
# nums.
#
#
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
#
#
# Constraints:
#
#
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= n
#
#
#
# Follow up: Could you do it without extra space and in O(n) runtime? You may
# assume the returned list does not count as extra space.
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "set inplace")
APPR = appr.inplace


class Solution:
    if APPR == appr.set:

        def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
            """make a set of unseen numbers and remove every encounter as we go"""
            missing = set(range(1, 1 + len(nums)))
            for num in nums:
                missing.discard(num)
            return list(missing)

    elif APPR == appr.inplace:

        def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
            """change all encountered number to negative in place and return the indexs of the positive numbers

            2n or O(n) run time
            O(1) space

            93% top tier space solver, 8% slow solver
            """
            for num in nums:
                nums[abs(num) - 1] = -abs(nums[abs(num) - 1])
            return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# @lc code=end
def main() -> None:
    sol = Solution()
    ans = sol.findDisappearedNumbers(
        #
        []
    )
    print(ans)


if __name__ == "__main__":
    main()
