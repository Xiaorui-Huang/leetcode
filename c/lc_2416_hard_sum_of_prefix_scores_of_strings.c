/*
 * @lc app=leetcode id=2416 lang=c
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
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>
#include <assert.h>

// @lc code=start
// forward declaration of struct TrieNode
typedef struct TrieNode TrieNode;

struct TrieNode{
    TrieNode* children[26];
    bool is_end_of_word;
    int visitor_count;
};


void insert(TrieNode *trie, char * s){
    char c;
    TrieNode *cur = trie;

    while((c = *s++) != '\0'){
        if(cur->children[c - 'a'] == NULL){
            TrieNode * new_node = (TrieNode *) calloc(1, sizeof(TrieNode));

            // TrieNode * new_node = (TrieNode *) malloc(sizeof(TrieNode));
            // memset(new_node->children, 0, sizeof(TrieNode* ) * 26);
            // new_node->is_end_of_word = false;
            // new_node->visitor_count = 0;

            cur->children[c - 'a'] = new_node;
        }
        cur = cur->children[c - 'a'];
        cur->visitor_count++;
    }
    cur->is_end_of_word = true;
}

int find_score(TrieNode *trie, char * s){
    int score = 0;
    char c;
    TrieNode *cur = trie;

    while((c = *s++) != '\0'){
        assert(cur->children[c - 'a'] != NULL);
        cur = cur->children[c - 'a'];
        score += cur->visitor_count;
    }
    
    return score;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sumPrefixScores(char** words, int wordsSize, int* returnSize) {
    *returnSize = wordsSize;
    int * scores = (int *) malloc(sizeof(int) * wordsSize);
    TrieNode * root = (TrieNode *) calloc(1, sizeof(TrieNode));
    for (size_t i = 0; i < wordsSize; i++)
        insert(root, words[i]);

    for (size_t i = 0; i < wordsSize; i++)
        scores[i] = find_score(root, words[i]);
    
    return scores;
}
// @lc code=end

