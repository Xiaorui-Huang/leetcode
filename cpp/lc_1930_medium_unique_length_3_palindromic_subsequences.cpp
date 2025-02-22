/*
 * @lc app=leetcode id=1930 lang=cpp
 *
 * [1930] Unique Length-3 Palindromic Subsequences
 *
 * https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
 *
 * algorithms
 * Medium (66.10%)
 * Likes:    1799
 * Dislikes: 80
 * Total Accepted:    120.4K
 * Total Submissions: 180.4K
 * Testcase Example:  '"aabca"'
 *
 * Given a string s, return the number of unique palindromes of length three
 * that are a subsequence of s.
 * 
 * Note that even if there are multiple ways to obtain the same subsequence, it
 * is still only counted once.
 * 
 * A palindrome is a string that reads the same forwards and backwards.
 * 
 * A subsequence of a string is a new string generated from the original string
 * with some characters (can be none) deleted without changing the relative
 * order of the remaining characters.
 * 
 * 
 * For example, "ace" is a subsequence of "abcde".
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "aabca"
 * Output: 3
 * Explanation: The 3 palindromic subsequences of length 3 are:
 * - "aba" (subsequence of "aabca")
 * - "aaa" (subsequence of "aabca")
 * - "aca" (subsequence of "aabca")
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "adc"
 * Output: 0
 * Explanation: There are no palindromic subsequences of length 3 in "adc".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "bbcbaba"
 * Output: 4
 * Explanation: The 4 palindromic subsequences of length 3 are:
 * - "bbb" (subsequence of "bbcbaba")
 * - "bcb" (subsequence of "bbcbaba")
 * - "bab" (subsequence of "bbcbaba")
 * - "aba" (subsequence of "bbcbaba")
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 3 <= s.length <= 10^5
 * s consists of only lowercase English letters.
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
    int countPalindromicSubsequence(string s) {
        int n = s.size();
        vector<int> first(26, n), last(26, -1);
        for (int i = 0; i < n; i++) {
            first[s[i] - 'a'] = min(first[s[i] - 'a'], i);
            last[s[i] - 'a'] = max(last[s[i] - 'a'], i);
        }
        int ans = 0;
        bool seen[26] = {false};

        for (int i = 0; i < 26; i++) {
            if (first[i] < last[i]) {
                // reset seen
                fill(seen, seen + 26, false); 

                for (int j = first[i] + 1; j < last[i]; j++)
                    seen[s[j] - 'a'] = true;

                for (int j = 0; j < 26; j++)
                    if (seen[j])
                        ans++;
            }
        }
        return ans; 
    }
};
// @lc code=end

