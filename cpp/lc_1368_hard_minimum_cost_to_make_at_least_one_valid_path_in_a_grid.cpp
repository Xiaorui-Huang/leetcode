/*
 * @lc app=leetcode id=1368 lang=cpp
 *
 * [1368] Minimum Cost to Make at Least One Valid Path in a Grid
 *
 * https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/
 *
 * algorithms
 * Hard (62.41%)
 * Likes:    1784
 * Dislikes: 20
 * Total Accepted:    50.5K
 * Total Submissions: 80.8K
 * Testcase Example:  '[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]'
 *
 * Given an m x n grid. Each cell of the grid has a sign pointing to the next
 * cell you should visit if you are currently in this cell. The sign of
 * grid[i][j] can be:
 * 
 * 
 * 1 which means go to the cell to the right. (i.e go from grid[i][j] to
 * grid[i][j + 1])
 * 2 which means go to the cell to the left. (i.e go from grid[i][j] to
 * grid[i][j - 1])
 * 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i +
 * 1][j])
 * 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i -
 * 1][j])
 * 
 * 
 * Notice that there could be some signs on the cells of the grid that point
 * outside the grid.
 * 
 * You will initially start at the upper left cell (0, 0). A valid path in the
 * grid is a path that starts from the upper left cell (0, 0) and ends at the
 * bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
 * path does not have to be the shortest.
 * 
 * You can modify the sign on a cell with cost = 1. You can modify the sign on
 * a cell one time only.
 * 
 * Return the minimum cost to make the grid have at least one valid path.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
 * Output: 3
 * Explanation: You will start at point (0, 0).
 * The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
 * change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) -->
 * (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2,
 * 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
 * The total cost = 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
 * Output: 0
 * Explanation: You can follow the path from (0, 0) to (2, 2).
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[1,2],[4,3]]
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 100
 * 1 <= grid[i][j] <= 4
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
class Solution {
  public:
    vector<pair<int, int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    int minCost(vector<vector<int>> &grid) {
        auto rows = grid.size();
        auto cols = grid[0].size();

        // return -1 if node out of bound
        auto get_node_id = [&](int node, pair<int, int> &dir) -> int {
            int row = node / cols;
            int col = node % cols;

            auto x = row + dir.first, y = col + dir.second;
            if (x < 0 || x >= rows || y < 0 || y >= cols)
                return -1;

            return x * cols + y; // row * num_col + col
        };

        vector<vector<pair<int, bool>>> G(rows * cols);

        int cur_node = 0;
        for (auto &row : grid) {
            for (auto connection : row) {
                connection--; // make into cur_nodex
                for (size_t i = 0; i < 4; i++) {
                    bool weight = (i == connection) ? 0 : 1;
                    int to_node = get_node_id(cur_node, dirs[i]);
                    if (to_node == -1)
                        continue; // out of bound and we skip

                    G[cur_node].push_back({to_node, weight});
                }
                cur_node++;
            }
        }

        vector<int> costs(rows * cols, INT_MAX);
        costs[0] = 0;

        // 0 - 1 BFS (special case of dijkstra's - essentially a PQ that's just 0 or 1, so we don't need a Heap just a deque is good)
        deque<int> q;
        q.push_front(0);

        while (!q.empty()) {
            auto node = q.front();
            q.pop_front();

            if (node == rows * cols - 1)
                return costs[rows * cols - 1];

            for (auto &[neighbor, weight] : G[node]) {
                if (costs[neighbor] <= costs[node] + weight)
                    continue;

                costs[neighbor] = costs[node] + weight;
                if (weight == 0)
                    q.push_front(neighbor);
                else
                    q.push_back(neighbor);
            }
        }

        return costs[rows * cols - 1];
    }
};
// @lc code=end
