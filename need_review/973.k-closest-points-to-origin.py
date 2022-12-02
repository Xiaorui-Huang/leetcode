#
# @lc app=leetcode id=973 lang=python3
#
# [973] K Closest Points to Origin
#
# https://leetcode.com/problems/k-closest-points-to-origin/description/
#
# algorithms
# Medium (65.74%)
# Likes:    4625
# Dislikes: 188
# Total Accepted:    641.1K
# Total Submissions: 970.8K
# Testcase Example:  '[[1,3],[-2,2]]\n1'
#
# Given an array of points where points[i] = [xi, yi] represents a point on the
# X-Y plane and an integer k, return the k closest points to the origin (0,
# 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance
# (i.e., √(x1 - x2)^2 + (y1 - y2)^2).
#
# You may return the answer in any order. The answer is guaranteed to be unique
# (except for the order that it is in).
#
#
# Example 1:
#
#
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just
# [[-2,2]].
#
#
# Example 2:
#
#
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.
#
#
#
# Constraints:
#
#
# 1 <= k <= points.length <= 10^4
# -10^4 < xi, yi < 10^4
#
#
#

# @lc code=start
from numpy.linalg import norm
import heapq

from enum import Enum

approaches = Enum("approaches", "ONELINER MINHEAP")
APPROACH = approaches.MINHEAP

heap = list[tuple[int, int, int]]


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        if APPROACH == approaches.MINHEAP:
            max_heap: heap = []
            for x, y in points:
                dist = -(x * x + y * y)
                if len(max_heap) == k:
                    heapq.heappushpop(max_heap, (dist, x, y))
                else:
                    heapq.heappush(max_heap, (dist, x, y))
            return [[x, y] for _, x, y in max_heap]
        elif APPROACH == approaches.ONELINER:
            return heapq.nsmallest(k, points, key=lambda point: norm(point))
        return [[]]  # never reached

    # @lc code=end


def main():
    sol = Solution()
    ans = sol.kClosest(
        #
        # [[3, 3], [5, -1], [-2, 4]],
        # 2,
        # [[1, 0], [0, 1]],
        # 2,
        [
            [68, 97],
            [34, -84],
            [60, 100],
            [2, 31],
            [-27, -38],
            [-73, -74],
            [-55, -39],
            [62, 91],
            [62, 92],
            [-57, -67],
        ],
        5,
    )
    print(ans)


if __name__ == "__main__":
    main()
