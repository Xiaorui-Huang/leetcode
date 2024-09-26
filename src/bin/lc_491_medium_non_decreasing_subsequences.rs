//
// @lc app=leetcode id=491 lang=rust
//
// [491] Non-decreasing Subsequences
//
// https://leetcode.com/problems/non-decreasing-subsequences/description/
//
// algorithms
// Medium (52.31%)
// Likes:    2015
// Dislikes: 171
// Total Accepted:    93.9K
// Total Submissions: 175.1K
// Testcase Example:  '[4,6,7,7]'
//
// Given an integer array nums, return all the different possible non-decreasing
// subsequences of the given array with at least two elements. You may return
// the answer in any order.
//
//
// Example 1:
//
//
// Input: nums = [4,6,7,7]
// Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
//
//
// Example 2:
//
//
// Input: nums = [4,4,3,2,1]
// Output: [[4,4]]
//
//
//
// Constraints:
//
//
// 1 <= nums.length <= 15
// -100 <= nums[i] <= 100
//
//
//

struct Solution;
// @lc code=start
use std::collections::HashSet;
impl Solution {
    pub fn find_subsequences(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let n = nums.len();
        let mut seen_seq: HashSet<Vec<i32>> = HashSet::new();
        let mut subsequence = vec![];

        fn backtrack(
            index: usize,
            nums: &Vec<i32>,
            length: usize,
            seen_seq: &mut HashSet<Vec<i32>>,
            subsequence: &mut Vec<i32>,
        ) {
            if index == length {
                if subsequence.len() >= 2 {
                    seen_seq.insert(subsequence.to_vec());
                }
                return;
            }

            let num = nums[index];
            if subsequence.is_empty() || subsequence.last().unwrap() <= &num {
                subsequence.push(num);
                backtrack(index + 1, nums, length, seen_seq, subsequence);
                subsequence.pop();
            }

            backtrack(index + 1, nums, length, seen_seq, subsequence)
        }
        backtrack(0, &nums, n, &mut seen_seq, &mut subsequence);

        return seen_seq.into_iter().collect();
    }
}

// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![4, 6, 7, 7], vec![vec![4, 6], vec![4, 6, 7], vec![4, 6, 7, 7], vec![4, 7],vec![4, 7, 7],vec![6, 7],vec![6, 7, 7],vec! [7, 7]])]
#[case(vec![4, 4, 3, 2, 1], [vec![4, 4]].to_vec())]
fn test_find_subsequences(#[case] nums: Vec<i32>, #[case] expected: Vec<Vec<i32>>) {
    assert_eq!(
        Solution::find_subsequences(nums)
            .into_iter()
            .collect::<HashSet<Vec<i32>>>(),
        expected.into_iter().collect::<HashSet<Vec<i32>>>()
    );
}

fn main() {}
