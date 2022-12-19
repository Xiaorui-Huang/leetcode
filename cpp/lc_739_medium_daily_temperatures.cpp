#ifndef LC_739_MEDIUM_DAILY_TEMPERATURES_H
#define LC_739_MEDIUM_DAILY_TEMPERATURES_H
/*
 * @lc app=leetcode id=739 lang=cpp
 *
 * [739] Daily Temperatures
 *
 * https://leetcode.com/problems/daily-temperatures/description/
 *
 * algorithms
 * Medium (66.61%)
 * Likes:    9736
 * Dislikes: 224
 * Total Accepted:    550.4K
 * Total Submissions: 828.1K
 * Testcase Example:  '[73,74,75,71,69,72,76,73]'
 *
 * Given an array of integers temperatures represents the daily temperatures,
 * return an array answer such that answer[i] is the number of days you have to
 * wait after the i^th day to get a warmer temperature. If there is no future
 * day for which this is possible, keep answer[i] == 0 instead.
 *
 *
 * Example 1:
 * Input: temperatures = [73,74,75,71,69,72,76,73]
 * Output: [1,1,4,2,1,1,0,0]
 * Example 2:
 * Input: temperatures = [30,40,50,60]
 * Output: [1,1,1,0]
 * Example 3:
 * Input: temperatures = [30,60,90]
 * Output: [1,1,0]
 *
 *
 * Constraints:
 *
 *
 * 1 <= temperatures.length <= 10^5
 * 30 <= temperatures[i] <= 100
 *
 *
 */
#include <stack>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
  public:
    vector<int> dailyTemperatures(vector<int> &temperatures) {
        vector<int> ans(temperatures.size(), 0);
        stack<int> stack;
        for (size_t i = 0; i < temperatures.size(); i++) {
            while (!stack.empty() && temperatures[stack.top()] < temperatures[i]) {
                auto cur_i = stack.top();
                ans[cur_i] = i - cur_i;
                stack.pop();
            }
            stack.push(i);
        }
        return ans;
    }
};
// @lc code=end

#endif
