#ifndef LC_486_MEDIUM_PREDICT_THE_WINNER_H
#define LC_486_MEDIUM_PREDICT_THE_WINNER_H
/*
 * @lc app=leetcode id=486 lang=cpp
 *
 * [486] Predict the Winner
 *
 * https://leetcode.com/problems/predict-the-winner/description/
 *
 * algorithms
 * Medium (50.81%)
 * Likes:    3514
 * Dislikes: 171
 * Total Accepted:    127.9K
 * Total Submissions: 251.6K
 * Testcase Example:  '[1,5,2]'
 *
 * You are given an integer array nums. Two players are playing a game with
 * this array: player 1 and player 2.
 *
 * Player 1 and player 2 take turns, with player 1 starting first. Both players
 * start the game with a score of 0. At each turn, the player takes one of the
 * numbers from either end of the array (i.e., nums[0] or nums[nums.length -
 * 1]) which reduces the size of the array by 1. The player adds the chosen
 * number to their score. The game ends when there are no more elements in the
 * array.
 *
 * Return true if Player 1 can win the game. If the scores of both players are
 * equal, then player 1 is still the winner, and you should also return true.
 * You may assume that both players are playing optimally.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [1,5,2]
 * Output: false
 * Explanation: Initially, player 1 can choose between 1 and 2.
 * If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If
 * player 2 chooses 5, then player 1 will be left with 1 (or 2).
 * So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
 * Hence, player 1 will never be the winner and you need to return false.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,5,233,7]
 * Output: true
 * Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5
 * and 7. No matter which number player 2 choose, player 1 can choose 233.
 * Finally, player 1 has more score (234) than player 2 (12), so you need to
 * return True representing player1 can win.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 20
 * 0 <= nums[i] <= 10^7
 *
 *
 */

// @lc code=start
#include <iostream>
#include <limits>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}
// class Solution {
//   public:
//     bool PredictTheWinner(vector<int> &nums);
// };

class Solution {
  public:
    bool PredictTheWinner(vector<int> &nums) {
        size_t n = nums.size();
        vector<int> dp(n, 0);
        for (int row = n - 1; row >= 0; row--) {
            dp[row] = nums[row];
            for (size_t col = row + 1; col < n; col++) {
                int front_choice = nums[row] - dp[col];
                int back_choice = nums[col] - dp[col - 1];
                dp[col] = max(front_choice, back_choice);
            }
        }
        return dp[n - 1] >= 0;
    }
};
// @lc code=end
#endif
