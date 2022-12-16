#ifndef BINARY_TREE_H
#define BINARY_TREE_H
/**
 * Original Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include <sstream>
#include <vector>

using std::string;
using std::vector;
// Enable to print vectors just by calling its name

class TreeNode {
  public:
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(const int &x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(const int &x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}

    // Unfortunately the variadic parameter template needs to be discoverable to the .h file... I have trouble resolving
    // "Undefined Symbols" and "Duplicate Symbols" compilation errors with the main and lc files

    /** @brief Base case for Variadic arguments */
    void insert(){};
    /**
     * @brief Insert method for Binary Search Tree
     * @tparam Args Variadic Type
     * @param value current value to insert
     * @param args remaining list of parameter of values to insert
     */
    template <typename... Args> void insert(const int &value, Args... args) {
        if (value < val) {
            if (!left)
                left = new TreeNode(value);
            else
                left->insert(value);
        } else if (value > val) {
            if (!right)
                right = new TreeNode(value);
            else
                right->insert(value);
        } // skip and do nothing if value == val
        insert(args...);
    }

  private:
    /**
     * @brief Helper methods to visual this TreeNode into a std::vector of strings
     *
     * @return std::tuple<std::vector<string>, int, int, int> - std::vector of lines, width, height, and middle (width /
     * 2)
     */
    std::tuple<std::vector<string>, int, int, int> display_aux();

    /**
     * @brief Overloading << operator to cout a TreeNode string representation
     *
     * @param output output stream
     * @param root the root of the TreeNode
     * @return std::ostream& with TreeNode representation
     */
    friend std::ostream &operator<<(std::ostream &output, TreeNode &root);

    /**
     * @brief Overloading << operator to cout a TreeNode ptr string representation
     *
     * @param output output stream
     * @param root the root of the TreeNode
     * @return std::ostream& with TreeNode representation
     */
    friend std::ostream &operator<<(std::ostream &output, TreeNode *&root);
};

/**
 * @brief Transform leetcode binary tree string into a std::vector of int pts
 *
 * @param s string to parse
 * @param del delimiter to use, default to ','
 * @return std::vector<int *>
 */
std::vector<int *> parse_leetcode_bt(string s, char del = ',');

/**
 * @brief Create a TreeNode from LeetCode list convention format of int or null_ptr
 *
 * @param node_list
 * @return TreeNode *
 */
TreeNode *build_bt(std::vector<int *> node_list);

TreeNode *build_bt(string leetcode_bt);

#endif