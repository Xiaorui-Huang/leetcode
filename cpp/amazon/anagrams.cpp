/*
Problem Statement:

You are given n pairs of DNA sequences. For each pair of DNA sequences,
determine if the two DNA strings are "special" anagrams. Two strings are
considered "special" if they can become anagrams after removing any number of
occurrences of at most one character from each string.

Input:

- The first line contains an integer n (1 ≤ n ≤ 100), the number of pairs of DNA sequences.
- The next n lines each contain two strings, dna1 and dna2, consisting of
lowercase English letters only. Each string has a length of at most 100.

Output:

- For each pair of DNA sequences, output 1 if the pair is special and 0 if it is not.

Example:

Input:
2
abcee acdeedb
sljffsaje sljsje

Output:
1
0

Explanation:

For the first pair (abcee, acdeedb):
- Remove the character 'd' from acdeedb to make the two strings anagrams (abcee and acdeeb become anagrams after the removal of one character). Hence, the result is 1.

For the second pair (sljffsaje, sljsje):
- The characters 'f' and 'a' in sljffsaje cannot be matched by removing just one character from each string. So, the result is 0.
*/

#define TEST

#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Helper function to determine if two DNA sequences are special anagrams
bool is_special(const string &s1, const string &s2) {
    // Frequency arrays for each DNA string
    int freq1[26] = {0}, freq2[26] = {0};

    // Counting character frequencies for s1
    for (char c : s1)
        freq1[c - 'a']++;

    // Counting character frequencies for s2
    for (char c : s2)
        freq2[c - 'a']++;

    // Vectors to store characters with positive and negative differences
    int pos_diff = 0;
    int neg_diff = 0;

    // Compute differences and collect characters with positive and negative differences
    for (int i = 0; i < 26; ++i)
        if (freq1[i] != freq2[i])
            if (freq1[i] > freq2[i])
                pos_diff++;
            else
                neg_diff++;

    if (pos_diff > 1 || neg_diff > 1)
        // Cannot make them anagrams under given constraints
        return false;

    // now (pos_diff >= 1 and neg_diff >= 1)
    return true;
}

// Struct to define a test case
struct TestCase {
    std::string input1;
    std::string input2;
    bool expected;
    std::string description;
};

// Function to run the test cases
void run_tests(const std::vector<TestCase> &testCases) {
    int passed = 0;

    for (size_t i = 0; i < testCases.size(); ++i) {
        const TestCase &test = testCases[i];
        bool result = is_special(test.input1, test.input2);
        if (result == test.expected) {
            std::cout << "Test " << i + 1 << " PASSED (" << test.description << ").\n";
            ++passed;
        } else {
            std::cout << "Test " << i + 1 << " FAILED (" << test.description << ").\n";
            std::cout << "Expected: " << test.expected << ", Got: " << result << "\n";
        }
    }

    std::cout << "\n" << passed << " out of " << testCases.size() << " tests passed.\n";
}

int main() {
#ifndef TEST
    int n;
    cin >> n;
    while (n--) {
        string dna1, dna2;
        cin >> dna1 >> dna2;

        if (is_special(dna1, dna2)) {
            cout << "1" << endl;
        } else {
            cout << "0" << endl;
        }
    }
    return 0;
#endif
    std::vector<TestCase> testCases = {
        {"listen", "silent", true, "Anagram test with valid inputs"},
        {"triangle", "integral", true, "Another valid anagram test"},
        {"apple", "pale", true, "Non-anagram test with different lengths"},
        {"abc", "def", false, "Non-anagram test with same length, different chars"},
        {"", "", true, "Empty strings test"},
        {"", "aaaaa", true, "One empty string"},
        {"", "aaaba", false, "One empty string, with two chars"},
        {"aaaba", "", false, "One empty string, with two chars, fliped"},
        {"a", "a", true, "Single character anagram test"},
        {"abc", "cba", true, "Reversed strings test"},
        {"annaconda", "bannabonda", true, "Similar, but remove from both"},
        {"annaconda", "bannaccbonda", false, "Similar, but needs both b and c remove from s2"},
        {"jjljlljljla", "jjjjjjjjjajjjjjjj", true, "need to remove l from s1, but also j from s2"},
        {"jjljlaljljla", "jjjjjjjjjajjjjjjj", false, "need to remove a, l from s1, bad"},
    };

    // Run all the tests
    run_tests(testCases);
}