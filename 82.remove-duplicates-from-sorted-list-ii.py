#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (41.55%)
# Likes:    4088
# Dislikes: 140
# Total Accepted:    396.1K
# Total Submissions: 949.9K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given the head of a sorted linked list, delete all nodes that have duplicate
# numbers, leaving only distinct numbers from the original list. Return the
# linked list sorted as well.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,3,4,4,5]
# Output: [1,2,5]
#
#
# Example 2:
#
#
# Input: head = [1,1,1,2,3]
# Output: [2,3]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.
#
#
#
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return str(self.val)
        return f"{self.val} -> {self.next}"


# @lc code=start
# Definition for singly-linked list.
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # a Dummy to keep the head
        sentinel = ListNode(0, head)
        
        # the predecessor: anchor before the great duplicates
        prede = sentinel

        while head:
            # skipping to the last of the duplicates
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                # connecting the predecessor to the next LinkNode
                prede.next = head.next
            else:
                # no dups? move the prede like a normal person
                prede = prede.next

            # yep next
            head = head.next
                
        return sentinel.next

# @lc code=end


def build_linked_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return
    head = ListNode()
    cur = head
    for i, val in enumerate(vals):
        cur.val = val
        # avoid the last link to have a default next LinkNode
        if ~i != -len(vals):
            cur.next = ListNode()
            cur = cur.next

    return head


def main():
    sol = Solution()
    linked_list = build_linked_list(
        [1, 1, 2, 2, 3, 4, 8, 8, 10, 11, 11]
        # [1,2,3,3,4,4,5]
    )
    ans = sol.deleteDuplicates(linked_list)
    print(ans)


if __name__ == "__main__":
    main()
