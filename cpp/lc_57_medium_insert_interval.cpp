/*
 * @lc app=leetcode id=57 lang=cpp
 *
 * [57] Insert Interval
 *
 * https://leetcode.com/problems/insert-interval/description/
 *
 * algorithms
 * Medium (41.33%)
 * Likes:    10106
 * Dislikes: 776
 * Total Accepted:    1.1M
 * Total Submissions: 2.6M
 * Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
 *
 * You are given an array of non-overlapping intervals intervals where
 * intervals[i] = [starti, endi] represent the start and the end of the i^th
 * interval and intervals is sorted in ascending order by starti. You are also
 * given an interval newInterval = [start, end] that represents the start and
 * end of another interval.
 *
 * Insert newInterval into intervals such that intervals is still sorted in
 * ascending order by starti and intervals still does not have any overlapping
 * intervals (merge overlapping intervals if necessary).
 *
 * Return intervals after the insertion.
 *
 * Note that you don't need to modify intervals in-place. You can make a new
 * array and return it.
 *
 *
 * Example 1:
 *
 *
 * Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
 * Output: [[1,5],[6,9]]
 *
 *
 * Example 2:
 *
 *
 * Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
 * Output: [[1,2],[3,10],[12,16]]
 * Explanation: Because the new interval [4,8] overlaps with
 * [3,5],[6,7],[8,10].
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= intervals.length <= 10^4
 * intervals[i].length == 2
 * 0 <= starti <= endi <= 10^5
 * intervals is sorted by starti in ascending order.
 * newInterval.length == 2
 * 0 <= start <= end <= 10^5
 *
 *
 */
#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// @lc code=start

/**
 * @brief NB: can be done in O(n) time, but this is a O(logn + n) solution
 * 
 */
class Solution {
  public:
    // max position less than target
    int binary_search_left(vector<vector<int>> &nums, int target, int pos) {
        int lo = 0, hi = nums.size() - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int num = nums[mid][pos];
            if (num <= target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return hi; // -1 return
    }

    // min position larger than target
    int binary_search_right(vector<vector<int>> &nums, int target) {
        int lo = 0, hi = nums.size() - 1;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int num = nums[mid][0];
            if (target <= num) {
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return lo; // n return
    }

    /**
     * @brief Could have just did a linear search pass ...
     *
     * @param intervals
     * @param newInterval
     * @return vector<vector<int>>
     */
    vector<vector<int>> insert(vector<vector<int>> &intervals,
                               vector<int> &newInterval) {
        if (intervals.empty()) {
            return {newInterval};
        }
        // binary search right after for start and right before for end
        // start_index: if start_index's end >= start
        //                  we keep the interval and merge until end intervel

        int start_idx = binary_search_left(intervals, newInterval[0], 1) +
                        1; // possible n - search max less than ends
        //                                             end comared to starts
        int end_idx = binary_search_left(intervals, newInterval[1], 0) +
                      1; // possible n search max less than starts
        // cout << start_idx << ", " << end_idx << endl;
        // assert(start_idx <= end_idx);

        vector<vector<int>> res;
        for (int i = 0; i < start_idx; i++)
            res.push_back(intervals[i]);

        // we do a bunch of merged at once
        if (start_idx < end_idx) {
            int merged_start = min(intervals[start_idx][0], newInterval[0]);
            int merged_end = max(intervals[end_idx - 1][1], newInterval[1]);

            newInterval = {merged_start, merged_end};
        }

        // now that we have the latest merge, check on last time if we need to
        // merge res.back() and newInterval's start if we need to merge this
        // interval in, as it is directly following the
        if (res.empty() || res.back()[1] != newInterval[0])
            res.push_back(newInterval);
        // last interval end (... [a, b], [b, c] ...)
        else // res.back()[1] == newInterval[0]
            res.back()[1] = newInterval[1];

        // push back the rest of the vectors from intervals
        for (int i = end_idx; i < intervals.size(); i++)
            res.push_back(intervals[i]);
        return res;
    }
};
// @lc code=end