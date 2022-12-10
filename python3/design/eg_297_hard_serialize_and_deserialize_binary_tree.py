#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (55.08%)
# Likes:    8148
# Dislikes: 301
# Total Accepted:    703.5K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Clarification: The input/output format is the same as how LeetCode serializes
# a binary tree. You do not necessarily need to follow this format, so please
# be creative and come up with different approaches yourself.
#
#
# Example 1:
#
#
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
#
#
# Example 2:
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
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
#
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import Optional
from utils.binary_tree import TreeNode


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def recur_serialize(node: Optional[TreeNode]) -> None:
            if node:
                vals.append(str(node.val))
                recur_serialize(node.left)
                recur_serialize(node.right)
            else:
                vals.append("#")

        vals: list[str] = []
        recur_serialize(root)
        return " ".join(vals)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split())

        def recur_deserialize() -> Optional[TreeNode]:
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = recur_deserialize()
            node.right = recur_deserialize()
            return node

        return recur_deserialize()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
