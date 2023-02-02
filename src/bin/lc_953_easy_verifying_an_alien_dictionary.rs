/*
 * @lc app=leetcode id=953 lang=rust
 *
 * [953] Verifying an Alien Dictionary
 *
 * https://leetcode.com/problems/verifying-an-alien-dictionary/description/
 *
 * algorithms
 * Easy (52.78%)
 * Likes:    3514
 * Dislikes: 1156
 * Total Accepted:    394.8K
 * Total Submissions: 742.3K
 * Testcase Example:  '["hello","leetcode"]\n"hlabcdefgijkmnopqrstuvwxyz"'
 *
 * In an alien language, surprisingly, they also use English lowercase letters,
 * but possibly in a different order. The order of the alphabet is some
 * permutation of lowercase letters.
 *
 * Given a sequence of words written in the alien language, and the order of
 * the alphabet, return true if and only if the given words are sorted
 * lexicographically in this alien language.
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
 * Output: true
 * Explanation: As 'h' comes before 'l' in this language, then the sequence is
 * sorted.
 *
 *
 * Example 2:
 *
 *
 * Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
 * Output: false
 * Explanation: As 'd' comes after 'l' in this language, then words[0] >
 * words[1], hence the sequence is unsorted.
 *
 *
 * Example 3:
 *
 *
 * Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
 * Output: false
 * Explanation: The first three characters "app" match, and the second string
 * is shorter (in size.) According to lexicographical rules "apple" > "app",
 * because 'l' > '∅', where '∅' is defined as the blank character which is less
 * than any other character (More info).
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 100
 * 1 <= words[i].length <= 20
 * order.length == 26
 * All characters in words[i] and order are English lowercase letters.
 *
 *
 */

struct Solution;
// @lc code=start
use std::collections::HashMap;

impl Solution {
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        let mut lexi = HashMap::new();
        for (i, ch) in order.chars().enumerate() {
            lexi.insert(ch, i);
        }

        let alien_lexi_ordered = |word1: &String, word2: &String| -> bool {
            for (ch1, ch2) in word1.chars().zip(word2.chars()) {
                let (pos1, pos2) = (lexi.get(&ch1).unwrap(), lexi.get(&ch2).unwrap());
                if pos1 < pos2 {
                    return true;
                } else if pos1 > pos2 {
                    return false;
                }
            }
            return word1.len() <= word2.len();
        };
        let mut word_iter = words.into_iter();
        let mut cur_word = word_iter.next().unwrap();
        for word in word_iter {
            if !alien_lexi_ordered(&cur_word, &word) {
                return false;
            }
            cur_word = word;
        }
        return true;
    }
}
// @lc code=end

fn main() {}
