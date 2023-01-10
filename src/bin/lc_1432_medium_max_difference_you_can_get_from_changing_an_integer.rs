/*
 * @lc app=leetcode id=1432 lang=rust
 *
 * [1432] Max Difference You Can Get From Changing an Integer
 *
 * https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/
 *
 * algorithms
 * Medium (42.86%)
 * Likes:    169
 * Dislikes: 219
 * Total Accepted:    13.9K
 * Total Submissions: 32.5K
 * Testcase Example:  '555'
 *
 * You are given an integer num. You will apply the following steps exactly two
 * times:
 *
 *
 * Pick a digit x (0 <= x <= 9).
 * Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
 * Replace all the occurrences of x in the decimal representation of num by
 * y.
 * The new integer cannot have any leading zeros, also the new integer cannot
 * be 0.
 *
 *
 * Let a and b be the results of applying the operations to num the first and
 * second times, respectively.
 *
 * Return the max difference between a and b.
 *
 *
 * Example 1:
 *
 *
 * Input: num = 555
 * Output: 888
 * Explanation: The first time pick x = 5 and y = 9 and store the new integer
 * in a.
 * The second time pick x = 5 and y = 1 and store the new integer in b.
 * We have now a = 999 and b = 111 and max difference = 888
 *
 *
 * Example 2:
 *
 *
 * Input: num = 9
 * Output: 8
 * Explanation: The first time pick x = 9 and y = 9 and store the new integer
 * in a.
 * The second time pick x = 9 and y = 1 and store the new integer in b.
 * We have now a = 9 and b = 1 and max difference = 8
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= num <= 10^8
 *
 *
 */
struct Solution;

// @lc code=start
enum Approach {
    Messy,
    Clean,
}
const APPROACH: Approach = Approach::Clean;
impl Solution {
    pub fn max_diff(num: i32) -> i32 {
        match APPROACH {
            Approach::Messy => Self::max_diff_messy(num),
            Approach::Clean => Self::max_diff_clean(num),
        }
    }
    pub fn max_diff_clean(num: i32) -> i32 {
        let mut cur = num;
        let mut stack = vec![];
        stack.reserve(9);
        while cur != 0 {
            stack.push(cur % 10);
            cur /= 10;
        }

        let (mut high, mut low) = (0, 0);
        // target_high default to 9 as that is the else case
        // target_low default to 2 since it cannot be 0 or 1 when first_digit is 1
        let (mut target_high, mut target_low) = (9, 2);
        // find target high
        for &digit in stack.iter().rev() {
            if digit != 9 {
                target_high = digit;
                break;
            }
        }
        // calculate high
        for &digit in stack.iter().rev() {
            high *= 10;
            high += if digit == target_high { 9 } else { digit };
        }

        // calculate low
        let first_digit = *stack.last().unwrap();
        // first is not 1, just set all digit equal to first to 1
        if first_digit != 1 {
            for &digit in stack.iter().rev() {
                low *= 10;
                low += if digit == first_digit { 1 } else { digit };
            }
        // first is 1, find the target is larger than 0 and 1, then replace it
        } else {
            for &digit in stack.iter().rev() {
                if digit != 0 && digit != 1 {
                    target_low = digit;
                    break;
                }
            }
            let mut skip_first_iter = stack.iter().rev();
            low += skip_first_iter.next().unwrap();

            for &digit in skip_first_iter {
                low *= 10;
                low += if digit == target_low { 0 } else { digit };
            }
        }

        return high - low;
    }

    pub fn max_diff_messy(num: i32) -> i32 {
        let mut cur = num;
        let mut stack = vec![];
        stack.reserve(9); // according to constraint, we have a maximum of 9 digits
        let mut others: bool = false;
        while cur != 0 {
            // gather all the digits
            stack.push(cur % 10);
            if !(vec![0, 1].contains(stack.last().unwrap())) {
                others = true;
            }
            cur /= 10;
        }
        //get the target to replace, depending on value of the first and last digits
        let (mut target_low, mut target_high);
        let value_low;
        let first_digit = *stack.last().unwrap();
        if first_digit == 1 {
            target_low = (10 as i32).pow(stack.len() as u32 - 1);
            let mut diff = num - target_low;
            target_low = diff / (10 as i32).pow((diff as f64).log10() as u32); //use log10 to get the number of digits
            while others && target_low == 1 {
                diff = diff - (10 as i32).pow((diff as f64).log10() as u32);
                target_low = diff / (10 as i32).pow((diff as f64).log10() as u32);
            }
            value_low = if target_low == 1 { 1 } else { 0 };
        } else {
            target_low = first_digit;
            value_low = 1;
        }

        target_high = first_digit;
        if first_digit == 9 {
            for &digit in stack.iter().rev() {
                if digit != 9 {
                    target_high = digit;
                    break;
                }
            }
        }

        let (mut high, mut low) = (0, 0);
        while !stack.is_empty() {
            high *= 10;
            low *= 10;

            let digit = stack.pop().unwrap();
            let (mut cur_val_high, mut cur_val_low) = (digit, digit);

            if digit == target_high {
                cur_val_high = 9;
            }
            if digit == target_low {
                cur_val_low = value_low;
            }
            high += cur_val_high;
            low += cur_val_low;
        }
        return high - low;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(9089733, 9989733 - 1081733)]
#[case(1101057, 9909057 - 1101007)]
#[case(111, 999 - 111)]
#[case(96293012, 83080000)] //99293012 - 16213012
#[case(555, 888)]
#[case(545, 808)]
#[case(9, 8)]
#[case(108121, 808808)] // 908929 - 100121 # target for low is 8 -> 0
#[case(109191, 809898)] //909999 - 100101 # target for low is 9 -> 0
#[case(919, 888)]
#[case(819, 919 - 119)]
#[case(1231929, 9239929 - 1031909)]
fn test_max_diff(#[case] num: i32, #[case] expected: i32) {
    assert_eq!(Solution::max_diff(num), expected);
}

fn main() {}
