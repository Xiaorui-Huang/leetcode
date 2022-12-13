/*
 * @lc app=leetcode id=2225 lang=cpp
 *
 * [2225] Find Players With Zero or One Losses
 *
 * https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/
 *
 * algorithms
 * Medium (69.29%)
 * Likes:    569
 * Dislikes: 49
 * Total Accepted:    40.2K
 * Total Submissions: 56.4K
 * Testcase Example:  '[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]'
 *
 * You are given an integer array matches where matches[i] = [winneri, loseri]
 * indicates that the player winneri defeated player loseri in a match.
 *
 * Return a list answer of size 2 where:
 *
 *
 * answer[0] is a list of all players that have not lost any matches.
 * answer[1] is a list of all players that have lost exactly one match.
 *
 *
 * The values in the two lists should be returned in increasing order.
 *
 * Note:
 *
 *
 * You should only consider the players that have played at least one
 * match.
 * The testcases will be generated such that no two matches will have the same
 * outcome.
 *
 *
 *
 * Example 1:
 *
 *
 * Input: matches =
 * [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
 * Output: [[1,2,10],[4,5,7,8]]
 * Explanation:
 * Players 1, 2, and 10 have not lost any matches.
 * Players 4, 5, 7, and 8 each have lost one match.
 * Players 3, 6, and 9 each have lost two matches.
 * Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
 *
 *
 * Example 2:
 *
 *
 * Input: matches = [[2,3],[1,3],[5,4],[6,4]]
 * Output: [[1,2,5,6],[]]
 * Explanation:
 * Players 1, 2, 5, and 6 have not lost any matches.
 * Players 3 and 4 each have lost two matches.
 * Thus, answer[0] = [1,2,5,6] and answer[1] = [].
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= matches.length <= 10^5
 * matches[i].length == 2
 * 1 <= winneri, loseri <= 10^5
 * winneri != loseri
 * All matches[i] are unique.
 *
 *
 */
#include <algorithm>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// not used because of complexity
/**
 * @brief Insert item into sorted vector
 *
 * @tparam T
 * @param vec the vector
 * @param item the item to be inserted
 * @return std::vector<T>::iterator at which the item is inserted
 */
template <typename T> typename std::vector<T>::iterator insert_sorted(std::vector<T> &vec, T const &item) {
    return vec.insert(std::upper_bound(vec.begin(), vec.end(), item), item);
}
// @lc code=start
class Solution {
  public:
    vector<vector<int>> findWinners(vector<vector<int>> &matches) {
        std::unordered_map<int, int> records;
        vector<int> undefeated{}, lost_once{};
        for (auto &&match : matches) {
            auto &winner = match[0], &loser = match[1];
            if (records.find(winner) == records.end()) // not in records
                records[winner] = 0;

            if (records.find(loser) == records.end()) // not in records
                records[loser] = 0;
            records[loser]++;
        }
        for (auto &&record : records) {
            if (record.second == 0)
                undefeated.emplace_back(record.first);
            if (record.second == 1)
                lost_once.emplace_back(record.first);
        }
        sort(undefeated.begin(), undefeated.end());
        sort(lost_once.begin(), lost_once.end());
        return vector<vector<int>>{undefeated, lost_once};
    }
};
// @lc code=end
