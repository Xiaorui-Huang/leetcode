/*
 * @lc app=leetcode id=834 lang=rust
 *
 * [834] Sum of Distances in Tree
 *
 * https://leetcode.com/problems/sum-of-distances-in-tree/description/
 *
 * algorithms
 * Hard (54.25%)
 * Likes:    4236
 * Dislikes: 100
 * Total Accepted:    76K
 * Total Submissions: 128.4K
 * Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
 *
 * There is an undirected connected tree with n nodes labeled from 0 to n - 1
 * and n - 1 edges.
 * 
 * You are given the integer n and the array edges where edges[i] = [ai, bi]
 * indicates that there is an edge between nodes ai and bi in the tree.
 * 
 * Return an array answer of length n where answer[i] is the sum of the
 * distances between the i^th node in the tree and all other nodes.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
 * Output: [8,12,6,10,10,10]
 * Explanation: The tree is shown above.
 * We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
 * equals 1 + 1 + 2 + 2 + 2 = 8.
 * Hence, answer[0] = 8, and so on.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 1, edges = []
 * Output: [0]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 2, edges = [[1,0]]
 * Output: [1,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 3 * 10^4
 * edges.length == n - 1
 * edges[i].length == 2
 * 0 <= ai, bi < n
 * ai != bi
 * The given input represents a valid tree.
 * 
 * 
 */

struct Solution;
// @lc code=start
// fricking first time writing rust 😅
impl Solution {
    pub fn sum_of_distances_in_tree(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut graph = vec![vec![]; n as usize];
        
        for edge in edges.iter() {
            let (a, b) = (edge[0] as usize, edge[1] as usize);
            graph[a].push(b);
            graph[b].push(a);
        }
        
        let mut counts = vec![0; n as usize];
        let mut ans = vec![0; n as usize];

        
        fn dfs_count_and_root_dist(node:usize, graph: &Vec<Vec<usize>>, counts: &mut Vec<usize>, ans: &mut Vec<usize>) {
            counts[node] = 1; // mark as visited in dfs
            for &child in graph[node].iter(){
                if counts[child] > 0 {continue} // skip parents
                dfs_count_and_root_dist(child, graph, counts, ans);
                ans[node] += ans[child] + counts[child];
                counts[node] += counts[child];
            }
        }
        fn dfs_infer_dist(node:usize, parent: Option<usize>, graph: &Vec<Vec<usize>>, counts: &Vec<usize>, ans: &mut Vec<usize>, n: usize) {
            for &child in graph[node].iter(){
                if parent.unwrap_or_default() == child {continue} // skip parents
                //if parent.is_some() && parent.unwrap() as usize == child {continue} // skip parents
                ans[child] = ans[node] - counts[child] + (n - counts[child]);
                dfs_infer_dist(child, Some(node), graph, counts, ans, n);
            }
        }
        dfs_count_and_root_dist(0, &graph, &mut counts, &mut ans);
        
        // mark -1 as no parent
        dfs_infer_dist(0, None, &graph, &counts, &mut ans, n as usize);

        return ans.iter().map(|&x| x as i32).collect(); //converting Vec<usize> to Vec<i32>
    }

}
// @lc code=end

fn main(){
    let arr = [[0,1],[0,2],[2,3],[2,4],[2,5]];
    let edges = arr.to_vec().iter().map(|&edge| edge.to_vec()).collect();
    let ans = Solution::sum_of_distances_in_tree(6, edges);
    println!("{:?}", ans);
}
