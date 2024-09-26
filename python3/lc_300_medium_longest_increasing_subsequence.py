#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (51.77%)
# Likes:    16362
# Dislikes: 302
# Total Accepted:    1.1M
# Total Submissions: 2.2M
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an integer array nums, return the length of the longest strictly
# increasing subsequence.
#
#
# Example 1:
#
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 2500
# -10^4 <= nums[i] <= 10^4
#
#
#
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time
# complexity?
#
#


# @lc code=start
from bisect import bisect_left
from enum import Enum

appr = Enum("approaches", "binary_search dp")
APPR = appr.dp


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        match APPR:
            case appr.dp:
                return self.lengthOfLIS_dp(nums)
            case appr.binary_search:
                return self.lengthOfLIS_binary_search(nums)
        # Never Reached
        return 0  # type: ignore

    # O(n^2)
    def lengthOfLIS_dp(self, nums: list[int]) -> int:
        # initialize to 1, since all subsequence is at least a length of 1
        dp = [1] * len(nums)

        sequence_len = 0
        for i, num in enumerate(nums):
            for j in range(i):
                prev = nums[j]
                if prev < num:
                    dp[i] = max(dp[i], 1 + dp[j])

            sequence_len = max(sequence_len, dp[i])
        return sequence_len

    # O(n log n)
    def lengthOfLIS_binary_search(self, nums: list[int]) -> int:
        # ****NOTE: For simplicity of analysis, dp is 1-indexed, but the
        # actual code will use a 0-indexed array****
        #
        # We define array dp where dp[i] is the minimum of
        # the rightmost (largest) elements of all LIS of length i
        # we've encountered so far
        #
        # Claim: dp is sorted in strictly increasing order
        #
        # Proof: Suppose not. Then there exists an LIS of length j, which
        # we shall denote LIS_j, and an LIS of length k, which we denote LIS_k,
        # where k < j, but dp[k] >= dp[j].
        # We know that LIS_j contains in itself an LIS of length k (LIS_j[:k]),
        # and LIS_j[k] < LIS_j[j], by definition of LIS.
        # By definition of dp, dp[k] = LIS_k[k] <= LIS_j[k]
        # Then, dp[k] < LIS_j[j] = dp[j], and we've arrived at a contradiction
        dp: list[int] = []
        for num in nums:
            # If num > all values in dp, append it to dp
            # Otherwise, binary search dp for num and replace the next larger
            # (or equal) number in dp with it
            #
            # This works because, suppose we are going to replace dp[i].
            # If i is 1 this is trivial: num itself forms an LIS of length 1.
            # Otherwise, we know dp[i-1] = LIS_(i-1)[i-1] < num. Thus we can form
            # an LIS of length i by adding num to LIS_(i-1).
            # With the knowledge that we've formed a new length-i LIS with rightmost
            # element being num, combined with the fact that num < dp[i] by the
            # binary search, we'll need to replace dp[i] with num to maintain
            # the invariant of dp.
            if not dp or num > dp[-1]:
                dp.append(num)
            else:
                i = bisect_left(dp, num)
                dp[i] = num

        # By the invariant, len(dp) is the length of longest subsequence
        return len(dp)


# @lc code=end
