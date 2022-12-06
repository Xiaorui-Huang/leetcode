/*
 * @lc app=leetcode id=472 lang=cpp
 *
 * [472] Concatenated Words
 *
 * https://leetcode.com/problems/concatenated-words/description/
 *
 * algorithms
 * Hard (45.49%)
 * Likes:    2347
 * Dislikes: 236
 * Total Accepted:    157.2K
 * Total Submissions: 343.4K
 * Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
 *
 * Given an array of strings words (without duplicates), return all the
 * concatenated words in the given list of words.
 *
 * A concatenated word is defined as a string that is comprised entirely of at
 * least two shorter words in the given array.
 *
 *
 * Example 1:
 *
 *
 * Input: words =
 * ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
 * Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
 * Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
 * "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
 * "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
 *
 * Example 2:
 *
 *
 * Input: words = ["cat","dog","catdog"]
 * Output: ["catdog"]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= words.length <= 10^4
 * 1 <= words[i].length <= 30
 * words[i] consists of only lowercase English letters.
 * All the strings of words are unique.
 * 1 <= sum(words[i].length) <= 10^5
 *
 *
 */
#include <algorithm>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// @lc code=start
// TODO implement trie approach
#define APPR DP

enum appr { DP, trie };

class Solution {
  public:
    vector<string> findAllConcatenatedWordsInADict(vector<string> &words) {
        if (APPR == DP)
            return findAllConcatenatedWordsInADict_DP(words);
        return vector<string>{}; // Never Reached
    }
    vector<string> findAllConcatenatedWordsInADict_DP(vector<string> &words) {
        unordered_set<string> word_dict(words.begin(), words.end());
        vector<string> concats;
        for (const auto &word : words)
            if (word_break(word, word_dict))
                concats.emplace_back(word);
        return concats;
    }

    bool word_break(const string &s, const unordered_set<string> &word_dict) {
        const int n = s.length();
        vector<bool> dp(n + 1);
        dp[0] = true;

        for (size_t i = 1; i < n + 1; i++)
            // (n == i) ? 1 : 0 prevents checking self. e.g. s = "leet" and word_dict = [...,"leet",...] returning true
            // !dp[i] acts like a break after dp[i] is set to true
            for (size_t j = (n == i ? 1 : 0); !dp[i] && j < i; j++)
                dp[i] = dp[j] && word_dict.count(s.substr(j, i - j));

        return dp[n];
    }
};
// @lc code=end

int main() {
    vector<string> arr{"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"};
    auto ans = Solution().findAllConcatenatedWordsInADict(arr);
    std::cout << ans << std::endl;
}
