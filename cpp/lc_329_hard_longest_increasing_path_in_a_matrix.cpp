/*
 * @lc app=leetcode id=329 lang=cpp
 *
 * [329] Longest Increasing Path in a Matrix
 *
 * https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
 *
 * algorithms
 * Hard (54.04%)
 * Likes:    9024
 * Dislikes: 136
 * Total Accepted:    556.3K
 * Total Submissions: 1M
 * Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
 *
 * Given an m x n integers matrix, return the length of the longest increasing
 * path in matrix.
 * 
 * From each cell, you can either move in four directions: left, right, up, or
 * down. You may not move diagonally or move outside the boundary (i.e.,
 * wrap-around is not allowed).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
 * Output: 4
 * Explanation: The longest increasing path is [1, 2, 6, 9].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
 * Output: 4
 * Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
 * is not allowed.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: matrix = [[1]]
 * Output: 1
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == matrix.length
 * n == matrix[i].length
 * 1 <= m, n <= 200
 * 0 <= matrix[i][j] <= 2^31 - 1
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
    int longestIncreasingPath(vector<vector<int>> &matrix) {
        // 1. Count the outdegrees of each node (based on increase in value to neighbour)
        // 2. for every outdegree that is 0 we process all the dir that is an out going node and reduce it's outdegree and enqueue these nodes for the next level
        // 3. everytime we do 2. it increases the path length by 1 (all possible path +1 together)
        // 4. repeat this until all outdegree is 0
        //
        // sidenote: no need to check for cycles, since strictly increasing will always have be a DAG
        // Normally in Matrix DFS you can't use topological search, since there is a trivial cycle almost always
        // Question, can we solve this with DFS based topological search? (instead of Kanh's algorithm)  and what' the complexity difference

        // implementation detail, we add buffer around the matrix so that number of edges in buffed graph == number of node in path (think of the case with max len of 1)
        size_t rows, cols;
        rows = matrix.size();
        cols = matrix[0].size();

        // padding
        for (auto &row : matrix) {
            row.insert(row.begin(), INT_MIN);
            row.push_back(INT_MIN);
        }
        matrix.insert(matrix.begin(), vector<int>(cols + 2, INT_MIN));
        matrix.push_back(vector<int>(cols + 2, INT_MIN));
        rows += 2;
        cols += 2;

        vector<vector<int>> outdegrees(rows, vector<int>(cols, 0));
        vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (size_t row = 1; row < rows - 1; row++) {
            for (size_t col = 1; col < cols - 1; col++) {
                for (auto &[dx, dy] : dir) {
                    int x = row + dx;
                    int y = col + dy;
                    if (matrix[row][col] < matrix[x][y])
                        outdegrees[row][col]++;
                }
            }
        }

        vector<pair<int, int>> q, q_swaps;
        for (size_t row = 1; row < rows - 1; row++)
            for (size_t col = 1; col < cols - 1; col++)
                if (outdegrees[row][col] == 0)
                    q.push_back({row, col});

        int layers = 0; // or path length, depending on the analody
        while (!q.empty()) {
            layers++;
            for (auto &[r, c] : q) {
                // [r, c] has outdegree 0
                // we check for all neighours that that points to [r, c] and check cheir out degree
                // i.e. [r, c] is the sink, flowing from [x, y]
                // check if matrix[r, c] > matrix[x, y]
                for (auto &[dx, dy] : dir) {
                    int x = r + dx, y = c + dy;
                    if (matrix[x][y] < matrix[r][c] && --outdegrees[x][y] == 0)
                        q_swaps.push_back({x, y});
                }
            }
            q.clear();
            q = q_swaps;
            q_swaps.clear();
        }

        return layers;
    };
};
// @lc code=end
