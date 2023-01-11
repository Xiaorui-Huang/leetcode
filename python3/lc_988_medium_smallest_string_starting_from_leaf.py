#
# @lc app=leetcode id=988 lang=python3
#
# [988] Smallest String Starting From Leaf
#
# https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
#
# algorithms
# Medium (49.82%)
# Likes:    1371
# Dislikes: 193
# Total Accepted:    63.1K
# Total Submissions: 126.5K
# Testcase Example:  '[0,1,2,3,4,3,4]'
#
# You are given the root of a binary tree where each node has a value in the
# range [0, 25] representing the letters 'a' to 'z'.
#
# Return the lexicographically smallest string that starts at a leaf of this
# tree and ends at the root.
#
# As a reminder, any shorter prefix of a string is lexicographically
# smaller.
#
#
# For example, "ab" is lexicographically smaller than "aba".
#
#
# A leaf of a node is a node that has no children.
#
#
# Example 1:
#
#
# Input: root = [0,1,2,3,4,3,4]
# Output: "dba"
#
#
# Example 2:
#
#
# Input: root = [25,1,3,1,3,0,2]
# Output: "adz"
#
#
# Example 3:
#
#
# Input: root = [2,2,1,null,1,0,null,0]
# Output: "abc"
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 8500].
# 0 <= Node.val <= 25
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
from enum import Enum

appr = Enum("approaches", "stack leetcode")
APPR = appr.stack

ASCII_a = ord("a")


class Solution:
    def smallestFromLeaf(self, root: TreeNode | None) -> str:
        match APPR:
            case appr.leetcode:
                return self.smallestFromLeaf_leetcode(root)
            case appr.stack:
                return self.smallestFromLeaf_stack(root)
            case _:
                return ""  # type: ignore

    def smallestFromLeaf_leetcode(self, root: TreeNode | None) -> str:
        if not root:
            return ""

        # genius
        res = "z" * 13  # init max result, tree depth,  12< log2(8000) < 13

        def dfs(node: TreeNode, s: str = "") -> None:
            nonlocal res
            cur_s = chr(ASCII_a + node.val) + s
            if not node.left and not node.right:
                # jesus this is built in...
                res = min(res, cur_s)
                return

            if node.left:
                dfs(node.left, cur_s)

            if node.right:
                dfs(node.right, cur_s)

        dfs(root)
        return res

    def smallestFromLeaf_stack(self, root: TreeNode | None) -> str:
        if root is None:
            return ""  # should never happen

        # could just use a deque and appendleft so I don't need all this reversed calls
        cur_letter_stack: list[int] = []

        def dfs(node: TreeNode, letter_stack: list[int]) -> None:
            nonlocal cur_letter_stack
            letter_stack.append(node.val)

            if node.left:
                dfs(node.left, letter_stack.copy())

            if node.right:
                dfs(node.right, letter_stack.copy())

            if node.left is None and node.right is None:
                if not cur_letter_stack:  # the first leaf visited
                    cur_letter_stack = letter_stack
                    return
                for (a, b) in zip(reversed(cur_letter_stack), reversed(letter_stack)):
                    if a < b:
                        return  # cur_letter is lexi smaller, so do nothing
                    if a > b:
                        cur_letter_stack = letter_stack
                        return
                if len(letter_stack) < len(cur_letter_stack):
                    cur_letter_stack = letter_stack

        dfs(root, [])

        return "".join(map(lambda i: chr(i + ASCII_a), reversed(cur_letter_stack)))


# @lc code=end
