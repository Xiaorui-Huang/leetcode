/*
 * @lc app=leetcode id=2416 lang=cpp
 *
 * [2416] Sum of Prefix Scores of Strings
 *
 * https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
 *
 * algorithms
 * Hard (46.35%)
 * Likes:    815
 * Dislikes: 69
 * Total Accepted:    44.9K
 * Total Submissions: 85.1K
 * Testcase Example:  '["abc","ab","bc","b"]'
 *
 * You are given an array words of size n consisting of non-empty strings.
 * 
 * We define the score of a string word as the number of strings words[i] such
 * that word is a prefix of words[i].
 * 
 * 
 * For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is
 * 2, since "ab" is a prefix of both "ab" and "abc".
 * 
 * 
 * Return an array answer of size n where answer[i] is the sum of scores of
 * every non-empty prefix of words[i].
 * 
 * Note that a string is considered as a prefix of itself.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: words = ["abc","ab","bc","b"]
 * Output: [5,4,3,2]
 * Explanation: The answer for each string is the following:
 * - "abc" has 3 prefixes: "a", "ab", and "abc".
 * - There are 2 strings with the prefix "a", 2 strings with the prefix "ab",
 * and 1 string with the prefix "abc".
 * The total is answer[0] = 2 + 2 + 1 = 5.
 * - "ab" has 2 prefixes: "a" and "ab".
 * - There are 2 strings with the prefix "a", and 2 strings with the prefix
 * "ab".
 * The total is answer[1] = 2 + 2 = 4.
 * - "bc" has 2 prefixes: "b" and "bc".
 * - There are 2 strings with the prefix "b", and 1 string with the prefix
 * "bc".
 * The total is answer[2] = 2 + 1 = 3.
 * - "b" has 1 prefix: "b".
 * - There are 2 strings with the prefix "b".
 * The total is answer[3] = 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: words = ["abcd"]
 * Output: [4]
 * Explanation:
 * "abcd" has 4 prefixes: "a", "ab", "abc", and "abcd".
 * Each prefix has a score of one, so the total is answer[0] = 1 + 1 + 1 + 1 =
 * 4.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= words.length <= 1000
 * 1 <= words[i].length <= 1000
 * words[i] consists of lowercase English letters.
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

struct TrieNode {
    unordered_map<char, TrieNode *> children;
    bool is_end_of_word = false;
    int visitor_counter = 0;
};

class Trie {
  private:
    TrieNode *root;

  public:
    Trie() : root(new TrieNode()) {}

    void insert(const std::string word) {
        auto *cur = root;
        for (char c : word) {
            if (cur->children.find(c) == cur->children.end())
                cur->children[c] = new TrieNode(); // create it if not found

            cur = cur->children[c];
            cur->visitor_counter++;
        }
        cur->is_end_of_word = true;
    }

    bool search(const string &word) {
        auto node = find(word);
        return node != nullptr && node->is_end_of_word;
    }

    bool startWith(const string &prefix) { return find(prefix) != nullptr; }

    int query_visits(const std::string &prefix) {
        int total_visits = 0;
        auto cur = root;
        for (char c : prefix) {
            if (cur->children.find(c) == cur->children.end()) {
                return -1; // shouldn't happen in this question
            }
            cur = cur->children[c];
            total_visits += cur->visitor_counter;
        }

        return total_visits;
    }

  private:
    TrieNode *find(const std::string &prefix) {
        auto cur = root;
        for (char c : prefix) {
            if (cur->children.find(c) == cur->children.end())
                return nullptr;

            cur = cur->children[c];
        }

        return cur;
    }
};

class Solution {
  public:
    vector<int> sumPrefixScores(vector<string> &words) {
        Trie trie;
        for (auto &word : words) {
            trie.insert(word);
        }

        vector<int> scores;
        scores.reserve(words.size());
        for (auto word : words)
            scores.push_back(trie.query_visits(word));

        return scores;
    }
};
// @lc code=end
