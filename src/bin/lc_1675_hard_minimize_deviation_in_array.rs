/*
 * @lc app=leetcode id=1675 lang=rust
 *
 * [1675] Minimize Deviation in Array
 *
 * https://leetcode.com/problems/minimize-deviation-in-array/description/
 *
 * algorithms
 * Hard (51.96%)
 * Likes:    1821
 * Dislikes: 97
 * Total Accepted:    49.7K
 * Total Submissions: 94.8K
 * Testcase Example:  '[1,2,3,4]'
 *
 * You are given an array nums of n positive integers.
 *
 * You can perform two types of operations on any element of the array any
 * number of times:
 *
 *
 * If the element is even, divide it by 2.
 *
 *
 * For example, if the array is [1,2,3,4], then you can do this operation on
 * the last element, and the array will be [1,2,3,2].
 *
 *
 * If the element is odd, multiply it by 2.
 *
 * For example, if the array is [1,2,3,4], then you can do this operation on
 * the first element, and the array will be [2,2,3,4].
 *
 *
 *
 *
 * The deviation of the array is the maximum difference between any two
 * elements in the array.
 *
 * Return the minimum deviation the array can have after performing some number
 * of operations.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,2,3,4]
 * Output: 1
 * Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
 * then the deviation will be 3 - 2 = 1.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [4,1,5,20,3]
 * Output: 3
 * Explanation: You can transform the array after two operations to
 * [4,2,5,5,3], then the deviation will be 5 - 2 = 3.
 *
 *
 * Example 3:
 *
 *
 * Input: nums = [2,10,8]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * n == nums.length
 * 2 <= n <= 5 * 10^4
 * 1 <= nums[i] <= 10^9
 *
 *
 */

struct Solution;
// @lc code=start
use std::collections::BinaryHeap;
impl Solution {
    pub fn minimum_deviation(nums: Vec<i32>) -> i32 {
        let mut max_heap = BinaryHeap::new();
        let mut min_val = std::i32::MAX;
        for mut num in nums {
            if num % 2 == 1 {
                num *= 2;
            }
            max_heap.push(num);
            min_val = min_val.min(num);
        }

        let mut min_deviation = std::i32::MAX;

        while let Some(max_val) = max_heap.pop() {
            min_deviation = min_deviation.min(max_val - min_val);
            if max_val % 2 == 1 {
                break;
            }
            let new_val = max_val / 2;
            min_val = min_val.min(new_val);
            max_heap.push(new_val);
        }

        return min_deviation;
    }
}
// @lc code=end
fn main() {}
