#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (51.72%)
# Likes:    1590
# Dislikes: 343
# Total Accepted:    96.8K
# Total Submissions: 162K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' + '[[],[1],[],[3],[],[7],[],[2],[],[6],[]]'
#
# Given a data stream input of non-negative integers a1, a2, ..., an, summarize
# the numbers seen so far as a list of disjoint intervals.
#
# Implement the SummaryRanges class:
#
#
# SummaryRanges() Initializes the object with an empty stream.
# void addNum(int value) Adds the integer value to the stream.
# int[][] getIntervals() Returns a summary of the integers in the stream
# currently as a list of disjoint intervals [starti, endi]. The answer should
# be sorted by starti.
#
#
#
# Example 1:
#
#
# Input
# ["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals",
# "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
# [[], [1], [], [3], [], [7], [], [2], [], [6], []]
# Output
# [null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7,
# 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]
#
# Explanation
# SummaryRanges summaryRanges = new SummaryRanges();
# summaryRanges.addNum(1);      // arr = [1]
# summaryRanges.getIntervals(); // return [[1, 1]]
# summaryRanges.addNum(3);      // arr = [1, 3]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      // arr = [1, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
# summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]
#
#
#
# Constraints:
#
#
# 0 <= value <= 10^4
# At most 3 * 10^4 calls will be made to addNum and getIntervals.
#
#
#
# Follow up: What if there are lots of merges and the number of disjoint
# intervals is small compared to the size of the data stream?
#
#


# @lc code=start
from bisect import insort, bisect


class SummaryRanges:
    def __init__(self) -> None:
        self.seen: set[int] = set()
        self.intervals: list[list[int]] = []
        self.key = lambda lst: lst[0]

    def addNum(self, value: int) -> None:
        if value in self.seen:
            return

        self.seen.add(value)
        prev_exist, post_exist = value - 1 in self.seen, value + 1 in self.seen

        if not prev_exist and not post_exist:
            insort(self.intervals, [value, value], key=self.key)
            return

        i = bisect(self.intervals, value, key=self.key)
        # new interval by itself
        if prev_exist and post_exist:
            _, end = self.intervals.pop(i)
            self.intervals[i - 1][1] = end

        elif prev_exist:
            # end value for last interval
            self.intervals[i - 1][1] = value

        else:  # post_exist
            self.intervals[i][0] = value

    def getIntervals(self) -> list[list[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
# @lc code=end


def main() -> None:
    ranges = SummaryRanges()
    ranges.addNum(1)
    print(ranges.getIntervals())
    ranges.addNum(2)
    print(ranges.getIntervals())
    ranges.addNum(5)
    print(ranges.getIntervals())
    ranges.addNum(4)
    print(ranges.getIntervals())
    ranges.addNum(3)
    print(ranges.getIntervals())


if __name__ == "__main__":
    main()
