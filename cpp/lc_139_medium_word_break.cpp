/*
 * @lc app=leetcode id=139 lang=cpp
 *
 * [139] Word Break
 *
 * https://leetcode.com/problems/word-break/description/
 *
 * algorithms
 * Medium (45.37%)
 * Likes:    12870
 * Dislikes: 545
 * Total Accepted:    1.3M
 * Total Submissions: 2.7M
 * Testcase Example:  '"leetcode"\n["leet","code"]'
 *
 * Given a string s and a dictionary of strings wordDict, return true if s can
 * be segmented into a space-separated sequence of one or more dictionary
 * words.
 *
 * Note that the same word in the dictionary may be reused multiple times in
 * the segmentation.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "leetcode", wordDict = ["leet","code"]
 * Output: true
 * Explanation: Return true because "leetcode" can be segmented as "leet
 * code".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "applepenapple", wordDict = ["apple","pen"]
 * Output: true
 * Explanation: Return true because "applepenapple" can be segmented as "apple
 * pen apple".
 * Note that you are allowed to reuse a dictionary word.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= s.length <= 300
 * 1 <= wordDict.length <= 1000
 * 1 <= wordDict[i].length <= 20
 * s and wordDict[i] consist of only lowercase English letters.
 * All the strings of wordDict are unique.
 *
 *
 */
#include <algorithm>
#include <iostream>
#include <limits>
#include <string_view>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
  public:
    /**
     * @brief Given a string s and a dictionary of strings wordDict, check is s
     * can be segmented by words in wordDict
     *
     * @param s the string to check if break up is possible
     * @param wordDict dictionary of word splits
     * @return return true if s can be segmented into a space-separated sequence
     * of one or more dictionary words.
     */
    bool wordBreak(string s, vector<string> &wordDict) {
        /**
         * DP solution:
         *      let dp[i] be if s[:i] can be separated using wordDict
         *          dp[i] = dp[j] and s[j:] is in wordDict, for 0 <= j < i
         *          dp[0] = True, since empty string can stand in place for any
         * word in wordDict e.g. "" + "leetcode" -> "leetcode"
         */
        int n = s.length();
        vector<bool> dp(n + 1, false);
        dp[0] = true;

        unordered_set<string_view> dict;
        
        // we create read-only view stirng that can substring and check membership without copying
        auto s_view = string_view(s);
        auto str_to_view = [](const string &str) { return string_view(str); };
        // use transform to map string to string_view
        std::transform(wordDict.begin(), wordDict.end(), inserter(dict, dict.end()), str_to_view);

        // i is the length of the substring from 0
        for (size_t i = 0; i < n + 1; i++)
            // j counts up to i, so as to check the partitioning of the substring
            for (size_t j = 0; j < i; j++)
                // if (dp[j] && dict.count(s.substr(j, i - j)))
                if (dp[j] && dict.count(s_view.substr(j, i - j)))
                    dp[i] = true;

        return dp[n];
    }
};
// @lc code=end
