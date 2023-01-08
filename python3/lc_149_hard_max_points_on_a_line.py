#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (21.90%)
# Likes:    1884
# Dislikes: 272
# Total Accepted:    268.4K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane, return the maximum number of points that lie on the same straight
# line.
#
#
# Example 1:
#
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
#
#
# Example 2:
#
#
# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
#
#
#
# Constraints:
#
#
# 1 <= points.length <= 300
# points[i].length == 2
# -10^4 <= xi, yi <= 10^4
# All the points are unique.
#
#
#

# @lc code=start
from math import atan2
from collections import defaultdict


class Solution:
    def maxPoints(self, points: list[tuple[int, int]]) -> int:
        n = len(points)
        if n == 1:
            return 1
        res = 1
        for i in range(n):
            ax, ay = points[i]
            angles_counts: dict[float, int] = defaultdict(int)
            for j in range(n):
                bx, by = points[j]
                if i != j:
                    angles_counts[atan2(by - ay, bx - ax)] += 1
            res = max(res, max(angles_counts.values()) + 1)
        return res


# @lc code=end
