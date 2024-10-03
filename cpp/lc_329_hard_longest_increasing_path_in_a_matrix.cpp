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

#define KAHN_ALGO 0
#define DFS_MEMO 1

// #define APPR DFS_MEMO
#define APPR KAHN_ALGO

// @lc code=start
class Solution {
  public:
    vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
#if APPR == KAN_ALGO
    int longestIncreasingPath(vector<vector<int>> &matrix) {
        // 1. Count the outdegrees of each node (based on increase in value to neighbour)
        // 2. for every outdegree that is 0 we process all the dir that is an outgoing node
        //    and reduce its outdegree and enqueue these nodes for the next level.
        // 3. every time we do 2, it increases the path length by 1 (all possible path +1 together)
        // 4. repeat this until all outdegrees are 0
        //
        // sidenote: no need to check for cycles, since strictly increasing will always be a DAG.
        // Normally in Matrix DFS you can't use topological search, since there is a trivial cycle almost always.

        // Question: can we solve this with DFS-based topological search? (instead of Kahn's algorithm) and what's the complexity difference?

        // implementation detail, we add buffer around the matrix so that number of edges in the buffed graph
        // equals the number of nodes in the path (think of the case with max len of 1).

        int rows = matrix.size();
        if (rows == 0)
            return 0;
        int cols = matrix[0].size();

        // Inline helper for bound check
        auto in_bounds = [&](int x, int y) { return x >= 0 && x < rows && y >= 0 && y < cols; };

        // outdegrees array
        vector<vector<int>> outdegrees(rows, vector<int>(cols, 0));

        // O(mn)
        // Calculate outdegrees based on neighbors
        for (int row = 0; row < rows; row++)
            for (int col = 0; col < cols; col++)
                for (auto &[dx, dy] : dir) {
                    int x = row + dx;
                    int y = col + dy;
                    if (in_bounds(x, y) && matrix[row][col] < matrix[x][y])
                        outdegrees[row][col]++;
                }

        // O(mn)
        // Start BFS from nodes with outdegree == 0
        vector<pair<int, int>> queue;
        for (int row = 0; row < rows; row++)
            for (int col = 0; col < cols; col++)
                if (outdegrees[row][col] == 0)
                    queue.push_back({row, col});

        // O(mn) -> on the worst case we have an Edge between all, and that is bounded by mn in a matrix
        int layers = 0; // or path length, depending on the analogy
        while (!queue.empty()) {
            vector<pair<int, int>> next_queue;
            layers++;

            // anchor at rc, probe it's neighbors [x, y] = [r + dx, c + dy]
            for (auto &[r, c] : queue)
                for (auto &[dx, dy] : dir) {
                    // [r, c] has outdegree 0
                    // We check for all neighbors that point to [r, c] and reduce their outdegree.
                    // [r, c] is the sink, flowing from [x, y]. We check if matrix[r, c] > matrix[x, y].
                    int x = r + dx;
                    int y = c + dy;
                    if (in_bounds(x, y) && matrix[x][y] < matrix[r][c] && --outdegrees[x][y] == 0)
                        next_queue.push_back({x, y});
                }

            queue = std::move(next_queue); // Avoid copying vectors by using std::move
        }

        return layers;
    }
#elif APPR == DFS_MEMO
    // Directions for moving in the matrix: right, left, down, up

    int longestIncreasingPath(vector<vector<int>> &matrix) {

        int rows = matrix.size(), cols = matrix[0].size();
        // Memoization table to store the longest path starting from each cell
        vector<vector<int>> memo(rows, vector<int>(cols, 0));

        int maxPath = 0;
        // Try DFS from each cell
        for (int r = 0; r < rows; ++r)
            for (int c = 0; c < cols; ++c)
                maxPath = max(maxPath, dfs(matrix, memo, r, c));
        return maxPath;
    }

    int dfs(const vector<vector<int>> &matrix, vector<vector<int>> &memo, int r, int c) {
        // If this cell is already visited, return the stored result
        if (memo[r][c] != 0)
            return memo[r][c];

        int maxLength = 1; // The length of the path starting from this cell (itself)
        for (auto [dx, dy] : dir) {
            int x = r + dx, y = c + dy;
            // Ensure we stay within bounds and the next cell has a strictly greater value
            if (x >= 0 && x < matrix.size() && y >= 0 && y < matrix[0].size())
                if (matrix[x][y] > matrix[r][c])
                    maxLength = max(maxLength, 1 + dfs(matrix, memo, x, y));
        }

        memo[r][c] = maxLength; // Store the result for future calls
        return maxLength;
    }
#endif
};

// @lc code=end
