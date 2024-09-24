/*
 * @lc app=leetcode id=2707 lang=cpp
 *
 * [2707] Extra Characters in a String
 *
 * https://leetcode.com/problems/extra-characters-in-a-string/description/
 *
 * algorithms
 * Medium (52.56%)
 * Likes:    2398
 * Dislikes: 124
 * Total Accepted:    141.7K
 * Total Submissions: 252.9K
 * Testcase Example:  '"leetscode"\n["leet","code","leetcode"]'
 *
 * You are given a 0-indexed string s and a dictionary of words dictionary. You
 * have to break s into one or more non-overlapping substrings such that each
 * substring is present in dictionary. There may be some extra characters in s
 * which are not present in any of the substrings.
 * 
 * Return the minimum number of extra characters left over if you break up s
 * optimally.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
 * Output: 1
 * Explanation: We can break s in two substrings: "leet" from index 0 to 3 and
 * "code" from index 5 to 8. There is only 1 unused character (at index 4), so
 * we return 1.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "sayhelloworld", dictionary = ["hello","world"]
 * Output: 3
 * Explanation: We can break s in two substrings: "hello" from index 3 to 7 and
 * "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used
 * in any substring and thus are considered as extra characters. Hence, we
 * return 3.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 50
 * 1 <= dictionary.length <= 50
 * 1 <= dictionary[i].length <= 50
 * dictionary[i] and s consists of only lowercase English letters
 * dictionary contains distinct words
 * 
 * 
 */

#include <vector>
#include <string>

using namespace std;

// @lc code=start
class Solution {
  public:
    int minExtraChar(string s, vector<string> &dictionary) {
        int n = s.size();
        vector<int> dp(n + 1, n);
        dp[0] = 0; // dp[i] is the minimum number of extra characters left over
                   // if we break up s[0..i-1] optimally
                   
        // O(nkm) where
        // - n is the the number of char
        // - k is the number of words in dictionary
        // - m is the avg number of char in dictionary
        
        // run dp on i
        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + 1; // we start assuming we have to add one more
                                   // character to the previous optimal (no word match)
            // now we check for word matches and find the minimum
            for (string &word : dictionary) {
                int len = word.size();
                // for each word that matches (backwards) at i exactly
                if (i >= len && s.substr(i - len, len) == word)
                    // the word match would be at i-len (backwards)
                    dp[i] = min(dp[i], dp[i - len]);
            }
        }
        return dp[n];
    }
};
// @lc code=end

