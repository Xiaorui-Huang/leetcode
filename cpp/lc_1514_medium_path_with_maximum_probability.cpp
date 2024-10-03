/*
 * @lc app=leetcode id=1514 lang=cpp
 *
 * [1514] Path with Maximum Probability
 *
 * https://leetcode.com/problems/path-with-maximum-probability/description/
 *
 * algorithms
 * Medium (54.66%)
 * Likes:    3535
 * Dislikes: 95
 * Total Accepted:    242.2K
 * Total Submissions: 394.7K
 * Testcase Example:  '3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2'
 *
 * You are given an undirected weighted graph of n nodes (0-indexed),
 * represented by an edge list where edges[i] = [a, b] is an undirected edge
 * connecting the nodes a and b with a probability of success of traversing
 * that edge succProb[i].
 * 
 * Given two nodes start and end, find the path with the maximum probability of
 * success to go from start to end and return its success probability.
 * 
 * If there is no path from start to end, return 0. Your answer will be
 * accepted if it differs from the correct answer by at most 1e-5.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start =
 * 0, end = 2
 * Output: 0.25000
 * Explanation: There are two paths from start to end, one having a probability
 * of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start =
 * 0, end = 2
 * Output: 0.30000
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
 * Output: 0.00000
 * Explanation: There is no path between 0 and 2.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= n <= 10^4
 * 0 <= start, end < n
 * start != end
 * 0 <= a, b < n
 * a != b
 * 0 <= succProb.length == edges.length <= 2*10^4
 * 0 <= succProb[i] <= 1
 * There is at most one edge between every two nodes.
 * 
 * 
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <queue>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

#define SET 0
#define MAX_HEAP 1

// #define DS SET
#define DS MAX_HEAP

// @lc code=start
class Solution {
  public:
    double maxProbability(int n,
                          vector<vector<int>> &edges,
                          vector<double> &succProb,
                          int start_node,
                          int end_node) {

        // we use dijstraks here since 0 <= probs, so djikstra can handle it.
        // gotta build graph (adjacency matrix from edges)
        vector<vector<pair<int, double>>> graph(n, vector<pair<int, double>>());
        for (size_t i = 0; i < edges.size(); i++) {
            auto w = succProb[i];
            auto u = edges[i][0], v = edges[i][1];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }

        // will use dijkstras
        vector<double> probs(n, 0.0);
        probs[start_node] = 1.0;
#if DS == SET
        set<pair<double, int>> PQ; // max prob, node (max probs here is only used for PQ sorting)
        PQ.insert({1, start_node});

        while (!PQ.empty()) {
            // to get the max element from the PQ, we have to get prev from end
            auto max_prob_pair = prev(PQ.end());
            int node = max_prob_pair->second;
            if (node == end_node)
                return probs[end_node];

            PQ.erase(max_prob_pair);

            for (auto &[neighbor, edge_prob] : graph[node]) {
                if (probs[neighbor] < probs[node] * edge_prob) {
                    if (probs[neighbor] != 0)
                        PQ.erase({probs[neighbor], neighbor});

                    probs[neighbor] = probs[node] * edge_prob;
                    PQ.insert({probs[neighbor], neighbor});
                }
            }
        }
#elif DS == MAX_HEAP
        priority_queue<pair<double, int>> PQ;
        PQ.push({probs[start_node], start_node});

        while (!PQ.empty()) {
            auto u = PQ.top().second;
            PQ.pop();

            if (u == end_node)
                return probs[u];

            for (auto &[v, prob] : graph[u]) {
                if (probs[u] + prob > probs[v]) {
                    probs[v] = probs[u] + prob;
                    PQ.push({probs[v], v});
                }
            }
        }

#endif

        return probs[end_node];
    }
};
// @lc code=end
