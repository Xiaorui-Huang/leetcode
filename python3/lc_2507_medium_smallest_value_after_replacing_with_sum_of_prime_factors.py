#
# @lc app=leetcode id=2507 lang=python3
#
# [2507] Smallest Value After Replacing With Sum of Prime Factors
#
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/description/
#
# algorithms
# Medium (47.24%)
# Likes:    157
# Dislikes: 16
# Total Accepted:    12.2K
# Total Submissions: 25.8K
# Testcase Example:  '15'
#
# You are given a positive integer n.
#
# Continuously replace n with the sum of its prime factors.
#
#
# Note that if a prime factor divides n multiple times, it should be included
# in the sum as many times as it divides n.
#
#
# Return the smallest value n will take on.
#
#
# Example 1:
#
#
# Input: n = 15
# Output: 5
# Explanation: Initially, n = 15.
# 15 = 3 * 5, so replace n with 3 + 5 = 8.
# 8 = 2 * 2 * 2, so replace n with 2 + 2 + 2 = 6.
# 6 = 2 * 3, so replace n with 2 + 3 = 5.
# 5 is the smallest value n will take on.
#
#
# Example 2:
#
#
# Input: n = 3
# Output: 3
# Explanation: Initially, n = 3.
# 3 is the smallest value n will take on.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^5
#
#
#

# @lc code=start
class Solution:
    def smallestValue(self, n: int) -> int:
        prime_sum, cur = 0, n
        for div in range(2, n + 1):
            # while loop to handle multiple identical factors
            while cur % div == 0:
                prime_sum += div
                cur //= div
        # base case is when n is a prime -> prime sum equals n
        return prime_sum if prime_sum == n else self.smallestValue(prime_sum)


# @lc code=end
