/*
 * @lc app=leetcode id=109 lang=rust
 *
 * [109] Convert Sorted List to Binary Search Tree
 *
 * https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
 *
 * algorithms
 * Medium (57.63%)
 * Likes:    6414
 * Dislikes: 139
 * Total Accepted:    451.2K
 * Total Submissions: 759.9K
 * Testcase Example:  '[-10,-3,0,5,9]'
 *
 * Given the head of a singly linked list where elements are sorted in
 * ascending order, convert it to a height-balanced binary search tree.
 *
 *
 * Example 1:
 *
 *
 * Input: head = [-10,-3,0,5,9]
 * Output: [0,-3,9,-10,null,5]
 * Explanation: One possible answer is [0,-3,9,-10,null,5], which represents
 * the shown height balanced BST.
 *
 *
 * Example 2:
 *
 *
 * Input: head = []
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in head is in the range [0, 2 * 10^4].
 * -10^5 <= Node.val <= 10^5
 *
 *
 */

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}
// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}
struct Solution;
// @lc code=start
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn sorted_list_to_bst(head: Option<Box<ListNode>>) -> Option<Rc<RefCell<TreeNode>>> {
        if head.is_none() {
            return None;
        }
        return sorted_list_to_bst_head_to_tail(head.as_ref(), None);

        fn sorted_list_to_bst_head_to_tail(
            head: Option<&Box<ListNode>>,
            tail: Option<&Box<ListNode>>,
        ) -> Option<Rc<RefCell<TreeNode>>> {
            if head == tail {
                return None;
            }

            let mut slow = head;
            let mut fast = head;

            while fast != tail {
                let fast_next = fast.and_then(|fast| fast.next.as_ref());
                if fast_next == tail {
                    break;
                }
                slow = slow.and_then(|slow| slow.next.as_ref());
                fast = fast_next.and_then(|fast_next| fast_next.next.as_ref());
            }
            let mut root = TreeNode::new(slow.unwrap().val);
            root.left = sorted_list_to_bst_head_to_tail(head, slow);
            root.right =
                sorted_list_to_bst_head_to_tail(slow.and_then(|slow| slow.next.as_ref()), tail);

            return Some(Rc::new(RefCell::new(root)));
        }
    }
}
// @lc code=end

fn main() {}
