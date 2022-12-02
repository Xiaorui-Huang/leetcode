#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (30.06%)
# Likes:    14593
# Dislikes: 1403
# Total Accepted:    1.6M
# Total Submissions: 5.4M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an integer array nums, return all the triplets [nums[i], nums[j],
# nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
# nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
#
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:
# Input: nums = []
# Output: []
# Example 3:
# Input: nums = [0]
# Output: []
#
#
# Constraints:
#
#
# 0 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Hashmap 1 pass approach

        There is also two pointer approach, using sorted list

        """
        hashmap: dict[int, int] = {}
        found, dup_val = set(), set()

        # O(n)
        # for i, num in enumerate(nums):
        #     hashmap[num] = i

        # O(n^2)
        for i, val_i in enumerate(nums):
            # skip the iteration if the values already exist, (avoid a bunch of the same number)
            if val_i not in dup_val:
                dup_val.add(val_i)
                for j, val_j in enumerate(nums[i + 1 :]):
                    val_k = -(val_i + val_j)
                    if val_k in hashmap and hashmap[val_k] == i:
                        found.add(tuple(sorted([val_i, val_j, val_k])))
                    hashmap[val_j] = i
        return found  # type: ignore


# @lc code=end


def main():
    sol = Solution()
    ans = sol.threeSum(
        #
        [-1, 0, 1, 2, -1, -4],
        # [0]
    )
    print(ans)


if __name__ == "__main__":
    main()
