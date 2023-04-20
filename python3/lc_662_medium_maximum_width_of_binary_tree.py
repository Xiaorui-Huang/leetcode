#
# @lc app=leetcode id=662 lang=python3
#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (40.73%)
# Likes:    6500
# Dislikes: 891
# Total Accepted:    247.2K
# Total Submissions: 605.9K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return the maximum width of the given tree.
#
# The maximum width of a tree is the maximum width among all levels.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and rightmost non-null nodes), where the null nodes between the
# end-nodes that would be present in a complete binary tree extending down to
# that level are also counted into the length calculation.
#
# It is guaranteed that the answer will in the range of a 32-bit signed
# integer.
#
#
# Example 1:
#
#
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4
# (5,3,null,9).
#
#
# Example 2:
#
#
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7
# (6,null,null,null,null,null,7).
#
#
# Example 3:
#
#
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2
# (3,2).
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 3000].
# -100 <= Node.val <= 100
#
#
#

from utils.binary_tree import TreeNode, build_bt, null


# @lc code=start
from collections import deque


from enum import Enum

appr = Enum("approaches", "dfs bfs")
APPR = appr.dfs


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        match APPR:
            case appr.bfs:
                return self.widthOfBinaryTree_bfs(root)
            case appr.dfs:
                return self.widthOfBinaryTree_dfs(root)
        # Never Reached
        return 0  # type: ignore

    def widthOfBinaryTree_dfs(self, root: TreeNode) -> int:
        left_mosts = {}  # key: depth, value: node id
        self.max_width = 0

        def dfs(node: TreeNode | None, depth: int, index: int) -> None:
            if not node:
                return

            if depth not in left_mosts:
                left_mosts[depth] = index

            dfs(node.left, depth + 1, 2 * index)
            dfs(node.right, depth + 1, 2 * index + 1)

            self.max_width = max(self.max_width, index - left_mosts[depth] + 1)

        dfs(root, 0, 1)
        return self.max_width

    def widthOfBinaryTree_bfs(self, root: TreeNode) -> int:
        q: deque[tuple[TreeNode, int]] = deque([(root, 1)])

        max_width = 1

        while q:
            level_len = len(q)
            _, level_start = q[0]
            index = 0
            for i in range(level_len):
                node, index = q.popleft()
                if node.left:
                    q.append((node.left, 2 * index))
                if node.right:
                    q.append((node.right, 2 * index + 1))
            max_width = max(max_width, index - level_start + 1)

        return max_width


# @lc code=end
