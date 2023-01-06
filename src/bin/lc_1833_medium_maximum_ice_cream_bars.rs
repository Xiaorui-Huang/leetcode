/*
 * @lc app=leetcode id=1833 lang=rust
 *
 * [1833] Maximum Ice Cream Bars
 *
 * https://leetcode.com/problems/maximum-ice-cream-bars/description/
 *
 * algorithms
 * Medium (65.69%)
 * Likes:    1644
 * Dislikes: 583
 * Total Accepted:    113.8K
 * Total Submissions: 153.6K
 * Testcase Example:  '[1,3,2,4,1]\n7'
 *
 * It is a sweltering summer day, and a boy wants to buy some ice cream bars.
 *
 * At the store, there are n ice cream bars. You are given an array costs of
 * length n, where costs[i] is the price of the i^th ice cream bar in coins.
 * The boy initially has coins coins to spend, and he wants to buy as many ice
 * cream bars as possible.
 *
 * Return the maximum number of ice cream bars the boy can buy with coins
 * coins.
 *
 * Note: The boy can buy the ice cream bars in any order.
 *
 *
 * Example 1:
 *
 *
 * Input: costs = [1,3,2,4,1], coins = 7
 * Output: 4
 * Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total
 * price of 1 + 3 + 2 + 1 = 7.
 *
 *
 * Example 2:
 *
 *
 * Input: costs = [10,6,8,7,7,8], coins = 5
 * Output: 0
 * Explanation: The boy cannot afford any of the ice cream bars.
 *
 *
 * Example 3:
 *
 *
 * Input: costs = [1,6,3,1,2,5], coins = 20
 * Output: 6
 * Explanation: The boy can buy all the ice cream bars for a total price of 1 +
 * 6 + 3 + 1 + 2 + 5 = 18.
 *
 *
 *
 * Constraints:
 *
 *
 * costs.length == n
 * 1 <= n <= 10^5
 * 1 <= costs[i] <= 10^5
 * 1 <= coins <= 10^8
 *
 */
struct Solution;
// @lc code=start
use std::collections::BinaryHeap;
impl Solution {
    pub fn max_ice_cream(costs: Vec<i32>, coins: i32) -> i32 {
        let (mut count, mut spending) = (0, 0);
        let mut heap = BinaryHeap::new();
        for cost in costs {
            if (spending + cost) <= coins {
                spending += cost;
                count += 1;
                heap.push(cost);
                continue;
            }
            if &cost < heap.peek().unwrap_or(&(cost - 1)) {
                spending = spending - heap.pop().unwrap() + cost;
                heap.push(cost);
            }
        }

        count
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![1,3,2,4,1], 7, 4)]
#[case(vec![10,6,8,7,7,8], 5, 0)]
#[case(vec![1,6,3,1,2,5], 20, 6)]
#[case(vec![27, 23, 33, 26, 46, 86, 70, 85, 89, 82, 57, 66, 42, 18, 18, 5, 46, 56, 42, 82, 52, 78, 4, 27, 96, 74, 74, 52, 2, 24, 78, 18, 42, 10, 12, 10, 80, 30, 60, 38, 32, 7, 98, 26, 18, 62, 50, 42, 15, 14, 32, 86, 93, 98, 47, 46, 58, 42, 74, 69, 51, 53, 58, 40, 66, 46, 65, 2, 10, 82, 94, 26, 6, 78, 2, 101, 97, 16, 12, 18, 71, 5, 46, 22, 58, 12, 18, 62, 61, 51, 2, 18, 34, 12, 36, 58, 20, 12, 17, 70], 241, 24)]
fn test_max_ice_cream(#[case] costs: Vec<i32>, #[case] coins: i32, #[case] expected: i32) {
    assert_eq!(Solution::max_ice_cream(costs, coins), expected);
}

fn main() {}
