#
# @lc app=leetcode id=1339 lang=python3
#
# [1339] Maximum Product of Splitted Binary Tree
#
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/description/
#
# algorithms
# Medium (43.41%)
# Likes:    1531
# Dislikes: 68
# Total Accepted:    65.5K
# Total Submissions: 150.7K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given the root of a binary tree, split the binary tree into two subtrees by
# removing one edge such that the product of the sums of the subtrees is
# maximized.
#
# Return the maximum product of the sums of the two subtrees. Since the answer
# may be too large, return it modulo 10^9 + 7.
#
# Note that you need to maximize the answer before taking the mod and not after
# taking it.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,5,6]
# Output: 110
# Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10.
# Their product is 110 (11*10)
#
#
# Example 2:
#
#
# Input: root = [1,null,2,3,4,null,null,5,6]
# Output: 90
# Explanation: Remove the red edge and get 2 binary trees with sum 15 and
# 6.Their product is 90 (15*6)
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 5 * 10^4].
# 1 <= Node.val <= 10^4
#
#
#

from typing import Optional
from utils.binary_tree import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


MOD = 10**9 + 7


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        partial_sums = []

        def traverse_sums(root: Optional[TreeNode]) -> int:
            """return the sum of this Binary tree rooted at node and add to partial sum"""
            if root is None:
                return 0
            tree_sum = traverse_sums(root.left) + int(root.val) + traverse_sums(root.right)
            partial_sums.append(tree_sum)
            return tree_sum

        total_sum = traverse_sums(root)
        max_prod = 0
        for partial_sum in partial_sums:
            max_prod = max(max_prod, (total_sum - partial_sum) * partial_sum)
        return max_prod % MOD


# @lc code=end
