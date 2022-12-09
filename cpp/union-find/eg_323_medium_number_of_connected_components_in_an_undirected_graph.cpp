/*
 * @lc app=leetcode id=323 lang=cpp
 *
 * [323] Number of Connected Components in an Undirected Graph
 *
 * https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
 *
 * algorithms
 * Medium (62.13%)
 * Likes:    2320
 * Dislikes: 80
 * Total Accepted:    310.1K
 * Total Submissions: 499.1K
 * Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
 *
 * You have a graph of n nodes. You are given an integer n and an array edges
 * where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
 * in the graph.
 *
 * Return the number of connected components in the graph.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 5, edges = [[0,1],[1,2],[3,4]]
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
 * Output: 1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 2000
 * 1 <= edges.length <= 5000
 * edges[i].length == 2
 * 0 <= ai <= bi < n
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
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// @lc code=start

// NB: leetcode official Disjoint set union solution
class Solution {
  public:
    int find(vector<int> &representative, int vertex) {
        if (vertex == representative[vertex])
            return vertex;

        return representative[vertex] = find(representative, representative[vertex]);
    }

    int combine(vector<int> &representative, vector<int> &size, int vertex1, int vertex2) {
        vertex1 = find(representative, vertex1);
        vertex2 = find(representative, vertex2);

        if (vertex1 == vertex2)
            return 0;
        else {

            if (size[vertex1] > size[vertex2]) {
                size[vertex1] += size[vertex2];
                representative[vertex2] = vertex1;
            } else {
                size[vertex2] += size[vertex1];
                representative[vertex1] = vertex2;
            }
            return 1;
        }
    }

    int countComponents(int n, vector<vector<int>> &edges) {
        vector<int> representative(n), size(n);

        for (int i = 0; i < n; i++) {
            representative[i] = i;
            size[i] = 1;
        }

        int components = n;
        for (int i = 0; i < edges.size(); i++)
            components -= combine(representative, size, edges[i][0], edges[i][1]);

        return components;
    }
};
// @lc code=end
