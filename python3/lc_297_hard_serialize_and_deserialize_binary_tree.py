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

from utils.binary_tree import TreeNode

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
from typing import Any, Optional


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        Args:
            root (TreeNode): root of the binary tree to serialize

        Return:
            str: serialized binary tree in a string
        """
        if not root:
            return ""
        # BFS on the binary tree and append the values to a string similar
        serialization = ""

        q: deque[Optional[TreeNode]] = deque([root])
        while len(q):
            node = q.popleft()
            if node is None:
                serialization += "None "
                continue
            else:
                serialization += f"{node.val} "
            q.append(node.left)
            q.append(node.right)

        return serialization.rstrip("None ")

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        Args:
            data (str): serialized binary tree data

        Returns:
            Optional[TreeNode]: _description_
        """
        if not data:
            return None
        # change datatypes from str to int or None
        node_list = [int(val) if val != "None" else None for val in data.split()]
        return self.build_bt(node_list)

    # I just copied from my own library... haha
    def build_bt(self, node_lst: list[Any]) -> Optional[TreeNode]:
        # empty tree
        n = len(node_lst)
        if not n:
            return None
        root = TreeNode(node_lst[0])

        q: deque[TreeNode] = deque([root])

        index = 1
        while index < n:
            cur = q.popleft()

            # index + 1 should exist by the structure of the input (i.e. if the last
            # leaf in empty should give null and not omit it)
            left = node_lst[index]
            right = node_lst[index + 1] if index + 1 < n else None

            # check None, if not null add to tree and put on queue for processing
            if left is not None:
                cur.left = TreeNode(left)
                q.append(cur.left)
            if right is not None:
                cur.right = TreeNode(right)
                q.append(cur.right)

            index += 2  # processed two more nodes

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
