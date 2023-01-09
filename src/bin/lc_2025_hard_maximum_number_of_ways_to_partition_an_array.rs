/*
 * @lc app=leetcode id=2025 lang=rust
 *
 * [2025] Maximum Number of Ways to Partition an Array
 *
 * https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/description/
 *
 * algorithms
 * Hard (32.62%)
 * Likes:    371
 * Dislikes: 38
 * Total Accepted:    6.6K
 * Total Submissions: 20.3K
 * Testcase Example:  '[2,-1,2]\n3'
 *
 * You are given a 0-indexed integer array nums of length n. The number of ways
 * to partition nums is the number of pivot indices that satisfy both
 * conditions:
 *
 *
 * 1 <= pivot < n
 * nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] +
 * ... + nums[n - 1]
 *
 *
 * You are also given an integer k. You can choose to change the value of one
 * element of nums to k, or to leave the array unchanged.
 *
 * Return the maximum possible number of ways to partition nums to satisfy both
 * conditions after changing at most one element.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [2,-1,2], k = 3
 * Output: 1
 * Explanation: One optimal approach is to change nums[0] to k. The array
 * becomes [3,-1,2].
 * There is one way to partition the array:
 * - For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [0,0,0], k = 1
 * Output: 2
 * Explanation: The optimal approach is to leave the array unchanged.
 * There are two ways to partition the array:
 * - For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
 * - For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
 * Output: 4
 * Explanation: One optimal approach is to change nums[2] to k. The array
 * becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
 * There are four ways to partition the array.
 *
 *
 *
 * Constraints:
 *
 *
 * n == nums.length
 * 2 <= n <= 10^5
 * -10^5 <= k, nums[i] <= 10^5
 *
 *
 */

struct Solution;
// @lc code=start
use std::{cmp::max, collections::HashMap};

impl Solution {
    pub fn ways_to_partition(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let mut total = 0;
        let mut prefix_sum = vec![0; n];
        for (i, num) in nums.iter().enumerate() {
            total += num;
            prefix_sum[i] = total;
        }

        let mut count = 0;
        prefix_sum.pop();
        for cur_sum in prefix_sum.iter() {
            if *cur_sum == total - cur_sum {
                count += 1
            }
        }

        let mut prefix_counter = HashMap::new();
        let mut suffix_counter = HashMap::new();
        for cur_sum in prefix_sum.iter() {
            suffix_counter
                .entry(*cur_sum)
                .and_modify(|v| *v += 1)
                .or_insert(1);
        }

        prefix_sum.push(total);
        for (num, cur_sum) in nums.iter().zip(prefix_sum) {
            let goal = (total + k - num) as f64 / 2.0;
            if goal.fract() == 0.0 {
                let adjusted_goal = goal as i32 - k + num;
                count = max(
                    count,
                    prefix_counter.get(&(goal as i32)).unwrap_or(&0)
                        + suffix_counter.get(&adjusted_goal).unwrap_or(&0),
                );
            }
            suffix_counter
                .entry(cur_sum)
                .and_modify(|count| *count -= 1);
            prefix_counter
                .entry(cur_sum)
                .and_modify(|count| *count += 1)
                .or_insert(1);
        }

        return count;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![0, 0, 0], 1, 2)]
#[case(vec![0, 0, 0, 3], 1, 0)]
#[case(vec![0, 0, 0, 3], 0, 3)]
#[case(vec![0, 0, 0, 3, 0], 0, 4)]
#[case(vec![0, 0, 0, 3], -3, 2)]
#[case(vec![2, -1, 2], 3, 1)]
#[case(vec![2, 1, 3, 1, 3, 0, -4, 5, 2], 4, 2)]
#[case(vec![22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], -33, 4)]
fn test_ways_to_partition(#[case] nums: Vec<i32>, #[case] k: i32, #[case] expected: i32) {
    assert_eq!(Solution::ways_to_partition(nums, k), expected);
}

fn main() {}
