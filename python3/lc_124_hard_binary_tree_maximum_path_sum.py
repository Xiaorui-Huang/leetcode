#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#
# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (38.50%)
# Likes:    12350
# Dislikes: 604
# Total Accepted:    876.4K
# Total Submissions: 2.3M
# Testcase Example:  '[1,2,3]'
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in
# the sequence at most once. Note that the path does not need to pass through
# the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty
# path.
#
#
# Example 1:
#
#
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
#
# Example 2:
#
#
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7
# = 42.
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3 * 10^4].
# -1000 <= Node.val <= 1000
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
# NB: reimplement in C++ and write proof for, in particular either left or right but not both
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = root.val

        def path_gain(node: TreeNode | None) -> int:
            if not node:
                return 0
            nonlocal max_path_sum

            left_gain = max(path_gain(node.left), 0)
            right_gain = max(path_gain(node.right), 0)
            max_path_sum = max(max_path_sum, left_gain + right_gain + node.val)

            return node.val + max(left_gain, right_gain)

        path_gain(root)
        return max_path_sum


# @lc code=end
