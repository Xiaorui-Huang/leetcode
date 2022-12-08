#
# @lc app=leetcode id=1474 lang=python3
#
# [1474] Delete N Nodes After M Nodes of a Linked List
#
# https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/description/
#
# algorithms
# Easy (73.81%)
# Likes:    332
# Dislikes: 9
# Total Accepted:    23.6K
# Total Submissions: 32.1K
# Testcase Example:  '[1,2,3,4,5,6,7,8,9,10,11,12,13]\n2\n3'
#
# You are given the head of a linked list and two integers m and n.
#
# Traverse the linked list and remove some nodes in the following way:
#
#
# Start with the head as the current node.
# Keep the first m nodes starting with the current node.
# Remove the next n nodes
# Keep repeating steps 2 and 3 until you reach the end of the list.
#
#
# Return the head of the modified list after removing the mentioned nodes.
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10,11,12,13], m = 2, n = 3
# Output: [1,2,6,7,11,12]
# Explanation: Keep the first (m = 2) nodes starting from the head of the
# linked List  (1 ->2) show in black nodes.
# Delete the next (n = 3) nodes (3 -> 4 -> 5) show in read nodes.
# Continue with the same procedure until reaching the tail of the Linked List.
# Head of the linked list after removing nodes is returned.
#
#
# Example 2:
#
#
# Input: head = [1,2,3,4,5,6,7,8,9,10,11], m = 1, n = 3
# Output: [1,5,9]
# Explanation: Head of linked list after removing nodes is returned.
#
#
#
# Constraints:
#
#
# The number of nodes in the list is in the range [1, 10^4].
# 1 <= Node.val <= 10^6
# 1 <= m, n <= 1000
#
#
#
# Follow up: Could you solve this problem by modifying the list in-place?
#
#

from utils.linked_list import ListNode, linked_list  # type: ignore

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        sentinel = ListNode(0, head)
        prev = sentinel
        while head:
            # keep
            for _ in range(m):
                if head:
                    # shift the prev
                    prev = prev.next
                    head = head.next
                else:
                    break

            # remove
            for _ in range(n):
                if head:
                    # prev stays stationary
                    prev.next = head.next
                    head = head.next
                else:
                    break

        return sentinel.next


# @lc code=end
def main():
    sol = Solution()
    link = linked_list(list(range(1, 14 + 1)))
    ans = sol.deleteNodes(link, 1, 12)
    print(ans)


if __name__ == "__main__":
    main()
