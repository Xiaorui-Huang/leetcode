/*
 * @lc app=leetcode id=1345 lang=rust
 *
 * [1345] Jump Game IV
 *
 * https://leetcode.com/problems/jump-game-iv/description/
 *
 * algorithms
 * Hard (43.87%)
 * Likes:    3132
 * Dislikes: 108
 * Total Accepted:    114.6K
 * Total Submissions: 247K
 * Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
 *
 * Given an array of integers arr, you are initially positioned at the first
 * index of the array.
 *
 * In one step you can jump from index i to index:
 *
 *
 * i + 1 where: i + 1 < arr.length.
 * i - 1 where: i - 1 >= 0.
 * j where: arr[i] == arr[j] and i != j.
 *
 *
 * Return the minimum number of steps to reach the last index of the array.
 *
 * Notice that you can not jump outside of the array at any time.
 *
 *
 * Example 1:
 *
 *
 * Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
 * Output: 3
 * Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that
 * index 9 is the last index of the array.
 *
 *
 * Example 2:
 *
 *
 * Input: arr = [7]
 * Output: 0
 * Explanation: Start index is the last index. You do not need to jump.
 *
 *
 * Example 3:
 *
 *
 * Input: arr = [7,6,9,6,9,6,9,7]
 * Output: 1
 * Explanation: You can jump directly from index 0 to index 7 which is last
 * index of the array.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= arr.length <= 5 * 10^4
 * -10^8 <= arr[i] <= 10^8
 *
 *
 */

struct Solution;

// @lc code=start
use std::collections::VecDeque;
impl Solution {
    pub fn min_jumps(arr: Vec<i32>) -> i32 {
        let n = arr.len();
        let mut portals = arr.iter().enumerate().fold(
            std::collections::HashMap::new(),
            |mut map, (i, &portal_key)| {
                map.entry(portal_key).or_insert(vec![]).push(i);
                return map;
            },
        );
        let mut visited = vec![false; n];

        let mut q = VecDeque::new();
        q.push_back((0, 0));

        while !q.is_empty() {
            let (i, step) = q.pop_front().unwrap();
            if i == n - 1 {
                return step;
            }
            if visited[i] {
                continue;
            }
            visited[i] = true;

            if i > 0 {
                q.push_back((i - 1, step + 1));
            }
            if i < n - 1 {
                q.push_back((i + 1, step + 1));
            }
            if let Some(portal) = portals.get_mut(&arr[i]) {
                for &portal_index in portal.iter() {
                    q.push_back((portal_index, step + 1));
                }
                portal.clear();
            }
        }

        // never reached
        return -1;
    }
}
// @lc code=end

fn main() {}
