#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (53.23%)
# Likes:    13002
# Dislikes: 820
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
# the x-axis forms a container, such that the container contains the most
# water.
#
# Notice that you may not slant the container.
#
#
# Example 1:
#
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
#
#
# Example 2:
#
#
# Input: height = [1,1]
# Output: 1
#
#
# Example 3:
#
#
# Input: height = [4,3,2,1,4]
# Output: 16
#
#
# Example 4:
#
#
# Input: height = [1,2,1]
# Output: 2
#
#
#
# Constraints:
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        width = r
        area = 0

        # intuitive logic: move the side of the bar that is short
        # while l < r:
        #     area = max(area, min(height[l], height[r]) * w)
        #     if height[l] > height[r]:
        #         r -= 1
        #     else:
        #         l += 1
        #     w -= 1

        # Optimization run reverse loop on w
        for w in range(width, 0, -1):
            if height[l] > height[r]:
                area = max(area, height[r] * w)
                r -= 1
            else:
                area = max(area, height[l] * w)
                l += 1
        return area


# @lc code=end
s = Solution()
a = s.maxArea([1, 3, 2, 5, 25, 24, 5])

print(a)
