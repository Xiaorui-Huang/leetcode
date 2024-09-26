/*
 * @lc app=leetcode id=946 lang=rust
 *
 * [946] Validate Stack Sequences
 *
 * https://leetcode.com/problems/validate-stack-sequences/description/
 *
 * algorithms
 * Medium (67.68%)
 * Likes:    4085
 * Dislikes: 71
 * Total Accepted:    201.1K
 * Total Submissions: 296.8K
 * Testcase Example:  '[1,2,3,4,5]\n[4,5,3,2,1]'
 *
 * Given two integer arrays pushed and popped each with distinct values, return
 * true if this could have been the result of a sequence of push and pop
 * operations on an initially empty stack, or false otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
 * Output: true
 * Explanation: We might do the following sequence:
 * push(1), push(2), push(3), push(4),
 * pop() -> 4,
 * push(5),
 * pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
 *
 *
 * Example 2:
 *
 *
 * Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
 * Output: false
 * Explanation: 1 cannot be popped before 2.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= pushed.length <= 1000
 * 0 <= pushed[i] <= 1000
 * All the elements of pushed are unique.
 * popped.length == pushed.length
 * popped is a permutation of pushed.
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack = Vec::new();
        let mut i = 0;
        for ele in pushed {
            if ele != popped[i] {
                stack.push(ele);
            } else {
                i += 1;
            }
            while let Some(top) = stack.last() {
                if *top == popped[i] {
                    stack.pop();
                    i += 1;
                } else {
                    break;
                }
            }
        }
        return stack.is_empty();
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![1,2,3,4,5],vec![4,5,3,2,1], true)]
#[case(vec![1,2,3,4,5],vec![4,3,5,1,2], false)]
#[case(vec![1,2,3,4,5],vec![4,3,5,2,1], true)]
#[case(vec![],vec![], true)]
fn test_validate_stack_sequences(
    #[case] pushed: Vec<i32>,
    #[case] popped: Vec<i32>,
    #[case] expected: bool,
) {
    assert_eq!(Solution::validate_stack_sequences(pushed, popped), expected);
}
fn main() {}
