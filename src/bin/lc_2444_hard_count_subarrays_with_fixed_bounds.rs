/*
 * @lc app=leetcode id=2444 lang=rust
 *
 * [2444] Count Subarrays With Fixed Bounds
 *
 * https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/
 *
 * algorithms
 * Hard (44.10%)
 * Likes:    732
 * Dislikes: 14
 * Total Accepted:    14.8K
 * Total Submissions: 30.7K
 * Testcase Example:  '[1,3,5,2,7,5]\n1\n5'
 *
 * You are given an integer array nums and two integers minK and maxK.
 *
 * A fixed-bound subarray of nums is a subarray that satisfies the following
 * conditions:
 *
 *
 * The minimum value in the subarray is equal to minK.
 * The maximum value in the subarray is equal to maxK.
 *
 *
 * Return the number of fixed-bound subarrays.
 *
 * A subarray is a contiguous part of an array.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
 * Output: 2
 * Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,1,1,1], minK = 1, maxK = 1
 * Output: 10
 * Explanation: Every subarray of nums is a fixed-bound subarray. There are 10
 * possible subarrays.
 *
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 10^5
 * 1 <= nums[i], minK, maxK <= 10^6
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, min_k: i32, max_k: i32) -> i64 {
        let mut count = 0;
        let (mut left_bound, mut min_pos, mut max_pos) = (-1, -1, -1);

        for (i, num) in nums.into_iter().enumerate() {
            if num < min_k || max_k < num {
                left_bound = i as i64;
                continue;
            }
            if num == min_k {
                min_pos = i as i64
            }
            if num == max_k {
                max_pos = i as i64
            }
            count += 0.max(min_pos.min(max_pos) - left_bound);
        }

        return count;
    }
}
// @lc code=end

fn main() {}
