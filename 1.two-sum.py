#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (47.91%)
# Likes:    27366
# Dislikes: 875
# Total Accepted:    5.6M
# Total Submissions: 11.6M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
# You can return the answer in any order.
#
#
# Example 1:
#
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 10^4
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
# Only one valid answer exists.
#
#
#
# Follow-up: Can you come up with an algorithm that is less than O(n^2) time
# complexity?
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """This works without a full hash index since even if the initial value
        that has a compliment didn't return because the later compliment wasn't
        in the hash yet, when we get the compliment laster it will always find
        the previous value that is actually in the hash
        
        Pre-condition: there is exactly one pair of indices that adds to target
        
        Return the pair of indices that adds to up to the target
        """
        hashmap = {}
        for i, num in enumerate(nums):
            # check for complement first otherwise it maybe reusing the same number
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


def main():
    sol = Solution()
    ans = sol.twoSum(
        # [2, 7, 11, 15],
        # 9,
        [3, 2, 4],
        6,
    )
    print(ans)


if __name__ == "__main__":
    main()


# @lc code=end
