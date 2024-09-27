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

// @lc code=start

#include <functional>
#include <string>
#include <vector>
using namespace std;

class Solution {
  public:
    string alienOrder(vector<string> &words) {
        /* 1. build the graph from words directed
         * 2. detect cycle in the graph
         * 3. topological sort
         *    - post order traversal with dfs 
         *    - while eliminating cycles
         *    - what's is indegree? Kahn's algorithm
         */
        // adjacency matrix
        bool nodes[26] = {0};
        vector<vector<bool>> graph(26, vector<bool>(26, false));

        // Build the graph
        // Mark all characters as existing nodes
        // important to note that within a word there is no evidence for any lexicographic relations
        // only in between words. the mere existence only tells you that they exists
        for (auto &word : words)
            for (char c : word)
                nodes[c - 'a'] = true;

        for (size_t i = 0; i < words.size() - 1; i++) {
            auto word1 = words[i];
            auto word2 = words[i + 1];

            if (word1.size() > word2.size() && word2 == word1.substr(0, word2.size()))
                return "";

            for (size_t j = 0; j < min(word1.size(), word2.size()); j++) {
                if (word1[j] != word2[j]) {
                    graph[word1[j] - 'a'][word2[j] - 'a'] = true;
                    break; // only the first different character between the two words will help us find the order
                }
            }
        }

        // Count the number of nodes in the graph
        int graph_size = 0;
        for (size_t i = 0; i < 26; i++)
            if (nodes[i])
                graph_size++;

        // DFS - stack based
        bool visited[26] = {0};
        bool on_path[26] = {0}; // to detect cycles
        string final_dict = "";

        std::function<bool(int)> dfs = [&](int node) -> bool {
            if (on_path[node])
                return false; // cycle detected
            if (visited[node])
                return true;

            visited[node] = true;
            on_path[node] = true;

            for (size_t i = 0; i < 26; i++) {
                if (graph[node][i]) {
                    if (!dfs(i))
                        return false;
                }
            }

            on_path[node] = false; // backtrack path
            final_dict.push_back(node + 'a');
            return true;
        };

        // Perform DFS for each node
        for (size_t i = 0; i < 26; i++) {
            if (nodes[i] && !visited[i]) {
                if (!dfs(i))
                    return ""; // cycle detected
            }
        }

        // Reverse the final dictionary to get the correct order
        reverse(final_dict.begin(), final_dict.end());

        return final_dict.size() == graph_size ? final_dict : "";
    }
};

// @lc code=end