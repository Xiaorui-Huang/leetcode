#include "lc_269_hard_alien_dictionary.cpp"
#include <iostream>

int main() {
    vector<string> input = {"wrt", "wrf", "er", "ett", "rftt"};
    Solution sol;
    std::cout << sol.alienOrder(input) << std::endl;

    // Test Case 1
    vector<string> input1 = {"wrt", "wrf", "er", "ett", "rftt"};
    cout << "Test Case 1: " << sol.alienOrder(input1) << endl; // Expected Output: "wertf"

    // Test Case 2
    vector<string> input2 = {"z", "x"};
    cout << "Test Case 2: " << sol.alienOrder(input2) << endl; // Expected Output: "zx"

    // Test Case 3
    vector<string> input3 = {"z", "x", "z"};
    cout << "Test Case 3: " << sol.alienOrder(input3) << endl; // Expected Output: ""

    // Additional Test Cases
    // Test Case 4: Single word
    vector<string> input4 = {"abc"};
    cout << "Test Case 4: " << sol.alienOrder(input4) << endl; // Expected Output: "abc"

    // Test Case 5: Multiple words with no valid order
    vector<string> input5 = {"abc", "ab"};
    cout << "Test Case 5: " << sol.alienOrder(input5) << endl; // Expected Output: ""
                                                               //
    vector<string> input6 = {"aac", "aabb"};
    cout << "Test Case 6: " << sol.alienOrder(input6) << endl; // Expected Output: "acb"

    vector<string> input7 = {"abc", "abd", "bda"};
    cout << "Test Case 7: " << sol.alienOrder(input7)
         << endl; // Expected Output: "acbd" (or any valid order like "abcd")

    // Test Case 8: All characters same in words
    vector<string> input8 = {"aaa", "aaa"};
    cout << "Test Case 8: " << sol.alienOrder(input8) << endl; // Expected Output: "a"

    // Test Case 11: One letter per word, valid order
    vector<string> input11 = {"a", "b", "c", "d"};
    cout << "Test Case 11: " << sol.alienOrder(input11) << endl; // Expected Output: "abcd"

    // Test Case 12: Single word with repeated letters
    vector<string> input12 = {"aaaa"};
    cout << "Test Case 12: " << sol.alienOrder(input12) << endl; // Expected Output: "a"

    // Test Case 13: Larger case with mixed valid order
    vector<string> input13 = {"zxy", "zxz", "yzx", "xzy"};
    cout << "Test Case 13: " << sol.alienOrder(input13) << endl; // Expected Output: ""  invalid

    vector<string> input14 = {"z", "z"};
    cout << "Test Case 14: " << sol.alienOrder(input14) << endl; // Expected Output: ""  invalid

    // Test Case 15: Valid order with multiple words
    vector<string> input15 = {"ab", "adc"};
    cout << "Test Case 15: " << sol.alienOrder(input15)
         << endl; // Expected Output: "abcd" (or any valid order like "abdc")
}
