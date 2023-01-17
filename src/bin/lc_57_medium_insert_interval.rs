/*
 * @lc app=leetcode id=57 lang=rust
 *
 * [57] Insert Interval
 *
 * https://leetcode.com/problems/insert-interval/description/
 *
 * algorithms
 * Medium (38.05%)
 * Likes:    6767
 * Dislikes: 477
 * Total Accepted:    665.1K
 * Total Submissions: 1.7M
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

struct Solution;
// @lc code=start
use std::{cmp::min, vec};
impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        if intervals.is_empty() {
            return vec![new_interval];
        }

        let (mut start, mut end) = (new_interval[0], new_interval[1]);
        if end < intervals[0][0] {
            return [vec![new_interval], intervals].concat();
        }
        let binary_search = |target: i32| -> usize {
            let (mut lo, mut hi) = (0, (intervals.len() - 1) as i32);

            while lo < hi {
                let mid = ((hi + lo) / 2) as usize;
                let start = intervals[mid][0];
                if start <= target && target < intervals[mid + 1][0] {
                    return mid;
                } else if target < start {
                    hi = mid as i32 - 1
                } else {
                    lo = mid as i32 + 1
                }
            }
            return lo as usize;
        };

        let (mut start_insert_i, end_insert_i) = (binary_search(start), binary_search(end));
        let (interval_start, interval_end) =
            (intervals[start_insert_i][0], intervals[start_insert_i][1]);

        if interval_end < start {
            start_insert_i += 1
        } else {
            start = min(interval_start, start);
        }

        let (interval_start, interval_end) =
            (intervals[end_insert_i][0], intervals[end_insert_i][1]);
        if interval_start <= end && end <= interval_end {
            end = interval_end
        }
        let res = [
            &intervals[..start_insert_i],
            &[vec![start, end]],
            &intervals[(end_insert_i + 1)..],
        ]
        .concat();

        return res;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(&[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], &[4, 8], &[[1, 2], [3, 10], [12, 16]])]
#[case(&[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], &[0, 1], &[[0, 2], [3, 5], [6, 7], [8, 10], [12, 16]])]
#[case(&[[1, 3], [6, 9]], &[9, 11], &[[1, 3], [6, 11]])]
#[case(&[], &[1, 3], &[[1, 3]])]
#[case(&[[1, 3], [6, 9]], &[-1, 0], &[[-1, 0], [1, 3], [6, 9]])]
#[case(&[[1, 3], [6, 9]], &[0, 0], &[[0, 0], [1, 3], [6, 9]])]
#[case(&[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], &[4, 7], &[[1, 2], [3, 7], [8, 10], [12, 16]])]
#[case(&[[1, 2], [3, 5], [6, 7], [9, 10], [15, 16]], &[11, 14], &[[1, 2], [3, 5], [6, 7], [9, 10], [11, 14], [15, 16]])]
#[case(&[[1, 2], [3, 5], [6, 7], [9, 10], [15, 16]], &[11, 200], &[[1, 2], [3, 5], [6, 7], [9, 10], [11, 200]])]
#[case(&[[1, 2], [3, 5], [6, 7], [9, 10], [12, 16]], &[7, 8], &[[1, 2], [3, 5], [6, 8], [9, 10], [12, 16]])]
#[case(&[[1, 3], [6, 9]], &[2, 5], &[[1, 5], [6, 9]])]
#[case(&[[1, 3], [6, 9]], &[1, 9], &[[1, 9]])]
#[case(&[[1, 3], [6, 9]], &[1, 10], &[[1, 10]])]
#[case(&[[1, 3], [6, 9]], &[0, 111], &[[0, 111]])]
#[case(&[[1, 3], [6, 9]], &[0, 1], &[[0, 3], [6, 9]])]
#[case(&[[1, 3], [6, 9]], &[10, 11], &[[1, 3], [6, 9], [10, 11]])]
fn test_insert(
    #[case] intervals: &[[i32; 2]],
    #[case] new_interval: &[i32; 2],
    #[case] expected: &[[i32; 2]],
) {
    assert_eq!(
        Solution::insert(
            intervals.to_vec().into_iter().map(|x| x.to_vec()).collect(),
            new_interval.to_vec()
        ),
        expected
            .to_vec()
            .into_iter()
            .map(|x| x.to_vec())
            .collect::<Vec<Vec<i32>>>()
    );
}
fn main() {}
