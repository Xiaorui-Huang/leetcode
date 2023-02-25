/*
 * @lc app=leetcode id=131 lang=rust
 *
 * [131] Palindrome Partitioning
 *
 * https://leetcode.com/problems/palindrome-partitioning/description/
 *
 * algorithms
 * Medium (62.91%)
 * Likes:    9208
 * Dislikes: 299
 * Total Accepted:    564.4K
 * Total Submissions: 893.8K
 * Testcase Example:  '"aab"'
 *
 * Given a string s, partition s such that every substring of the partition is
 * a palindrome. Return all possible palindrome partitioning of s.
 *
 *
 * Example 1:
 * Input: s = "aab"
 * Output: [["a","a","b"],["aa","b"]]
 * Example 2:
 * Input: s = "a"
 * Output: [["a"]]
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 16
 * s contains only lowercase English letters.
 *
 *
 */
struct Solution;

// @lc code=start
impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let mut palin_parts = vec![];
        fn dfs(s: String, mut path: Vec<String>, palim_parts: &mut Vec<Vec<String>>) {
            if s.is_empty() {
                palim_parts.push(path);
                return;
            }
            for i in 1..=s.len() {
                let (left, right) = s.split_at(i);
                if Solution::is_palindrome(left.to_string()) {
                    path.push(left.to_string());
                    dfs(right.to_string(), path.clone(), palim_parts);
                    path.pop();
                }
            }
        }
        dfs(s, vec![], &mut palin_parts);
        return palin_parts;
    }
    fn is_palindrome(s: String) -> bool {
        let s = s.as_bytes();
        let n = s.len();
        for i in 0..(n / 2) {
            if s[i] != s[n - i - 1] {
                return false;
            }
        }

        return true;
    }
}
// @lc code=end
fn main() {}
