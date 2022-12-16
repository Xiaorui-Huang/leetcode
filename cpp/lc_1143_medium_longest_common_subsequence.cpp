#ifndef LC_1143_MEDIUM_LONGEST_COMMON_SUBSEQUENCE_H
#define LC_1143_MEDIUM_LONGEST_COMMON_SUBSEQUENCE_H
/*
 * @lc app=leetcode id=1143 lang=cpp
 *
 * [1143] Longest Common Subsequence
 *
 * https://leetcode.com/problems/longest-common-subsequence/description/
 *
 * algorithms
 * Medium (58.81%)
 * Likes:    8560
 * Dislikes: 98
 * Total Accepted:    542.6K
 * Total Submissions: 922.6K
 * Testcase Example:  '"abcde"\n"ace"'
 *
 * Given two strings text1 and text2, return the length of their longest common
 * subsequence. If there is no common subsequence, return 0.
 *
 * A subsequence of a string is a new string generated from the original string
 * with some characters (can be none) deleted without changing the relative
 * order of the remaining characters.
 *
 *
 * For example, "ace" is a subsequence of "abcde".
 *
 *
 * A common subsequence of two strings is a subsequence that is common to both
 * strings.
 *
 *
 * Example 1:
 *
 *
 * Input: text1 = "abcde", text2 = "ace"
 * Output: 3
 * Explanation: The longest common subsequence is "ace" and its length is 3.
 *
 *
 * Example 2:
 *
 *
 * Input: text1 = "abc", text2 = "abc"
 * Output: 3
 * Explanation: The longest common subsequence is "abc" and its length is 3.
 *
 *
 * Example 3:
 *
 *
 * Input: text1 = "abc", text2 = "def"
 * Output: 0
 * Explanation: There is no such common subsequence, so the result is 0.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= text1.length, text2.length <= 1000
 * text1 and text2 consist of only lowercase English characters.
 *
 *
 */

#include <iostream>
#include <vector>
using namespace std;
// @lc code=start
class Solution {
  public:
    /**
     * @brief
     * let LCS(i,j) = LCS for s1[0...i] and s2[0...j]

     * LCS(i,j) =
     *         # base cases
     *         1.  I(s1 == s2)                               , if len(s1) = len(s2) = 0
     *         2.  LCS(i - 1, j - 1) + 1                     , if s[i] == s[j]
     *         3.  max{LCS(i, j - 1), LCS(i - 1, j)}         , if s[i] != s[j]
     * @param text1
     * @param text2
     * @return int
     */
    int longestCommonSubsequence(string text1, string text2) {
        if (text1.length() > text2.length())
            swap(text1, text2);

        auto rows = text1.length();
        auto cols = text2.length();
        int top_left = 0; // LCS(i - 1, j - 1)
        int top = 0;      // LCS(i - 1, j)
        int left = 0;     // LCS(i, j - 1)

        // auto prev_col = vector<int>(rows, 0); // dp for left column values
        auto prev_col = make_unique<int[]>(rows); // dynamic array
        for (size_t col = 0; col < cols; col++) {
            top_left = 0;
            top = 0;
            for (size_t row = 0; row < rows; row++) {
                left = prev_col[row];
                // gathered top, left, top_left -> calculate cur; And this cur is the next top
                top = (text1[row] == text2[col]) ? top_left + 1 : max(top, left);
                prev_col[row] = top;
                top_left = left;
            }
        }
        return top;
    }
};
// @lc code=end

#endif
