#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
#
# algorithms
# Medium (73.94%)
# Likes:    3684
# Dislikes: 88
# Total Accepted:    187.1K
# Total Submissions: 247.2K
# Testcase Example:  '[8,3,10,1,6,null,14,null,null,4,7,13]'
#
# Given the root of a binary tree, find the maximum value v for which there
# exist different nodes a and b where v = |a.val - b.val| and a is an ancestor
# of b.
#
# A node a is an ancestor of b if either: any child of a is equal to b or any
# child of a is an ancestor of b.
#
#
# Example 1:
#
#
# Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
# Output: 7
# Explanation: We have various ancestor-node differences, some of which are
# given below :
# |8 - 3| = 5
# |3 - 7| = 4
# |8 - 1| = 7
# |10 - 13| = 3
# Among all possible differences, the maximum value of 7 is obtained by |8 - 1|
# = 7.
#
# Example 2:
#
#
# Input: root = [1,null,2,null,0,3]
# Output: 3
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [2, 5000].
# 0 <= Node.val <= 10^5
#
#
#

from utils.binary_tree import TreeNode, build_bt

# @lc code=start
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def max_diff(node: Optional[TreeNode], cur_max: int, cur_min: int) -> int:
            if not node:  # leaf node
                return cur_max - cur_min

            # update cur max and min
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)

            # get the max_diff based on local cur_max, cur_min
            left_max_diff = max_diff(node.left, cur_max, cur_min)
            right_max_diff = max_diff(node.right, cur_max, cur_min)
            return max(left_max_diff, right_max_diff)

        return max_diff(root, root.val, root.val)


# @lc code=end
