/*
 * @lc app=leetcode id=72 lang=rust
 *
 * [72] Edit Distance
 *
 * https://leetcode.com/problems/edit-distance/description/
 *
 * algorithms
 * Hard (52.98%)
 * Likes:    11200
 * Dislikes: 127
 * Total Accepted:    585.1K
 * Total Submissions: 1.1M
 * Testcase Example:  '"horse"\n"ros"'
 *
 * Given two strings word1 and word2, return the minimum number of operations
 * required to convert word1 to word2.
 *
 * You have the following three operations permitted on a word:
 *
 *
 * Insert a character
 * Delete a character
 * Replace a character
 *
 *
 *
 * Example 1:
 *
 *
 * Input: word1 = "horse", word2 = "ros"
 * Output: 3
 * Explanation:
 * horse -> rorse (replace 'h' with 'r')
 * rorse -> rose (remove 'r')
 * rose -> ros (remove 'e')
 *
 *
 * Example 2:
 *
 *
 * Input: word1 = "intention", word2 = "execution"
 * Output: 5
 * Explanation:
 * intention -> inention (remove 't')
 * inention -> enention (replace 'i' with 'e')
 * enention -> exention (replace 'n' with 'x')
 * exention -> exection (replace 'n' with 'c')
 * exection -> execution (insert 'u')
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= word1.length, word2.length <= 500
 * word1 and word2 consist of lowercase English letters.
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn min_distance(word1: String, word2: String) -> i32 {
        let (word1, word2) = if word1.len() <= word2.len() {
            (word1.as_bytes(), word2.as_bytes())
        } else {
            (word2.as_bytes(), word1.as_bytes())
        };

        let (cols, rows) = (word1.len(), word2.len());
        let mut dp = vec![0; cols + 1];
        let mut cur = 0;

        for len2 in 0..=rows {
            for len1 in 0..=cols {
                if len2 == 0 {
                    dp[len1] = len1;
                    continue;
                }
                if len1 == 0 {
                    cur = len2;
                    continue;
                }

                let prev = cur;
                cur = if word1[len1 - 1] != word2[len2 - 1] {
                    1 + dp[len1 - 1].min(dp[len1]).min(prev)
                } else {
                    dp[len1 - 1]
                };

                dp[len1 - 1] = prev;
            }
            dp[cols] = cur;
        }

        return *dp.last().unwrap() as i32;
    }
}
// @lc code=end
fn main() {}

// alternative solution
fn min_distance(word1: String, word2: String) -> i32 {
    // Treat characters as raw bytes, as it allows us to directly access the underlying arrays:
    let (word1, word2) = (word1.as_bytes(), word2.as_bytes());

    // Allocate memory in one-go, as it is typically faster:
    let mut dist = Vec::with_capacity(word2.len() + 1);

    // Base case: we need to delete j characters in word2 in order to match the empty string word1:
    for j in 0..=word2.len() {
        dist.push(j)
    }

    // Use a second vector to store distances for i - 1.
    // This uses less memory than having a matrix of size (m, n),
    // and we always just use the previous row in the matrix anyway:
    let mut prev_dist = dist.clone();

    for i in 1..=word1.len() {
        for j in 0..=word2.len() {
            if j == 0 {
                dist[j] += 1; // Base case: we need to insert a character in order to match word1.
            } else if word1[i - 1] == word2[j - 1] {
                // No difference, don't increment the edit distance:
                dist[j] = prev_dist[j - 1];
            } else {
                // Either insert, delete or replace a character: increment the edit distance by one:
                dist[j] = dist[j].min(dist[j - 1]).min(prev_dist[j - 1]) + 1;
            }
        }
        prev_dist.copy_from_slice(&dist); // Backup the distances for this row using memcpy.
    }
    dist[word2.len()] as i32
}
