/*
 * @lc app=leetcode id=438 lang=rust
 *
 * [438] Find All Anagrams in a String
 *
 * https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
 *
 * algorithms
 * Medium (49.06%)
 * Likes:    9765
 * Dislikes: 295
 * Total Accepted:    676.1K
 * Total Submissions: 1.4M
 * Testcase Example:  '"cbaebabacd"\n"abc"'
 *
 * Given two strings s and p, return an array of all the start indices of p's
 * anagrams in s. You may return the answer in any order.
 *
 * An Anagram is a word or phrase formed by rearranging the letters of a
 * different word or phrase, typically using all the original letters exactly
 * once.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "cbaebabacd", p = "abc"
 * Output: [0,6]
 * Explanation:
 * The substring with start index = 0 is "cba", which is an anagram of "abc".
 * The substring with start index = 6 is "bac", which is an anagram of "abc".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "abab", p = "ab"
 * Output: [0,1,2]
 * Explanation:
 * The substring with start index = 0 is "ab", which is an anagram of "ab".
 * The substring with start index = 1 is "ba", which is an anagram of "ab".
 * The substring with start index = 2 is "ab", which is an anagram of "ab".
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length, p.length <= 3 * 10^4
 * s and p consist of lowercase English letters.
 *
 *
 */

struct Solution;
// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        let n = p.len();
        if s.len() < n {
            return vec![];
        }

        let mut indices = vec![];
        let key_hole = p.as_bytes().into_iter().fold(HashMap::new(), |mut acc, c| {
            acc.entry(*c).and_modify(|x| *x += 1).or_insert(1);
            acc
        });
        let mut key = HashMap::new();

        let mut left = 0;
        let mut pins = 0;

        for (right, ch_right) in s.as_bytes().into_iter().enumerate() {
            if n < right - left + 1 {
                let ch_left = &s.as_bytes()[left];
                if key_hole.contains_key(ch_left) && key[ch_left] == key_hole[ch_left] {
                    pins -= 1;
                }
                key.entry(*ch_left).and_modify(|x| *x -= 1);
                left += 1;
            }

            key.entry(*ch_right).and_modify(|x| *x += 1).or_insert(1);
            if key_hole.contains_key(ch_right) && key[ch_right] == key_hole[ch_right] {
                pins += 1;
            }

            if pins == key_hole.len() {
                indices.push(left as i32);
            }
        }
        return indices;
    }
}
// @lc code=end

fn main() {}

use rstest::rstest;

#[rstest]
#[case(String::from("cbaebabacd"), String::from("abc"), vec![0, 6])]
#[case(String::from("abab"), String::from("ab"), vec![0, 1, 2])]
fn test_find_anagrams(#[case] s: String, #[case] p: String, #[case] expected: Vec<i32>) {
    assert_eq!(Solution::find_anagrams(s, p), expected);
}
