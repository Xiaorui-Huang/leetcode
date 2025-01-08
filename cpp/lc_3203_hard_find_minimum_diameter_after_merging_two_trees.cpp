/*
 * @lc app=leetcode id=3203 lang=cpp
 *
 * [3203] Find Minimum Diameter After Merging Two Trees
 *
 * https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/description/
 *
 * algorithms
 * Hard (35.85%)
 * Likes:    618
 * Dislikes: 38
 * Total Accepted:    71.4K
 * Total Submissions: 123K
 * Testcase Example:  '[[0,1],[0,2],[0,3]]\n[[0,1]]'
 *
 * There exist two undirected trees with n and m nodes, numbered from 0 to n -
 * 1 and from 0 to m - 1, respectively. You are given two 2D integer arrays
 * edges1 and edges2 of lengths n - 1 and m - 1, respectively, where edges1[i]
 * = [ai, bi] indicates that there is an edge between nodes ai and bi in the
 * first tree and edges2[i] = [ui, vi] indicates that there is an edge between
 * nodes ui and vi in the second tree.
 * 
 * You must connect one node from the first tree with another node from the
 * second tree with an edge.
 * 
 * Return the minimum possible diameter of the resulting tree.
 * 
 * The diameter of a tree is the length of the longest path between any two
 * nodes in the tree.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: edges1 = [[0,1],[0,2],[0,3]], edges2 = [[0,1]]
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * We can obtain a tree of diameter 3 by connecting node 0 from the first tree
 * with any node from the second tree.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: edges1 = [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]], edges2 =
 * [[0,1],[0,2],[0,3],[2,4],[2,5],[3,6],[2,7]]
 * 
 * Output: 5
 * 
 * Explanation:
 * 
 * We can obtain a tree of diameter 5 by connecting node 0 from the first tree
 * with node 0 from the second tree.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n, m <= 10^5
 * edges1.length == n - 1
 * edges2.length == m - 1
 * edges1[i].length == edges2[i].length == 2
 * edges1[i] = [ai, bi]
 * 0 <= ai, bi < n
 * edges2[i] = [ui, vi]
 * 0 <= ui, vi < m
 * The input is generated such that edges1 and edges2 represent valid trees.
 * 
 * 
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

// @lc code=start
// we need to find the centroid of the tree -> until the queue has 2 or 1 nodes left, (centred at a node or an edge)
// but here we can run double dfs/bfs on each tree and return (min-diameter1 + min-diameter2) / 2

// #define CEIL_DIV(a, b) 1 + ((((a) - 1)) / (b)) // if a != 0 and this avoids overflow
#define CEIL_DIV(a, b) ((a) + (b) - 1) / (b)

#define BFS 0
#define LEAF_RM 1

// #define APPR BFS
#define APPR LEAF_RM

class Solution {
  public:
    int minimumDiameterAfterMerge(vector<vector<int>> &edges1, vector<vector<int>> &edges2) {
        int n = edges1.size() + 1, m = edges2.size() + 1;

        vector<vector<int>> G1(n);
        vector<vector<int>> G2(m);
        for (auto e : edges1) {
            G1[e[0]].push_back(e[1]);
            G1[e[1]].push_back(e[0]);
        }

        for (auto e : edges2) {
            G2[e[0]].push_back(e[1]);
            G2[e[1]].push_back(e[0]);
        }

#if APPR == BFS
        // we use double bfs to find the furthest node from root 0, a
        // then we do bfs again from a to find the furthurest node b
        auto [_1, a1] = bfs(G1, 0);
        auto [diameter1, b1] = bfs(G1, a1);

        // diameter = a <-> b
        // c is in the middle
        auto [_2, a2] = bfs(G2, 0);
        auto [diameter2, b2] = bfs(G2, a2);
        // cout << "D1: " << diameter1 << " D2: " << diameter2 << "\n";
#elif APPR == LEAF_RM
        auto [diameter1, center1] = leaf_removal(G1);
        auto [diameter2, center2] = leaf_removal(G2);
#endif
        return max({diameter1, diameter2, CEIL_DIV(diameter1, 2) + CEIL_DIV(diameter2, 2) + 1});
    }

    /**
     * @brief Use leaf removal to find the diameter and center of the tree
     * 
     * @param G adjacency list of the graph
     * @return pair<int, int> {diamater, center node}
     */
    pair<int, int> leaf_removal(vector<vector<int>> &G) {
        int n = G.size();
        vector<int> degrees(n);
        queue<int> q;
        for (size_t i = 0; i < n; i++) {
            degrees[i] = G[i].size();
            if (degrees[i] == 1)
                q.push(i);
        }

        int layer = 0;
        int count = n;
        while (count > 2) {
            int q_size = q.size();
            for (size_t i = 0; i < q_size; i++) {
                int leaf = q.front();
                q.pop();
                degrees[leaf]--;
                for (auto parent : G[leaf]) {
                    degrees[parent]--;
                    if (degrees[parent] == 1)
                        q.push(parent);
                }
            }
            count -= q_size;
            layer++;
        }

        if (count == 1)
            return {2 * layer, q.front()};

        return {2 * layer + 1, q.front()};
    }

    /**
     * @brief return the max path length explored by bfs and the furthurest node from root
     * if there is a tie in the furthurest node then we pick any one of them
     * 
     * @param G adjcency list of the graph
     * @param root starting node for bfs
     * @return pair<int, int> 
     */
    pair<int, int> bfs(vector<vector<int>> &G, int root) {
        vector<bool> seen(G.size(), false);
        int depth = 0;
        int furthest_node = 0;
        queue<int> q;
        q.push(root);
        seen[root] = true;
        while (!q.empty()) {
            int q_size = q.size();
            depth++;
            for (int i = 0; i < q_size; i++) {
                int cur = q.front();
                furthest_node = cur;
                q.pop();
                for (auto neighbour : G[cur]) {
                    if (seen[neighbour])
                        continue;

                    seen[neighbour] = true;
                    q.push(neighbour);
                }
            }
        }
        return {depth - 1, furthest_node};
    }
};
// @lc code=end
