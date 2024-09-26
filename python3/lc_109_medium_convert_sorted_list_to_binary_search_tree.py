#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (57.63%)
# Likes:    6414
# Dislikes: 139
# Total Accepted:    451.2K
# Total Submissions: 759.9K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given the head of a singly linked list where elements are sorted in ascending
# order, convert it to a height-balanced binary search tree.
#
#
# Example 1:
#
#
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the
# shown height balanced BST.
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
#
# Constraints:
#
#
# The number of nodes in head is in the range [0, 2 * 10^4].
# -10^5 <= Node.val <= 10^5
#
#
#

from __future__ import annotations


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
from enum import Enum

appr = Enum("approaches", "arr linked_list")
APPR = appr.linked_list


class Solution:
    def sortedListToBST(self, head: ListNode | None) -> TreeNode | None:
        match APPR:
            case appr.arr:
                return self.sortedListToBST_arr(head)
            case appr.linked_list:
                return self.sortedListToBST_linked_list(head)
        # Never Reached
        return None  # type: ignore

    def sortedListToBST_linked_list(self, head: ListNode | None) -> TreeNode | None:
        def sorted_list_to_BST_head_to_tail(head: ListNode | None, tail: ListNode | None) -> TreeNode | None:
            if head == tail:
                return None

            slow: ListNode | None = head
            fast: ListNode | None = head
            while fast != tail and (fast_next := fast.next) != tail:  # type: ignore
                slow = slow.next  # type:ignore
                fast = fast_next.next  # type: ignore

            # now slow points to mid and fast is at the end of the linked list

            # break the linked list
            root = TreeNode(slow.val)  # type: ignore
            root.left = sorted_list_to_BST_head_to_tail(head, slow)
            root.right = sorted_list_to_BST_head_to_tail(slow.next, tail)  # type:ignore
            return root

        return sorted_list_to_BST_head_to_tail(head, None)

    def sortedListToBST_arr(self, head: ListNode | None) -> TreeNode | None:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next

        def make_tree(arr: list[int]) -> TreeNode | None:
            if not arr:
                return None
            mid = len(arr) // 2
            root = TreeNode(arr[mid])
            root.left = make_tree(arr[:mid])
            root.right = make_tree(arr[mid + 1 :])
            return root

        return make_tree(arr)


# @lc code=end
