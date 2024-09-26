/*
 * @lc app=leetcode id=269 lang=cpp
 *
 * [269] Alien Dictionary
 *
 * https://leetcode.com/problems/alien-dictionary/description/
 *
 * algorithms
 * Hard (37.60%)
 * Likes:    6903
 * Dislikes: 1193
 * Total Accepted:    426.5K
 * Total Submissions: 1.1M
 * Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
 *
 * There is a new alien language that uses the English alphabet. However, the
 * order among letters is unknown to you. You are given a list of strings
 * words from the alien language, sorted lexicographically by the rules of
 * this new language.
 *
 * You must derive the order of letters in this language.
 *
 * Return a string of the unique letters in the new alien language sorted in
 * lexicographically increasing order by the new language's rules. If there is
 * no solution, return "". If there are multiple solutions, return any of them.
 *
 * A string words[i] is lexicographically smaller than words[i+1] if and only
 * if at the first differing character from left to right, the character in
 * words[i] comes before the character in words[i+1] in the alien language.
 *
 * If the prefix of words[i] is the same as words[i+1], and words[i] is
 * longer than words[i+1], return "".
 *
 *
 * Example 1:
 *
 *
 * Input: words = ["wrt","wrf","er","ett","rftt"]
 * Output: "wertf"
 *
 *
 * Example 2:
 *
 *
 * Input: words = ["z","x"]
 * Output: "zx"
 *
 *
 * Example 3:
 *
 *
 * Input: words = ["z","x","z"]
 * Output: ""
 * Explanation: The order is invalid, so return "".
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 100
 * 1 <= words[i].length <= 100
 * words[i] consists of only lowercase English letters.
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
        os << (char)element << " ";
    return os;
}

// @lc code=start

class Solution {
  public:
    string alienOrder(vector<string> &words) {
        /* 1. build the graph from words directed
         * 2. detect cycle in the graph
         * 3. topological sort
         *    - post order traversal using stack (dfs)
         *    - what's is indegree? Kahn's algorithm
         */

        vector<vector<bool>> graph(26, vector<bool>(26, false));

        for (size_t i = 1; i < words.size(); i++) {
            auto word1 = words[i - 1];
            auto word2 = words[i];
            if (word1.size() > word2.size() && word2 == word1.substr(0, word2.size()))
                return "";

            for (size_t i = 0; i < min(word1.size(), word2.size()); i++) {
                if (word1[i] != word2[i]) {
                    graph[word1[i] - 'a'][word2[i] - 'a'] = true;
                }
            }
        }

        return "";
    }
};

// @lc code=end
