/*
 * @lc app=leetcode id=134 lang=rust
 *
 * [134] Gas Station
 *
 * https://leetcode.com/problems/gas-station/description/
 *
 * algorithms
 * Medium (45.14%)
 * Likes:    8871
 * Dislikes: 759
 * Total Accepted:    531.6K
 * Total Submissions: 1.2M
 * Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
 *
 * There are n gas stations along a circular route, where the amount of gas at
 * the i^th station is gas[i].
 *
 * You have a car with an unlimited gas tank and it costs cost[i] of gas to
 * travel from the i^th station to its next (i + 1)^th station. You begin the
 * journey with an empty tank at one of the gas stations.
 *
 * Given two integer arrays gas and cost, return the starting gas station's
 * index if you can travel around the circuit once in the clockwise direction,
 * otherwise return -1. If there exists a solution, it is guaranteed to be
 * unique
 *
 *
 * Example 1:
 *
 *
 * Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
 * Output: 3
 * Explanation:
 * Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
 * 4 = 4
 * Travel to station 4. Your tank = 4 - 1 + 5 = 8
 * Travel to station 0. Your tank = 8 - 2 + 1 = 7
 * Travel to station 1. Your tank = 7 - 3 + 2 = 6
 * Travel to station 2. Your tank = 6 - 4 + 3 = 5
 * Travel to station 3. The cost is 5. Your gas is just enough to travel back
 * to station 3.
 * Therefore, return 3 as the starting index.
 *
 *
 * Example 2:
 *
 *
 * Input: gas = [2,3,4], cost = [3,4,3]
 * Output: -1
 * Explanation:
 * You can't start at station 0 or 1, as there is not enough gas to travel to
 * the next station.
 * Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
 * 4
 * Travel to station 0. Your tank = 4 - 3 + 2 = 3
 * Travel to station 1. Your tank = 3 - 3 + 3 = 3
 * You cannot travel back to station 2, as it requires 4 unit of gas but you
 * only have 3.
 * Therefore, you can't travel around the circuit once no matter where you
 * start.
 *
 *
 *
 * Constraints:
 *
 *
 * n == gas.length == cost.length
 * 1 <= n <= 10^5
 * 0 <= gas[i], cost[i] <= 10^4
 *
 *
 */

struct Solution;
// @lc code=start
use std::cmp::min;
enum Approach {
    PrefixSum,
    OnePass,
}
const APPROACH: Approach = Approach::OnePass;

impl Solution {
    pub fn can_complete_circuit(gases: Vec<i32>, costs: Vec<i32>) -> i32 {
        match APPROACH {
            Approach::PrefixSum => Self::can_complete_circuit_prefix_sum(gases, costs),
            Approach::OnePass => Self::can_complete_circuit_one_pass(gases, costs),
        }
    }
    pub fn can_complete_circuit_one_pass(gases: Vec<i32>, costs: Vec<i32>) -> i32 {
        let (mut total_surplus, mut surplus, mut start) = (0, 0, 0);

        for (i, (gas, cost)) in gases.iter().zip(costs).enumerate() {
            total_surplus += gas - cost;
            surplus += gas - cost;
            if surplus < 0 {
                surplus = 0;
                start = (i + 1) as i32;
            }
        }
        if total_surplus < 0 {
            return -1;
        }
        start
    }
    pub fn can_complete_circuit_prefix_sum(gases: Vec<i32>, costs: Vec<i32>) -> i32 {
        let n = gases.len();
        let profits = gases
            .iter()
            .zip(costs)
            .map(|(gas, cost)| gas - cost)
            .collect::<Vec<i32>>();

        let mut deficit = profits[0];
        let mut running_sum = 0;
        for profit in profits.iter() {
            running_sum += profit;
            deficit = min(deficit, running_sum);
        }

        let target = running_sum;
        if target < 0 {
            return -1;
        }
        running_sum = 0; //reset to calculate running rum again but reversed

        for (i, profit) in profits.iter().rev().enumerate() {
            running_sum += profit;
            if running_sum + deficit == target {
                return (n - 1 - i) as i32; // will not overflow since n >= 1, 0 <= i < n => (n - 1 - i) >= 0
            };
        }
        0 // Never reached with a guaranteed unique solution
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![1,2,3,4,5], vec![3,4,5,1,2], 3)]
#[case(vec![2,3,4], vec![3,4,3], -1)]
fn test_can_complete_circuit(
    #[case] gases: Vec<i32>,
    #[case] costs: Vec<i32>,
    #[case] expected: i32,
) {
    assert_eq!(Solution::can_complete_circuit(gases, costs), expected);
}

fn main() {}
