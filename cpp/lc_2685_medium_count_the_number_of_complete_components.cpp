/*
 * @lc app=leetcode id=2685 lang=cpp
 *
 * [2685] Count the Number of Complete Components
 *
 * https://leetcode.com/problems/count-the-number-of-complete-components/description/
 *
 * algorithms
 * Medium (65.04%)
 * Likes:    585
 * Dislikes: 14
 * Total Accepted:    23.1K
 * Total Submissions: 35.6K
 * Testcase Example:  '6\n[[0,1],[0,2],[1,2],[3,4]]'
 *
 * You are given an integer n. There is an undirected graph with n vertices,
 * numbered from 0 to n - 1. You are given a 2D integer array edges where
 * edges[i] = [ai, bi] denotes that there exists an undirected edge connecting
 * vertices ai and bi.
 * 
 * Return the number of complete connected components of the graph.
 * 
 * A connected component is a subgraph of a graph in which there exists a path
 * between any two vertices, and no vertex of the subgraph shares an edge with
 * a vertex outside of the subgraph.
 * 
 * A connected component is said to be complete if there exists an edge between
 * every pair of its vertices.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
 * Output: 3
 * Explanation: From the picture above, one can see that all of the components
 * of this graph are complete.
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
 * Output: 1
 * Explanation: The component containing vertices 0, 1, and 2 is complete since
 * there is an edge between every pair of two vertices. On the other hand, the
 * component containing vertices 3, 4, and 5 is not complete since there is no
 * edge between vertices 4 and 5. Thus, the number of complete components in
 * this graph is 1.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 50
 * 0 <= edges.length <= n * (n - 1) / 2
 * edges[i].length == 2
 * 0 <= ai, bi <= n - 1
 * ai != bi
 * There are no repeated edges.
 * 
 * 
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
  public:
    unordered_set<int> seen;
    bool dfs(int node, vector<vector<int>> &graph) {
        if (seen.count(node))
            return false;

        vector<int> stack;
        stack.push_back(node);

        size_t node_count = 0;
        size_t edge_count = 0;

        while (!stack.empty()) {
            node = stack.back();
            stack.pop_back();
            if(seen.count(node))
                continue;
            seen.insert(node);
            node_count++;

            for (auto &adj : graph[node])
                if (!seen.count(adj)) {
                    stack.push_back(adj);
                    edge_count++;
                }
        }

        // if V is a complete graph and |V| = n -> |E| = n(n-1)/2
        return (node_count * (node_count - 1) / 2) == edge_count;
    }

    int countCompleteComponents(int n, vector<vector<int>> &edges) {
        vector<vector<int>> graph(n);
        for (auto &edge : edges) {
            graph[edge.front()].push_back(edge.back());
            graph[edge.back()].push_back(edge.front());
        }

        size_t complete_count = 0;
        for (int i = 0; i < n; i++) 
            if (dfs(i, graph))
                complete_count++;

        return complete_count;
    }
};
// @lc code=end
