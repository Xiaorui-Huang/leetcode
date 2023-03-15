#
# @lc app=leetcode id=958 lang=python3
#
# [958] Check Completeness of a Binary Tree
#
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
#
# algorithms
# Medium (53.87%)
# Likes:    2539
# Dislikes: 34
# Total Accepted:    138.1K
# Total Submissions: 255.1K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a binary tree, determine if it is a complete binary tree.
#
# In a complete binary tree, every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level
# h.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: true
# Explanation: Every level before the last is full (ie. levels with node-values
# {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left
# as possible.
#
#
# Example 2:
#
#
# Input: root = [1,2,3,4,5,null,7]
# Output: false
# Explanation: The node with value 7 isn't as far left as possible.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 100].
# 1 <= Node.val <= 1000
#
#
#

from utils.binary_tree import TreeNode


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        is_complete, _, _ = self._is_complete_tree(root)
        return is_complete

    def _is_complete_tree(self, root: TreeNode | None) -> tuple[bool, bool, int]:
        """Return if the tree is complete, is full and the height of the tree."""

        # trivially complete and full with heigh 0
        if not root:
            return True, True, 0

        if not root.left and root.right:
            return False, False, -1

        left_complete, left_full, left_height = self._is_complete_tree(root.left)
        right_complete, right_full, right_height = self._is_complete_tree(root.right)

        if (left_complete and right_complete) and (
            (left_height == right_height and left_full) or (left_height - 1 == right_height and right_full)
        ):
            return True, left_height == right_height and left_full and right_full, left_height + 1

        return False, False, -1


# @lc code=end
