#ifndef LC_79_MEDIUM_WORD_SEARCH_H
#define LC_79_MEDIUM_WORD_SEARCH_H
/*
 * @lc app=leetcode id=79 lang=cpp
 *
 * [79] Word Search
 *
 * https://leetcode.com/problems/word-search/description/
 *
 * algorithms
 * Medium (41.48%)
 * Likes:    15186
 * Dislikes: 634
 * Total Accepted:    1.5M
 * Total Submissions: 3.7M
 * Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
 *
 * Given an m x n grid of characters board and a string word, return true if
 * word exists in the grid.
 * 
 * The word can be constructed from letters of sequentially adjacent cells,
 * where adjacent cells are horizontally or vertically neighboring. The same
 * letter cell may not be used more than once.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCCED"
 * Output: true
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "SEE"
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
 * = "ABCB"
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * m == board.length
 * n = board[i].length
 * 1 <= m, n <= 6
 * 1 <= word.length <= 15
 * board and word consists of only lowercase and uppercase English letters.
 * 
 * 
 * 
 * Follow up: Could you use search pruning to make your solution faster with a
 * larger board?
 * 
 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;


// @lc code=start
// #define DEBUG

class Solution {
  public:
    bool exist(vector<vector<char>> &board, string word) {
        auto num_rows = board.size();
        auto num_cols = board.at(0).size();
        auto len = word.length();
        const vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        // can use a seen map since, 1 <= m, n <= 6 is small, but will use a modify and revert approach
        auto backtrack = [&](int i, int j, int idx) -> bool {
            auto backtrack_impl = [&](int i, int j, int idx, auto &backtrack_ref) -> bool {
                if (word[idx] != board[i][j])
                    return false;

                if (idx == len - 1)
                    return true;

                bool result = false;

                board[i][j] = '0'; // set as exploring

                for (auto [di, dj] : directions) {
                    auto row = i + di;
                    auto col = j + dj;

                    if (row < 0 || col < 0 || row >= num_rows || col >= num_cols)
                        continue;

                    if (backtrack_ref(row, col, idx + 1, backtrack_ref)) {
                        // don't early return true, instead we save the result, revert the work and then return
                        result = true;
                        break;
                    }
                }

                board[i][j] = word[idx]; // revert back as we have explored
                return result;
            };
            return backtrack_impl(i, j, idx, backtrack_impl);
        };

        for (size_t i = 0; i < num_rows; i++)
            for (size_t j = 0; j < num_cols; j++)
                if (backtrack(i, j, 0)) {
#ifdef DEBUG
                    // ensure the board is reverted back
                    for (size_t i = 0; i < num_rows; i++)
                        for (size_t j = 0; j < num_cols; j++)
                            assert(board[i][j] != '0');
#endif
                    return true;
                }
        return false;
    }
};
// @lc code=end
#endif
