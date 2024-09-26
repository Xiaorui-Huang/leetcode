/*
 * @lc app=leetcode id=1684 lang=c
 *
 * [1684] Count the Number of Consistent Strings
 *
 * https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
 *
 * algorithms
 * Easy (83.64%)
 * Likes:    1749
 * Dislikes: 75
 * Total Accepted:    199.6K
 * Total Submissions: 237.5K
 * Testcase Example:  '"ab"\n["ad","bd","aaab","baa","badab"]'
 *
 * You are given a string allowed consisting of distinct characters and an
 * array of strings words. A string is consistent if all characters in the
 * string appear in the string allowed.
 * 
 * Return the number of consistent strings in the array words.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
 * Output: 2
 * Explanation: Strings "aaab" and "baa" are consistent since they only contain
 * characters 'a' and 'b'.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
 * Output: 7
 * Explanation: All strings are consistent.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
 * Output: 4
 * Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= words.length <= 10^4
 * 1 <= allowed.length <=^ 26
 * 1 <= words[i].length <= 10
 * The characters in allowed are distinct.
 * words[i] and allowed contain only lowercase English letters.
 * 
 * 
 */

// @lc code=start

#include <stdbool.h>

int countConsistentStrings(char *allowed, char **words, int wordsSize) {
    char cur;
    bool dict[26] = {0};
    while ((cur = *(allowed++)) != '\0') {
        dict[cur - 'a'] = true;
    }

    int count = 0;
    for (int i = 0; i < wordsSize; i++) {
        char *word = words[i];
        count++;
        while ((cur = *(word++)) != '\0') {
            if (dict[cur - 'a'] == false) {
                count--;
                break;
            }
        }
    }
    return count;
}
// @lc code=end
