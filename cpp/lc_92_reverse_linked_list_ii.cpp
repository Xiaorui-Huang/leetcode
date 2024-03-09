#ifndef LC_92_REVERSE_LINKED_LIST_II_H
#define LC_92_REVERSE_LINKED_LIST_II_H
/*
 * @lc app=leetcode id=92 lang=cpp
 *
 *
 * https://leetcode.com/problems/reverse-linked-list-ii/description/
 *
92. Reverse Linked List II
Medium

Given the head of a singly linked list and two integers left and right where
left <= right, reverse the nodes of the list from position left to position
right, and return the reversed list.


Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]


Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


Follow up: Could you do it in one pass?
 */

#include <algorithm>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S>
ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

#include "linked_list.h"

class Solution {
  public:
    ListNode *reverseBetween(ListNode *head, int left, int right) {
        auto cur = head;
        ListNode *portion_head = NULL, *portion_tail = NULL, *portion_prev;

        // generic dummy head reference for abstract start of linked list
        ListNode dummy = ListNode(0, head);
        ListNode *sentinel = &dummy;

        int i = 1;

        while (cur) {
            // save the reference to the next node first
            auto next = cur->next;

            // record the sentinel that is the parent of portion_head
            if (i == left - 1)
                sentinel = cur;
            else if (i == left) {
                // init portion head and portion_prev
                portion_head = cur;
                portion_prev = portion_head;
            } else if (left < i && i <= right) {
                // reverse the portion until the end
                cur->next = portion_prev;
                portion_prev = cur;
                if (i == right) // mark the portion end
                    portion_tail = cur;
            } else if (i == right + 1) { 
                // early exit at the end of portion
                break;
            }

            cur = next;
            i++;
        }
        // finalize and link up the three segments
        if (portion_head && portion_tail) {
            // the node before the reverse portion
            sentinel->next = portion_tail;
            // connect the portion after 
            portion_head->next = cur;
            // if the sentinel is void then it's the head
            if (sentinel == &dummy)
                head = sentinel->next;
        }
        return head;
    }
};

// @lc code=end
#endif
