#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (60.27%)
# Likes:    8636
# Dislikes: 340
# Total Accepted:    1M
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
# Example 2:
#
#
# Input: head = []
# Output: []
#
#
# Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [0, 100].
# 0 <= Node.val <= 100
#
#
#

from typing import Optional
from utils.linked_list import ListNode, linked_list


# @lc code=start
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        sentinel = ListNode()
        if head and head.next:
            res: ListNode | None = head.next
        else:
            res = head
        while head and head.next:
            # gather all three
            first = head
            second = head.next
            third = head.next.next

            # link up from prev
            sentinel.next = second
            # swap
            first.next = third
            second.next = first

            # remember the sentinel to connect the next swap
            sentinel = first
            # point to the next
            head = third

        return res


# @lc code=end
def main() -> None:
    sol = Solution()
    lst = [1, 2, 3, 4, 5]
    ans = sol.swapPairs(linked_list(lst))
    print(ans)


if __name__ == "__main__":
    main()
