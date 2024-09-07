/*
 * @lc app=leetcode id=1367 lang=c
 *
 * [1367] Linked List in Binary Tree
 *
 * https://leetcode.com/problems/linked-list-in-binary-tree/description/
 *
 * algorithms
 * Medium (44.10%)
 * Likes:    2289
 * Dislikes: 68
 * Total Accepted:    85.1K
 * Total Submissions: 190.1K
 * Testcase Example:  '[4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]'
 *
 * Given a binary tree root and a linked list with head as the first node. 
 * 
 * Return True if all the elements in the linked list starting from the head
 * correspond to some downward path connected in the binary tree otherwise
 * return False.
 * 
 * In this context downward path means a path that starts at some node and goes
 * downwards.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: head = [4,2,8], root =
 * [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
 * Output: true
 * Explanation: Nodes in blue form a subpath in the binary Tree.  
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: head = [1,4,2,6], root =
 * [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
 * Output: true
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: head = [1,4,2,6,8], root =
 * [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
 * Output: false
 * Explanation: There is no path in the binary tree that contains all the
 * elements of the linked list from head.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in the tree will be in the range [1, 2500].
 * The number of nodes in the list will be in the range [1, 100].
 * 1 <= Node.val <= 100 for each node in the linked list and binary tree.
 * 
 * 
 */

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};

// Definition for a binary tree node.
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

#include <stdbool.h>
#include <stdlib.h>

// @lc code=start
bool isSubPath_helper(struct ListNode *cur, struct TreeNode *root) {
    if (cur == NULL) // Successfully matched the entire linked list
        return true;
    if (root == NULL) // Reached the end of the tree without fully matching the list
        return false;

    // If the current values match, try to match the next list node with the left or right child
    if (root->val == cur->val)
        if (isSubPath_helper(cur->next, root->left) || isSubPath_helper(cur->next, root->right))
            return true;

    return false; // No matching path found
}

// there is two different recursion happening, one with helper one with the full subpath if the helper fails
bool isSubPath(struct ListNode *head, struct TreeNode *root) {
    if (root == NULL)
        return false;

    // Check if we can start a match from the current root, or try from the left or right subtrees
    return isSubPath_helper(head, root) || isSubPath(head, root->left) ||
           isSubPath(head, root->right);
}
// @lc code=end
