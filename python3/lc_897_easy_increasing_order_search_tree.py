#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (76.56%)
# Likes:    2973
# Dislikes: 621
# Total Accepted:    197.4K
# Total Submissions: 253.6K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# Given the root of a binary search tree, rearrange the tree in in-order so
# that the leftmost node in the tree is now the root of the tree, and every
# node has no left child and only one right child.
#
#
# Example 1:
#
#
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
# Example 2:
#
#
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
#
#
#
# Constraints:
#
#
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000
#
#

from utils.bst import TreeNode, build_bst, null  # type: ignore

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # dummy root for the increasing TreeNode
        dummy = TreeNode()

        def in_order_insertion(bst: TreeNode, cur: TreeNode) -> TreeNode:
            """In order traversal of BST to visit nodes in sorted order

            Args:
                bst (TreeNode): the current position in the original bst
                cur (TreeNode): the current postion in the increasing bst

            Returns:
                TreeNode: the most recently inserted node to the increasing bst
            """
            if bst.left is None and bst.right is None:
                cur.right = TreeNode(bst.val)
                return cur.right

            # handes left child
            if bst.left:
                cur = in_order_insertion(bst.left, cur)

            # handles root
            cur.right = TreeNode(bst.val)
            cur = cur.right

            # handles right child
            if bst.right:
                cur = in_order_insertion(bst.right, cur)
            return cur

        in_order_insertion(root, dummy)
        return dummy.right


# @lc code=end


def main():
    sol = Solution()

    lst = [5, 3, 6, 2, 4, null, 8, 1, null, null, null, 7, 9]
    bst = build_bst(lst)

    ans = sol.increasingBST(bst)
    print(ans)


if __name__ == "__main__":
    main()
