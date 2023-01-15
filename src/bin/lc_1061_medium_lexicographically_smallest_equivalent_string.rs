/*
 * @lc app=leetcode id=1061 lang=rust
 *
 * [1061] Lexicographically Smallest Equivalent String
 *
 * https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/
 *
 * algorithms
 * Medium (73.37%)
 * Likes:    471
 * Dislikes: 34
 * Total Accepted:    17.1K
 * Total Submissions: 23.4K
 * Testcase Example:  '"parker"\n"morris"\n"parser"'
 *
 * You are given two strings of the same length s1 and s2 and a string
 * baseStr.
 *
 * We say s1[i] and s2[i] are equivalent characters.
 *
 *
 * For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' ==
 * 'd', and 'c' == 'e'.
 *
 *
 * Equivalent characters follow the usual rules of any equivalence
 * relation:
 *
 *
 * Reflexivity: 'a' == 'a'.
 * Symmetry: 'a' == 'b' implies 'b' == 'a'.
 * Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
 *
 *
 * For example, given the equivalency information from s1 = "abc" and s2 =
 * "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab"
 * is the lexicographically smallest equivalent string of baseStr.
 *
 * Return the lexicographically smallest equivalent string of baseStr by using
 * the equivalency information from s1 and s2.
 *
 *
 * Example 1:
 *
 *
 * Input: s1 = "parker", s2 = "morris", baseStr = "parser"
 * Output: "makkek"
 * Explanation: Based on the equivalency information in s1 and s2, we can group
 * their characters as [m,p], [a,o], [k,r,s], [e,i].
 * The characters in each group are equivalent and sorted in lexicographical
 * order.
 * So the answer is "makkek".
 *
 *
 * Example 2:
 *
 *
 * Input: s1 = "hello", s2 = "world", baseStr = "hold"
 * Output: "hdld"
 * Explanation: Based on the equivalency information in s1 and s2, we can group
 * their characters as [h,w], [d,e,o], [l,r].
 * So only the second letter 'o' in baseStr is changed to 'd', the answer is
 * "hdld".
 *
 *
 * Example 3:
 *
 *
 * Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
 * Output: "aauaaaaada"
 * Explanation: We group the equivalent characters in s1 and s2 as
 * [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except
 * 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
 *
 *
 *
 * Constraints:
 *
 *
 *
 * 1 <= s1.length, s2.length, baseStr <= 1000
 * s1.length == s2.length
 * s1, s2, and baseStr consist of lowercase English letters.
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn smallest_equivalent_string(s1: String, s2: String, base_str: String) -> String {
        // initialize each character to represent itself
        let mut representation: [usize; 26] = [0; 26];
        for (i, elem) in representation.iter_mut().enumerate() {
            *elem = i;
        }

        fn find(element: usize, representation: &mut [usize]) -> usize {
            let cur_rep = representation[element];
            if element == cur_rep {
                return element;
            }
            representation[element] = find(cur_rep, representation);
            return representation[element];
        }

        let mut union = |a: usize, b: usize| {
            let a = find(a, &mut representation);
            let b = find(b, &mut representation);

            if a == b {
                return;
            } // they are in the same set.
            if a < b {
                representation[b] = a;
            } else {
                representation[a] = b;
            }
        };

        for (a, b) in s1
            .bytes()
            .zip(s2.bytes())
            // first transform char to index before union
            .map(|(a, b)| (a - b'a', b - b'a'))
        {
            union(a as usize, b as usize);
        }
        // handy guide on turning utf8 to String/&str, although useless here
        // https://stackoverflow.com/questions/19076719/how-do-i-convert-a-vector-of-bytes-u8-to-a-string
        return base_str
            .bytes()
            .map(|ch| {
                // take a byte, look for the representation => cast into char
                char::from_u32(
                    (find((ch - b'a') as usize, &mut representation) + 'a' as usize) as u32,
                )
                .unwrap()
            })
            .collect::<String>(); // and collect into String
    }
}

// @lc code=end
use rstest::rstest;

#[rstest]
#[case("hello", "world", "hold", "hdld")]
fn test_smallest_equivalent_string(
    #[case] s1: String,
    #[case] s2: String,
    #[case] base_str: String,
    #[case] expected: String,
) {
    let ans = Solution::smallest_equivalent_string(s1, s2, base_str);
    assert_eq!(ans, expected);
}
fn main() {}
