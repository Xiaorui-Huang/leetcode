#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.com/problems/insert-interval/description/
#
# algorithms
# Medium (38.05%)
# Likes:    6767
# Dislikes: 477
# Total Accepted:    665.1K
# Total Submissions: 1.7M
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
#
#
#
# Constraints:
#
#
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
#
#

# @lc code=start

from enum import Enum


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals:
            return [newInterval]

        start, end = newInterval
        if end < intervals[0][0]:
            return [newInterval] + intervals

        def binary_search(target: int) -> int:
            lo, hi = 0, len(intervals) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                val, _ = intervals[mid]
                if val <= target < intervals[mid + 1][0]:
                    return mid
                elif target < val:
                    hi = mid - 1
                else:  # target <= intervals[mid + 1][0]: or larger than the mid + 1's start time
                    lo = mid + 1
            return lo

        start_insert_i, end_insert_i = binary_search(start), binary_search(end)
        interval_start, interval_end = intervals[start_insert_i]

        if interval_end < start:  # after the interval - insert at the next index
            start_insert_i += 1
        else:  # in the interval - overlapping
            start = min(interval_start, start)

        interval_start, interval_end = intervals[end_insert_i]
        if interval_start <= end <= interval_end:  # in the interval - overlapping
            end = interval_end

        res = intervals[:start_insert_i] + [[start, end]] + intervals[end_insert_i + 1 :]
        return res


# @lc code=end


def main() -> None:
    sol = Solution()
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    ans = sol.insert(intervals, newInterval)
    print(ans)


if __name__ == "__main__":
    main()
