#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (55.45%)
# Likes:    8738
# Dislikes: 230
# Total Accepted:    914.8K
# Total Submissions: 1.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the zigzag level order traversal of
# its nodes' values. (i.e., from left to right, then right to left for the next
# level and alternate between).
#
#
# Example 1:
#
#
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
#
#
# Example 2:
#
#
# Input: root = [1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
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
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        # let even depth be left to right and odd depth be right to left
        # depth start at 0
        # stack of Node and it's depth level
        if not root:
            return []

        zigzag: list[list[int]] = []
        stack: list[TreeNode] = [root]
        forward = True  # forward as in left to right

        while stack:
            cur_stack: list[TreeNode] = []
            cur_level: list[int] = []
            for cur_node in reversed(stack):
                cur_level.append(cur_node.val)
                left, right = cur_node.left, cur_node.right
                if not forward:
                    left, right = right, left
                if left:
                    cur_stack.append(left)
                if right:
                    cur_stack.append(right)
            zigzag.append(cur_level)
            stack = cur_stack
            forward = not forward

        return zigzag


# @lc code=end
