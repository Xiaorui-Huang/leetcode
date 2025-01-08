#ifndef LC_1408_EASY_STRING_MATCHING_IN_AN_ARRAY_H
#define LC_1408_EASY_STRING_MATCHING_IN_AN_ARRAY_H
/*
 * @lc app=leetcode id=1408 lang=cpp
 *
 * [1408] String Matching in an Array
 *
 * https://leetcode.com/problems/string-matching-in-an-array/description/
 *
 * algorithms
 * Easy (64.09%)
 * Likes:    1380
 * Dislikes: 122
 * Total Accepted:    240K
 * Total Submissions: 343.4K
 * Testcase Example:  '["mass","as","hero","superhero"]'
 *
 * Given an array of string words, return all strings in words that is a
 * substring of another word. You can return the answer in any order.
 * 
 * A substring is a contiguous sequence of characters within a string
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: words = ["mass","as","hero","superhero"]
 * Output: ["as","hero"]
 * Explanation: "as" is substring of "mass" and "hero" is substring of
 * "superhero".
 * ["hero","as"] is also a valid answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: words = ["leetcode","et","code"]
 * Output: ["et","code"]
 * Explanation: "et", "code" are substring of "leetcode".
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: words = ["blue","green","bu"]
 * Output: []
 * Explanation: No string of words is substring of another string.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= words.length <= 100
 * 1 <= words[i].length <= 30
 * words[i] contains only lowercase English letters.
 * All the strings of words are unique.
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

#define LPS 0 // longest prefix suffix
#define TRIE 1

// #define APPR LPS
#define APPR TRIE

#if APPR == TRIE
struct TrieNode {
    TrieNode *children[26] = {NULL};
    int freq = 0;
};

class SuffixTrie {
    TrieNode *root;

  public:
    SuffixTrie() { root = new TrieNode(); }

    void insert(const string &word) {
        int n = word.size();

        // for each start of ch insert them -> insert all suffix
        for (int i = 0; i < n; i++) {
            TrieNode *node = root;
            for (int j = i; j < n; j++) {
                auto idx = word[j] - 'a';
                // if the trie node doesn't exist create it
                if (!node->children[idx])
                    node->children[idx] = new TrieNode();

                node = node->children[idx];
                node->freq++;
            }
        }
    }

    bool search_substring(const string &word) {
        TrieNode *node = root;
        for (auto ch : word) {
            auto idx = ch - 'a';
            if (!node->children[idx])
                return false;
            node = node->children[idx];
        }
        // if the end frequency > 1 -> there is more than one word that shared the path not just the original word
        return node->freq > 1;
    }
};

#endif
class Solution {
  public:
#if APPR == LPS
    vector<int> compute_LPS(const string &word) {
        int n = word.size();
        vector<int> lps(word.size(), 0);
        int len = 0; // current longest prefix suffix len
        // the index we are probing at for pre-suf, we start at the seconds character for comparison
        int cur_idx = 1;

        while (cur_idx < n) {
            // matching the current substring end char with the last char of cur longest prefix suffix
            if (word[len] == word[cur_idx]) {
                len++;
                lps[cur_idx++] = len;
            } else {
                if (len > 0)
                    // we fallback to the next best LPS length for rechecking
                    len = lps[len - 1];
                else // len == 0, just move on
                    cur_idx++;
            }
        }
        return lps;
    }

    bool match(const vector<int> &lps, const string &main, const string &sub) {
        size_t a = 0; // index for main (text)
        size_t b = 0; // index for sub (pattern)

        while (a < main.size()) {
            if (main[a] == sub[b]) {
                a++;
                b++;
            }

            // If we've matched the entire sub (pattern)
            if (b == sub.size())
                // match found at position (a - b) in main
                // in a normal KMP algo -> Reset 'b' per standard KMP to allow for more matches in text
                // do b = lps[b - 1]; and keep matching
                return true;

            // Mismatch after b matches
            else if (a < main.size() && main[a] != sub[b]) {
                // Do we have some prefix matched? If so, jump to the LPS value.
                if (b > 0)
                    b = lps[b - 1];
                else
                    // If no prefix matched yet, just move on
                    a++;
            }
        }
        return false;
    }

    vector<string> stringMatching(vector<string> &words) {
        int n = words.size();
        vector<string> results;

        for (size_t i = 0; i < n; i++) {
            auto lps = compute_LPS(words[i]);
            for (size_t j = 0; j < n; j++) {
                // i is not a substring of a longer string
                if (i == j || words[i].size() > words[j].size())
                    continue;
                // try to match the substring
                if (match(lps, words[j], words[i])) {
                    results.push_back(words[i]);
                    break; // sub aka words[i] is a sub -> break out of checking and move on to the next word
                }
            }
        }
        return results;
    }

#elif APPR == TRIE

    vector<string> stringMatching(vector<string> &words) {
        int n = words.size();
        vector<string> results;

        SuffixTrie trie;
        for (auto word : words)
            trie.insert(word);

        for (auto word : words)
            if (trie.search_substring(word))
                results.push_back(word);

        return results;
    }

#endif
};
// @lc code=end
#endif
