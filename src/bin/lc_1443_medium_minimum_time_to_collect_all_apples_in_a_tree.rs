/*
* @lc app=leetcode id=1443 lang=rust
*
* [1443] Minimum Time to Collect All Apples in a Tree
*
* https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
*
* algorithms
* Medium (56.06%)
* Likes:    1204
* Dislikes: 95
* Total Accepted:    33.4K
* Total Submissions: 59.4K
* Testcase Example:  '7\n' +
 '[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n' +
 '[false,false,true,false,true,true,false]'
*
* Given an undirected tree consisting of n vertices numbered from 0 to n-1,
* which has some apples in their vertices. You spend 1 second to walk over one
* edge of the tree. Return the minimum time in seconds you have to spend to
* collect all apples in the tree, starting at vertex 0 and coming back to this
* vertex.
*
* The edges of the undirected tree are given in the array edges, where
* edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and
* bi. Additionally, there is a boolean array hasApple, where hasApple[i] =
* true means that vertex i has an apple; otherwise, it does not have any
* apple.
*
*
* Example 1:
*
*
* Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
* [false,false,true,false,true,true,false]
* Output: 8
* Explanation: The figure above represents the given tree where red vertices
* have an apple. One optimal path to collect all apples is shown by the green
* arrows.
*
*
* Example 2:
*
*
* Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
* [false,false,true,false,false,true,false]
* Output: 6
* Explanation: The figure above represents the given tree where red vertices
* have an apple. One optimal path to collect all apples is shown by the green
* arrows.
*
*
* Example 3:
*
*
* Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
* [false,false,false,false,false,false,false]
* Output: 0
*
*
*
* Constraints:
*
*
* 1 <= n <= 10^5
* edges.length == n - 1
* edges[i].length == 2
* 0 <= ai < bi <= n - 1
* fromi < toi
* hasApple.length == n
*
*
*/

use std::vec;

struct Solution;
// @lc code=start

impl Solution {
    pub fn min_time(n: i32, edges: Vec<Vec<i32>>, has_apple: Vec<bool>) -> i32 {
        let mut time = 0;
        let mut graph = vec![vec![]; n as usize];
        for edge in edges {
            let (a, b) = (edge[0] as usize, edge[1] as usize);
            graph[a as usize].push(b);
            graph[b as usize].push(a);
        }
        fn dfs(
            node: usize,
            parent: Option<usize>,
            graph: &Vec<Vec<usize>>,
            has_apple: &Vec<bool>,
            time: &mut i32,
        ) -> bool {
            let mut has_apple_here = has_apple[node];
            for &child in graph[node].iter() {
                if child != parent.unwrap_or(child + 1)
                    && dfs(child, Some(node), graph, has_apple, time)
                {
                    has_apple_here = true;
                    *time += 2;
                }
            }

            return has_apple_here;
        }

        dfs(0 as usize, None, &graph, &has_apple, &mut time);
        return time;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]].to_vec().iter().map(|x|x.to_vec()).collect(), vec![false, false, true, false, false, true, false], 6)]
fn test_min_tim(
    #[case] n: i32,
    #[case] edges: Vec<Vec<i32>>,
    #[case] has_apple: Vec<bool>,
    #[case] expected: i32,
) {
    assert_eq!(Solution::min_time(n, edges, has_apple), expected);
}
fn main() {}
