#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (36.97%)
# Likes:    9089
# Dislikes: 534
# Total Accepted:    841.3K
# Total Submissions: 2.3M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given an integer array nums. You are initially positioned at the
# array's first index, and each element in the array represents your maximum
# jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
#
#
#

# @lc code=start
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Return if we can jump to the last index from the first index given
        the max jump length at each index

        Idea: Using Dynamic Programming define:
            DP[i] = Furthest index we can reach given at index i
            
            Then DP(i) = max[DP(i - 1), i + nums[i]]
            Base case: DP[0] = 0
            Final Result: DP[len(nums)] > len(nums) - 1 i.e. the last index
            
            Conceptually requires linear space, but we can use constant space
            (bottom up \w for loop)

        Args:
            nums (List[int]): Max jump distance at each index

        Returns:
            bool: if we can reach the last index
        """
        # equivalent to DP[0] = 0
        dp = 0
        for i, num in enumerate(nums):
            dp = max(dp, i + num)
            
            # we can already reach the end (this is checked first as that is the
            # YES exit condition)

            if dp >= len(nums) - 1: 
                return True
            
            # if cannot go any furthur at index i (the furthest index we can
            # reach is itself then False)
            if dp == i:
                return False

        return True

# @lc code=end

def main():
    sol = Solution()
    ans = sol.canJump([0])
    print(ans)


if __name__ == "__main__":
    main()