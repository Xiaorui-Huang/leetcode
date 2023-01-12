/*
 * @lc app=leetcode id=1519 lang=rust
 *
 * [1519] Number of Nodes in the Sub-Tree With the Same Label
 *
 * https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/description/
 *
 * algorithms
 * Medium (41.02%)
 * Likes:    1734
 * Dislikes: 704
 * Total Accepted:    61.3K
 * Total Submissions: 112.5K
 * Testcase Example:  '7\n[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n"abaedcd"'
 *
 * You are given a tree (i.e. a connected, undirected graph that has no cycles)
 * consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The
 * root of the tree is the node 0, and each node of the tree has a label which
 * is a lower-case character given in the string labels (i.e. The node with the
 * number i has the label labels[i]).
 *
 * The edges array is given on the form edges[i] = [ai, bi], which means there
 * is an edge between nodes ai and bi in the tree.
 *
 * Return an array of size n where ans[i] is the number of nodes in the subtree
 * of the i^th node which have the same label as node i.
 *
 * A subtree of a tree T is the tree consisting of a node in T and all of its
 * descendant nodes.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels =
 * "abaedcd"
 * Output: [2,1,1,1,1,1,1]
 * Explanation: Node 0 has label 'a' and its sub-tree has node 2 with label 'a'
 * as well, thus the answer is 2. Notice that any node is part of its sub-tree.
 * Node 1 has a label 'b'. The sub-tree of node 1 contains nodes 1,4 and 5, as
 * nodes 4 and 5 have different labels than node 1, the answer is just 1 (the
 * node itself).
 *
 *
 * Example 2:
 *
 *
 * Input: n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
 * Output: [4,2,1,1]
 * Explanation: The sub-tree of node 2 contains only node 2, so the answer is
 * 1.
 * The sub-tree of node 3 contains only node 3, so the answer is 1.
 * The sub-tree of node 1 contains nodes 1 and 2, both have label 'b', thus the
 * answer is 2.
 * The sub-tree of node 0 contains nodes 0, 1, 2 and 3, all with label 'b',
 * thus the answer is 4.
 *
 *
 * Example 3:
 *
 *
 * Input: n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
 * Output: [3,2,1,1,1]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 10^5
 * edges.length == n - 1
 * edges[i].length == 2
 * 0 <= ai, bi < n
 * ai != bi
 * labels.length == n
 * labels is consisting of only of lowercase English letters.
 *
 *
 */

struct Solution;
// @lc code=start
use std::collections::HashMap;
impl Solution {
    pub fn count_sub_trees(n: i32, edges: Vec<Vec<i32>>, labels: String) -> Vec<i32> {
        let mut graph = vec![vec![]; n as usize];
        for edge in edges {
            let (a, b) = (edge[0] as usize, edge[1] as usize);
            graph[a].push(b);
            graph[b].push(a);
        }

        let mut ans = vec![0; n as usize];
        fn dfs(
            node: usize,
            parent: Option<usize>,
            graph: &Vec<Vec<usize>>,
            labels: &[u8],
            ans: &mut Vec<i32>,
        ) -> [i32; 26] {
            let label = (labels[node] - b'a') as usize;
            let mut counts = [0; 26];
            counts[label] += 1;

            for &child in graph[node].iter() {
                if child != parent.unwrap_or(child + 1) {
                    let child_counts = dfs(child, Some(node), graph, labels, ans);
                    for (i, count) in child_counts.into_iter().enumerate() {
                        counts[i] += count;
                    }
                }
            }
            ans[node] = counts[label];

            return counts;
        }
        dfs(0, None, &graph, &labels.as_bytes(), &mut ans);

        return ans;
    }
}
// @lc code=end

fn main() {}
