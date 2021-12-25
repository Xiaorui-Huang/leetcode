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
        parent = None # init as the parent of head
        cur = head

        while cur and cur.next:
            # duplicate
            # TODO: need to remove cur and the rest of the duplicates
            if cur.val == cur.next.val:
                dup_val = cur.val

                # skip to the end of the duplicates
                while cur.next and cur.next.val == dup_val:
                    cur = cur.next

                # move the pointer to the next (even if its None)
                cur = cur.next
                if parent:
                    parent.next = cur
                else:
                    # reset parent as the head is a dup
                    parent = None
                    head = cur
            else:# not a dup just move on
                parent = cur
                cur = cur.next
        return head


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


# @lc code=end


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
