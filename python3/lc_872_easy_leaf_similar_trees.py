#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (67.51%)
# Likes:    2824
# Dislikes: 65
# Total Accepted:    242.4K
# Total Submissions: 358.8K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n' + '[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree, from left to right order, the
# values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
#
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
#
#
# Example 1:
#
#
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 =
# [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
#
# Example 2:
#
#
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].
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
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def find_leaf(node: TreeNode | None, leaf_list: list[int]) -> None:
            """inorder traversal and collect the leaf nodes"""
            if not node:
                return
            if not node.left and not node.right:  # is leaf
                leaf_list.append(node.val)
            if node.left:  # first left
                find_leaf(node.left, leaf_list)
            if node.right:  # then right
                find_leaf(node.right, leaf_list)

        leaf_list1: list[int] = []
        leaf_list2: list[int] = []
        find_leaf(root1, leaf_list1)
        find_leaf(root2, leaf_list2)
        return leaf_list1 == leaf_list2


# @lc code=end
