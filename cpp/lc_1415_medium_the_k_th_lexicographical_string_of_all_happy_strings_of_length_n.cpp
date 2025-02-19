/*
 * @lc app=leetcode id=1415 lang=cpp
 *
 * [1415] The k-th Lexicographical String of All Happy Strings of Length n
 *
 * https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/
 *
 * algorithms
 * Medium (74.99%)
 * Likes:    1393
 * Dislikes: 39
 * Total Accepted:    138.8K
 * Total Submissions: 163.6K
 * Testcase Example:  '1\n3'
 *
 * A happy string is a string that:
 * 
 * 
 * consists only of letters of the set ['a', 'b', 'c'].
 * s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is
 * 1-indexed).
 * 
 * 
 * For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings
 * and strings "aa", "baa" and "ababbc" are not happy strings.
 * 
 * Given two integers n and k, consider a list of all happy strings of length n
 * sorted in lexicographical order.
 * 
 * Return the kth string of this list or return an empty string if there are
 * less than k happy strings of length n.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 1, k = 3
 * Output: "c"
 * Explanation: The list ["a", "b", "c"] contains all happy strings of length
 * 1. The third string is "c".
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 1, k = 4
 * Output: ""
 * Explanation: There are only 3 happy strings of length 1.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 3, k = 9
 * Output: "cab"
 * Explanation: There are 12 different happy string of length 3 ["aba", "abc",
 * "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You
 * will find the 9^th string = "cab"
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10
 * 1 <= k <= 100
 * 
 * 
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;
// @lc code=start
class Solution {
  public:
    int choose(int choice, int prev) {
        if (prev == 0)
            return choice + 1;
        if (prev == 1)
            return choice ? 2 : 0;

        return choice;
    }
    string getHappyString(int n, int k) {
        if(k > 3 * (1 << (n - 1)))
            return "";

        k--; // make into index 
        string kth(n, ' ');

        int prev = -1;

        for (int i = 0; i < n; i++) {
            int divisor = 1 << (n - i - 1);
            prev = choose(k / divisor, prev);
            kth[i] = prev + 'a';
            k %= divisor;
        }

        return kth;
    }
};
// @lc code=end
