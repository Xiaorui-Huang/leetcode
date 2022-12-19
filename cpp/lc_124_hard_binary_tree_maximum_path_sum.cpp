#ifndef LC_124_HARD_BINARY_TREE_MAXIMUM_PATH_SUM_H
#define LC_124_HARD_BINARY_TREE_MAXIMUM_PATH_SUM_H
/*
 * @lc app=leetcode id=124 lang=cpp
 *
 * [124] Binary Tree Maximum Path Sum
 *
 * https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
 *
 * algorithms
 * Hard (38.50%)
 * Likes:    12350
 * Dislikes: 604
 * Total Accepted:    876.4K
 * Total Submissions: 2.3M
 * Testcase Example:  '[1,2,3]'
 *
 * A path in a binary tree is a sequence of nodes where each pair of adjacent
 * nodes in the sequence has an edge connecting them. A node can only appear in
 * the sequence at most once. Note that the path does not need to pass through
 * the root.
 *
 * The path sum of a path is the sum of the node's values in the path.
 *
 * Given the root of a binary tree, return the maximum path sum of any
 * non-empty path.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3]
 * Output: 6
 * Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
 * 6.
 *
 *
 * Example 2:
 *
 *
 * Input: root = [-10,9,20,null,null,15,7]
 * Output: 42
 * Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 +
 * 7 = 42.
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 3 * 10^4].
 * -1000 <= Node.val <= 1000
 *
 *
 */
#include "binary_tree.h"
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
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
    int maxPathSum(TreeNode *root) {
        if (!root)
            return 0; // Never Reached
        int max_path_sum = root->val;

        // Example of recursive lambda function in c++
        std::function<int(TreeNode *)> path_gain = [&max_path_sum, &path_gain](TreeNode *node) -> int {
            if (!node)
                return 0;
            auto left_gain = std::max(path_gain(node->left), 0);
            auto right_gain = std::max(path_gain(node->right), 0);
            max_path_sum = std::max(max_path_sum, left_gain + node->val + right_gain);
            return node->val + std::max(left_gain, right_gain);
        };
        path_gain(root);
        return max_path_sum;
    }
};
// @lc code=end
#endif