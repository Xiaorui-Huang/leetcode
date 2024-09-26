#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Medium (38.76%)
# Likes:    10796
# Dislikes: 376
# Total Accepted:    785.6K
# Total Submissions: 2M
# Testcase Example:  '[2,3,1,1,4]'
#
# You are given a 0-indexed array of integers nums of length n. You are
# initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from
# index i. In other words, if you are at nums[i], you can jump to any nums[i +
# j] where:
#
#
# 0 <= j <= nums[i] and
# i + j < n
#
#
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are
# generated such that you can reach nums[n - 1].
#
#
# Example 1:
#
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1
# step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
#
#
#


# @lc code=start
class Solution:
    def jump(self, nums: list[int]) -> int:
        # let dp[i] be the min index that can reach i in one jump
        n = len(nums)
        if n == 1:
            return 0
        dp = [-1] * n
        pt = 0
        for i, num in enumerate(nums):
            for j in range(pt, min(i + num + 1, n)):
                dp[j] = i

            if (pt := max(pt, i + num + 1)) >= n:
                break

        # goal = len(nums) - 1
        # while goal != 0:
        #     for i in range(goal):
        pos = n - 1
        jumps = 1
        while (pos := dp[pos]) != 0:
            jumps += 1

        return jumps


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.jump([2, 3, 0, 1, 4])
    print(ans)


if __name__ == "__main__":
    main()
