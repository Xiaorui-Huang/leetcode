#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (42.28%)
# Likes:    3252
# Dislikes: 110
# Total Accepted:    135.1K
# Total Submissions: 318.2K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Given an array of integers nums and an integer k, return the number of
# contiguous subarrays where the product of all the elements in the subarray is
# strictly less than k.
#
#
# Example 1:
#
#
# Input: nums = [10,5,2,6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
# Example 2:
#
#
# Input: nums = [1,2,3], k = 0
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
#
#
#

# @lc code=start

from enum import Enum
from math import log
from bisect import bisect_left
from sys import float_info

appr = Enum("approaches", "DP DP_OPT sliding_window log_binary_search")
APPR = appr.sliding_window


# NB 1 <= nums[i] <= 1000
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if APPR == appr.log_binary_search:
            return self.numSubarrayProductLessThanK_log_binary_search(nums, k)
        if APPR == appr.sliding_window:
            return self.numSubarrayProductLessThanK_sliding_window(nums, k)
        if APPR == appr.DP:
            return self.numSubarrayProductLessThanK_DP(nums, k)
        if APPR == appr.DP_OPT:
            return self.numSubarrayProductLessThanK_DP_OPT(nums, k)
        return 0  # never reached

    def numSubarrayProductLessThanK_sliding_window(self, nums: list[int], k: int) -> int:
        count = 0
        prod = 1
        left = 0
        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            count += right - left + 1  # this works since 1 <= nums[i] < 1000
        return count

    def numSubarrayProductLessThanK_log_binary_search(self, nums: list[int], k: int) -> int:
        """
        Note that log(Prod of x's) = Sum(log(x's))
        Therefore question is equivalent to find continuous blocks of subarrays
        such that: (log(nums[i]) + ... + log(nums[j]) < log(k))

        let log_sums[i + 1] = log(nums[0]) + ... + log(nums[i])
        i.e. the number of cumulative sums

        => log_sums[j + 1] - log_nums[i] = log(nums[0]) + ... + log(nums[j]) - {log(nums[0]) + ... + log(nums[i - 1])}
        = log(nums[i]) + ... + log(nums[j])

        For each i, we need to find the largest j, such that log_sums[j + 1] - log_sums[i] < log(k)
        we add the interval length between j and i to the count.
        As the interval is the the number of subarrays valid given i

        Appendix:
        log_sums[j + 1] - log_sums[i] < log(k)
        log_sums[j + 1] < log(k) + log_sums[i]
        """
        # edge case - since log(0) is undefined
        if k == 0:
            return 0  # since nums are positive, so if k is 0 then there is no sub array strictly less than 0
        # Log precessing
        log_k = log(k)
        log_sums: list[float] = [0]
        for num in nums:
            log_sums.append(log_sums[-1] + log(num))

        count = 0
        for i in range(len(log_sums) - 1):
            j_plus_one = (
                bisect_left(
                    log_sums,
                    # i is in terms of log_sums that are excessive, which is one before (i + 1) -> i
                    log_k + log_sums[i],
                    # i + 1 is in terms of log_sums index starting point (from 1 ... end)
                    lo=i + 1,
                    hi=len(log_sums),
                )  # subtract one since bisect returns largest (index + 1) for val < x
                - 1
            )
            count += j_plus_one - i  # j - i + 1
        return count

    # NB Incorrect
    def numSubarrayProductLessThanK_DP(self, nums: list[int], k: int) -> int:
        """return all sub arrays with products less than k

        let dp[i][j] be the product of all nums in nums[i:j]
        then:
            dp[i][j+1] = dp[i][j] * nums[j]
            dp[i][i+1] = nums[i]

        Args:
            nums (list[int]): nums list
            k (int): the upper bound for subarray products

        Returns:
            int: the number of continuous subarray that is less than k
        """
        count = 0
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n + 1):
                # base case
                if j == i + 1:
                    prod = nums[i]
                else:
                    prod = dp[i][j - 1] * nums[j - 1]

                if prod < k:
                    count += 1
                dp[i][j] = prod
        return count

    # NB Incorrect
    def numSubarrayProductLessThanK_DP_OPT(self, nums: list[int], k: int) -> int:
        """DP solution with O(1) space"""
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                # initialize or calculate running sum
                prod: int = nums[i] if j == i + 1 else prod * nums[j - 1]
                # plus one if less than k
                count += int(prod < k)
        return count


# @lc code=end
def main():
    sol = Solution()
    nums = [1, 1, 1]
    k = 1
    nums = [10, 5, 2, 6]
    k = 100
    ans = sol.numSubarrayProductLessThanK(nums, k)
    print(ans)


if __name__ == "__main__":
    main()
