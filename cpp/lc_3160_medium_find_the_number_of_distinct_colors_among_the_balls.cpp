/*
 * @lc app=leetcode id=3160 lang=cpp
 *
 * [3160] Find the Number of Distinct Colors Among the Balls
 *
 * https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/
 *
 * algorithms
 * Medium (41.24%)
 * Likes:    577
 * Dislikes: 61
 * Total Accepted:    116.7K
 * Total Submissions: 221.9K
 * Testcase Example:  '4\n[[1,4],[2,5],[1,3],[3,4]]'
 *
 * You are given an integer limit and a 2D array queries of size n x 2.
 * 
 * There are limit + 1 balls with distinct labels in the range [0, limit].
 * Initially, all balls are uncolored. For every query in queries that is of
 * the form [x, y], you mark ball x with the color y. After each query, you
 * need to find the number of distinct colors among the balls.
 * 
 * Return an array result of length n, where result[i] denotes the number of
 * distinct colors after i^th query.
 * 
 * Note that when answering a query, lack of a color will not be considered as
 * a color.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]
 * 
 * Output: [1,2,2,3]
 * 
 * Explanation:
 * 
 * 
 * 
 * 
 * After query 0, ball 1 has color 4.
 * After query 1, ball 1 has color 4, and ball 2 has color 5.
 * After query 2, ball 1 has color 3, and ball 2 has color 5.
 * After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color
 * 4.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]
 * 
 * Output: [1,2,2,3,4]
 * 
 * Explanation:
 * 
 * 
 * 
 * 
 * After query 0, ball 0 has color 1.
 * After query 1, ball 0 has color 1, and ball 1 has color 2.
 * After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.
 * After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3
 * has color 4.
 * After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has
 * color 4, and ball 4 has color 5.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= limit <= 10^9
 * 1 <= n == queries.length <= 10^5
 * queries[i].length == 2
 * 0 <= queries[i][0] <= limit
 * 1 <= queries[i][1] <= 10^9
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
    vector<int> queryResults(int limit, vector<vector<int>> &queries) {
        int n = queries.size();
        unordered_map<int, int> ball2color, count_color;
        vector<int> result(n);

        for (int i = 0; i < n; i++) {
            int ball = queries[i][0];
            int color = queries[i][1];

            if (ball2color.find(ball) != ball2color.end()) {
                auto prev_color = ball2color[ball];
                count_color[prev_color]--;
                if (count_color[prev_color] == 0) 
                    count_color.erase(prev_color);
            }
            ball2color[ball] = color;
            count_color[color]++;

            result[i] = count_color.size();
        }
        return result;
    }
};
// @lc code=end
