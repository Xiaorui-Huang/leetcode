/*
 * @lc app=leetcode id=3 lang=cpp
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (33.76%)
 * Likes:    29597
 * Dislikes: 1257
 * Total Accepted:    3.9M
 * Total Submissions: 11.7M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string s, find the length of the longest substring without repeating
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 *
 * Example 2:
 *
 *
 * Input: s = "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 *
 * Example 3:
 *
 *
 * Input: s = "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * Notice that the answer must be a substring, "pwke" is a subsequence and not
 * a substring.
 *
 *
 *
 * Constraints:
 *
 *
 * 0 <= s.length <= 5 * 10^4
 * s consists of English letters, digits, symbols and spaces.
 *
 *
 */
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

// @lc code=start
class Solution {
  public:
    /**
     * @brief Uses sliding window and keeps track of the last position seen per
     * letter.
     *
     * @param s
     * @return Return the length of the longest non-repeating substring in s
     */
    int lengthOfLongestSubstring(string s) {
        int max_len = 0, left_pt = 0, last_seen;
        std::unordered_map<char, int> last_pos;
        for (int right_pt = 0; right_pt < s.length(); right_pt++) {
            char letter = s[right_pt];
            // in c++20 we can do last_pos.contains(letter)
            // last_seen = (last_pos.find(letter) != last_pos.end()) ? last_pos[letter] : -1;
            last_seen = (last_pos.find(letter) != last_pos.end()) ? last_pos[letter] : -1;

            if (last_seen >= left_pt)
                left_pt = last_seen + 1;

            last_pos[letter] = right_pt;
            max_len = max(max_len, right_pt - left_pt + 1);
        }
        return max_len;
    }
};
// @lc code=end

int main() {
    auto ans = Solution().lengthOfLongestSubstring("abcabcbb");
    std::cout << ans << std::endl;
}