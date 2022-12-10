#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval list Intersections
#
# https://leetcode.com/problems/interval-list-intersections/description/
#
# algorithms
# Medium (70.45%)
# Likes:    3646
# Dislikes: 78
# Total Accepted:    258.2K
# Total Submissions: 366K
# Testcase Example:  '[[0,2],[5,10],[13,23],[24,25]]\n[[1,5],[8,12],[15,24],[25,26]]'
#
# You are given two lists of closed intervals, firstlist and secondlist, where
# firstlist[i] = [starti, endi] and secondlist[j] = [startj, endj]. Each list
# of intervals is pairwise disjoint and in sorted order.
#
# Return the intersection of these two interval lists.
#
# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with
# a <= x <= b.
#
# The intersection of two closed intervals is a set of real numbers that are
# either empty or represented as a closed interval. For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].
#
#
# Example 1:
#
#
# Input: firstlist = [[0,2],[5,10],[13,23],[24,25]], secondlist =
# [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
#
# Example 2:
#
#
# Input: firstlist = [[1,3],[5,9]], secondlist = []
# Output: []
#
#
#
# Constraints:
#
#
# 0 <= firstlist.length, secondlist.length <= 1000
# firstlist.length + secondlist.length >= 1
# 0 <= starti < endi <= 10^9
# endi < starti+1
# 0 <= startj < endj <= 10^9
# endj < startj+1
#
#
#

# @lc code=start
class Solution:
    def intervalIntersection(self, firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:
        """The interval with the smallest end will match to at most 1 interval in the
        other list since they are disjoint, so we compare from first to last,
        get the intersection between two interval and discard the former one
        """
        intersect = []
        i, j = 0, 0
        while i < len(firstlist) and j < len(secondlist):
            si, ei = firstlist[i]
            sj, ej = secondlist[j]

            # smallest end point is discarded
            if min(ei, ej) == ei:
                i += 1
            else:
                j += 1

            s, e = max(si, sj), min(ei, ej)
            if s > e:
                continue
            intersect.append([s, e])

        return intersect


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.intervalIntersection(
        #
        # [[0, 2], [5, 10], [13, 23], [24, 25]],
        # [[1, 5], [8, 12], [15, 24], [25, 26]],
        # [[8, 15]],
        # [[2, 6], [8, 10], [12, 20]],
        [[3, 5], [9, 20]],
        [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]],
    )
    print(ans)


if __name__ == "__main__":
    main()
