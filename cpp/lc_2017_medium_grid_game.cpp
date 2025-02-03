/*
 * @lc app=leetcode id=2017 lang=cpp
 *
 * [2017] Grid Game
 *
 * https://leetcode.com/problems/grid-game/description/
 *
 * algorithms
 * Medium (46.21%)
 * Likes:    1629
 * Dislikes: 79
 * Total Accepted:    112.5K
 * Total Submissions: 186K
 * Testcase Example:  '[[2,5,4],[1,5,1]]'
 *
 * You are given a 0-indexed 2D array grid of size 2 x n, where grid[r][c]
 * represents the number of points at position (r, c) on the matrix. Two robots
 * are playing a game on this matrix.
 * 
 * Both robots initially start at (0, 0) and want to reach (1, n-1). Each robot
 * may only move to the right ((r, c) to (r, c + 1)) or down ((r, c) to (r + 1,
 * c)).
 * 
 * At the start of the game, the first robot moves from (0, 0) to (1, n-1),
 * collecting all the points from the cells on its path. For all cells (r, c)
 * traversed on the path, grid[r][c] is set to 0. Then, the second robot moves
 * from (0, 0) to (1, n-1), collecting the points on its path. Note that their
 * paths may intersect with one another.
 * 
 * The first robot wants to minimize the number of points collected by the
 * second robot. In contrast, the second robot wants to maximize the number of
 * points it collects. If both robots play optimally, return the number of
 * points collected by the second robot.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: grid = [[2,5,4],[1,5,1]]
 * Output: 4
 * Explanation: The optimal path taken by the first robot is shown in red, and
 * the optimal path taken by the second robot is shown in blue.
 * The cells visited by the first robot are set to 0.
 * The second robot will collect 0 + 0 + 4 + 0 = 4 points.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: grid = [[3,3,1],[8,5,2]]
 * Output: 4
 * Explanation: The optimal path taken by the first robot is shown in red, and
 * the optimal path taken by the second robot is shown in blue.
 * The cells visited by the first robot are set to 0.
 * The second robot will collect 0 + 3 + 1 + 0 = 4 points.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: grid = [[1,3,1,15],[1,3,3,1]]
 * Output: 7
 * Explanation: The optimal path taken by the first robot is shown in red, and
 * the optimal path taken by the second robot is shown in blue.
 * The cells visited by the first robot are set to 0.
 * The second robot will collect 0 + 1 + 3 + 3 + 0 = 7 points.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * grid.length == 2
 * n == grid[r].length
 * 1 <= n <= 5 * 10^4
 * 1 <= grid[r][c] <= 10^5
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
    long long gridGame(vector<vector<int>> &grid) {
        int n = grid.front().size();
        vector<long long> p1(n + 1, 0), p2(n + 1, 0);

        for (int i = 1; i <= n; i++)
            p1[i] = p1[i - 1] + grid[0][i - 1];

        for (int i = 1; i <= n; i++)
            p2[i] = p2[i - 1] + grid[1][i - 1];

        long long result = LLONG_MAX;
        for (int i = 1; i <= n; i++) {
            long long rob2_score = max(p2[i - 1], p1[n] - p1[i]);
            if (rob2_score < result)
                result = rob2_score;
        }
        return result;
    }
};
// @lc code=end
