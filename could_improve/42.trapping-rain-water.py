#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (54.69%)
# Likes:    15421
# Dislikes: 219
# Total Accepted:    955.8K
# Total Submissions: 1.7M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
#
#
# Example 1:
#
#
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
#
#
# Example 2:
#
#
# Input: height = [4,2,0,3,2,5]
# Output: 9
#
#
#
# Constraints:
#
#
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
#
#
#


# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        h = height.index(max(height))
        rain = 0

        # dp[i] = highest side to the left/or right opposite the max height
        dp = [0] * n

        for i in range(h):
            elev = height[i]
            # only need to check left side since we already know the right side
            # is max_h
            left = dp[i]
            if elev < left:
                rain += left - elev  # rain trapped above i
                dp[i + 1] = left
            else:
                dp[i + 1] = elev  # carry over the highest left sides

        for i in range(n - 1, h, -1):
            elev = height[i]
            # only need to check right side since we already know the left side
            # is max_h
            right = dp[i]
            if elev < right:
                rain += right - elev  # rain trapped above i
                dp[i - 1] = right
            else:
                dp[i - 1] = elev  # carry over the highest left sides

        return rain


sol = Solution()
a = sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(a)


# @lc code=end
# Original solution - more intuitive
# def trap(self, height: list[int]) -> int:
#     n = len(height)
#     max_h = max(height)
#     h = height.index(max_h)
#     rain = 0

#     # dp[i] = (a_i, b_i), where
#     # a_i is the highest elevation to the left of i
#     # b_i is the highest elevation to the right of i
#     dp = [[0,0] for _ in range(n)]

#     # Setting a single side of the dp with max_h
#     for i in range(n):
#         if i < h:
#             dp[i][1] = max_h
#         else:
#             dp[i][0] = max_h

#     for i in range(h):
#         elev = height[i]
#         # only need to check left side since we already know the right side
#         # is max_h
#         left = dp[i][0]
#         if elev < left:
#             rain += left - elev # rain trapped above i
#             dp[i + 1][0] = left
#         else:
#             dp[i + 1][0] = elev # carry over the highest left sides

#     for i in range(n - 1, h, -1):
#         elev = height[i]
#         # only need to check right side since we already know the left side
#         # is max_h
#         right = dp[i][1]
#         if elev < right:
#             rain += right - elev # rain trapped above i
#             dp[i - 1][1] = right
#         else:
#             dp[i - 1][1] = elev # carry over the highest left sides

#     return rain
