/*
 * @lc app=leetcode id=143 lang=cpp
 *
 * [143] Reorder List
 *
 * https://leetcode.com/problems/reorder-list/description/
 *
 * algorithms
 * Medium (56.23%)
 * Likes:    10501
 * Dislikes: 372
 * Total Accepted:    881.1K
 * Total Submissions: 1.5M
 * Testcase Example:  '[1,2,3,4]'
 *
 * You are given the head of a singly linked-list. The list can be represented
 * as:
 *
 *
 * L0 → L1 → … → Ln - 1 → Ln
 *
 *
 * Reorder the list to be on the following form:
 *
 *
 * L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
 *
 *
 * You may not modify the values in the list's nodes. Only nodes themselves may
 * be changed.
 *
 *
 * Example 1:
 *
 *
 * Input: head = [1,2,3,4]
 * Output: [1,4,2,3]
 *
 *
 * Example 2:
 *
 *
 * Input: head = [1,2,3,4,5]
 * Output: [1,5,2,4,3]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the list is in the range [1, 5 * 10^4].
 * 1 <= Node.val <= 1000
 *
 *
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

#include "linked_list.h"
// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

// Optimal way is to use two speed pointers
class Solution {
  public:
    void reorderList(ListNode *head) {
        // base case: only has 1 or 2 elements
        if (!head->next || !head->next->next)
            return;
        vector<ListNode *> nodes;
        while (head) {
            nodes.push_back(head);
            head = head->next;
        }
        int i = 0, n = nodes.size() - 1;

        ListNode *sentinel = new ListNode();
        auto cur = sentinel;

        while (i <= n - i) {
            cur->next = nodes[i];
            nodes[i]->next = nodes[n - i];
            cur = nodes[n - i];
            i++;
        }
        cur->next = NULL;
    }
};
// @lc code=end
