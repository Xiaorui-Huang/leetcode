/*
 * @lc app=leetcode id=2246 lang=rust
 *
 * [2246] Longest Path With Different Adjacent Characters
 *
 * https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
 *
 * algorithms
 * Hard (45.21%)
 * Likes:    898
 * Dislikes: 22
 * Total Accepted:    21.6K
 * Total Submissions: 44.1K
 * Testcase Example:  '[-1,0,0,1,1,2]\n"abacbe"'
 *
 * You are given a tree (i.e. a connected, undirected graph that has no cycles)
 * rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
 * represented by a 0-indexed array parent of size n, where parent[i] is the
 * parent of node i. Since node 0 is the root, parent[0] == -1.
 *
 * You are also given a string s of length n, where s[i] is the character
 * assigned to node i.
 *
 * Return the length of the longest path in the tree such that no pair of
 * adjacent nodes on the path have the same character assigned to them.
 *
 *
 * Example 1:
 *
 *
 * Input: parent = [-1,0,0,1,1,2], s = "abacbe"
 * Output: 3
 * Explanation: The longest path where each two adjacent nodes have different
 * characters in the tree is the path: 0 -> 1 -> 3. The length of this path is
 * 3, so 3 is returned.
 * It can be proven that there is no longer path that satisfies the
 * conditions.
 *
 *
 * Example 2:
 *
 *
 * Input: parent = [-1,0,0,0], s = "aabc"
 * Output: 3
 * Explanation: The longest path where each two adjacent nodes have different
 * characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is
 * returned.
 *
 *
 *
 * Constraints:
 *
 *
 * n == parent.length == s.length
 * 1 <= n <= 10^5
 * 0 <= parent[i] <= n - 1 for all i >= 1
 * parent[0] == -1
 * parent represents a valid tree.
 * s consists of only lowercase English letters.
 *
 *
 */

struct Solution;
// @lc code=start
use std::cmp::max;
impl Solution {
    pub fn longest_path(parents: Vec<i32>, s: String) -> i32 {
        let mut tree = vec![vec![]; parents.len()];
        for (i, parent) in parents.into_iter().enumerate() {
            if parent == -1 {
                continue;
            }
            tree[parent as usize].push(i);
        }
        let mut max_path = 1;

        fn find_path(
            node: usize,
            tree: &Vec<Vec<usize>>,
            labels: &[u8],
            max_path: &mut i32,
        ) -> i32 {
            let (mut longest_path, mut second_longest_path) = (0, 0);
            for &child in tree[node].iter() {
                let child_path = find_path(child, tree, labels, max_path);
                if labels[node] == labels[child] {
                    continue;
                }

                if child_path >= longest_path {
                    // destructuring assignment stabilized in 1.59 only 🥲
                    //(longest_path, second_longest_path) = (child_path, longest_path)
                    second_longest_path = longest_path;
                    longest_path = child_path
                } else if child_path > second_longest_path {
                    second_longest_path = child_path
                }
            }
            *max_path = max(*max_path, 1 + longest_path + second_longest_path);
            return 1 + longest_path;
        }

        find_path(0, &tree, s.as_bytes(), &mut max_path);

        return max_path;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![-1, 0, 0, 1, 1, 2], "abacbe", 3)]
#[case(vec![-1, 0, 0, 0], "aabc", 3)]
#[case(vec![-1, 0, 0, 0, 0, 4, 4], "aabceet", 4)]
#[case(vec![-1, 0, 1], "aab", 2)]
#[case(vec![-1], "z", 1)]
#[case(vec![-1, 137, 65, 60, 73, 138, 81, 17, 45, 163, 145, 99, 29, 162, 19, 20, 132, 132, 13, 60, 21, 18, 155, 65, 13, 163, 125, 102, 96, 60, 50, 101, 100, 86, 162, 42, 162, 94, 21, 56, 45, 56, 13, 23, 101, 76, 57, 89, 4, 161, 16, 139, 29, 60, 44, 127, 19, 68, 71, 55, 13, 36, 148, 129, 75, 41, 107, 91, 52, 42, 93, 85, 125, 89, 132, 13, 141, 21, 152, 21, 79, 160, 130, 103, 46, 65, 71, 33, 129, 0, 19, 148, 65, 125, 41, 38, 104, 115, 130, 164, 138, 108, 65, 31, 13, 60, 29, 116, 26, 58, 118, 10, 138, 14, 28, 91, 60, 47, 2, 149, 99, 28, 154, 71, 96, 60, 106, 79, 129, 83, 42, 102, 34, 41, 55, 31, 154, 26, 34, 127, 42, 133, 113, 125, 113, 13, 54, 132, 13, 56, 13, 42, 102, 135, 130, 75, 25, 80, 159, 39, 29, 41, 89, 85, 19, ], "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal", 17)]
fn test_longest_path(#[case] parents: Vec<i32>, #[case] s: String, #[case] expected: i32) {
    assert_eq!(Solution::longest_path(parents, s), expected);
}
fn main() {}
