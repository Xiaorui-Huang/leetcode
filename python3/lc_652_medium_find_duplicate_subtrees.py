#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#
# https://leetcode.com/problems/find-duplicate-subtrees/description/
#
# algorithms
# Medium (56.51%)
# Likes:    4064
# Dislikes: 341
# Total Accepted:    183.9K
# Total Submissions: 324.4K
# Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
#
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
#
# Two trees are duplicate if they have the same structure with the same node
# values.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,4,null,2,4,null,null,4]
# Output: [[2,4],[4]]
#
#
# Example 2:
#
#
# Input: root = [2,1,1]
# Output: [[1]]
#
#
# Example 3:
#
#
# Input: root = [2,2,2,3,null,3,null]
# Output: [[2,3],[3]]
#
#
#
# Constraints:
#
#
# The number of the nodes in the tree will be in the range [1, 5000]
# -200 <= Node.val <= 200
#
#
#

from collections import defaultdict
from utils.binary_tree import TreeNode, build_bt, null


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode | None) -> list[TreeNode]:
        duplicates: list[TreeNode] = []
        counts: dict[int, int] = defaultdict(int)
        triplet_id_map: dict[tuple[int, int, int], int] = {}

        def dfs(node: TreeNode | None) -> int:
            """
            return the id of the current node
            """
            if not node:
                return 0

            # nodes are represented by id's of left and right node and the node.val
            triplet = (dfs(node.left), node.val, dfs(node.right))
            # retrieve id if exists, otherwise create a new id for this triplet
            triplet_id = triplet_id_map.setdefault(triplet, len(triplet_id_map) + 1)

            # count the number of structures met
            counts[triplet_id] += 1
            # if we have duplicate append to answers, this only happens once
            if counts[triplet_id] == 2:
                duplicates.append(node)

            return triplet_id

        dfs(root)

        return duplicates


# @lc code=end
