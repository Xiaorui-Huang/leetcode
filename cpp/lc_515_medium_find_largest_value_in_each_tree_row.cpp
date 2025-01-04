/*
 * @lc app=leetcode id=515 lang=cpp
 *
 * [515] Find Largest Value in Each Tree Row
 *
 * https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
 *
 * algorithms
 * Medium (65.70%)
 * Likes:    4002
 * Dislikes: 127
 * Total Accepted:    457.4K
 * Total Submissions: 688.6K
 * Testcase Example:  '[1,3,2,5,3,null,9]'
 *
 * Given the root of a binary tree, return an array of the largest value in
 * each row of the tree (0-indexed).
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: root = [1,3,2,5,3,null,9]
 * Output: [1,3,9]
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: root = [1,2,3]
 * Output: [1,3]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree will be in the range [0, 10^4].
 * -2^31 <= Node.val <= 2^31 - 1
 * 
 * 
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> largestValues(TreeNode* root) {
        if(!root)
            return {};

        vector<TreeNode *> q;
        
        q.push_back(root);
        vector<int> results;
        
        while(!q.empty()){
            vector<TreeNode *> working_q;
            int max_level = INT_MIN;
            for(auto node: q){
                max_level = max(max_level, node->val);
                if(node->right)
                    working_q.push_back(node->right);
                if(node->left)
                    working_q.push_back(node->left);
            }
            results.push_back(max_level);
            q = working_q;
        }

        return results; 
    }
};
// @lc code=end

