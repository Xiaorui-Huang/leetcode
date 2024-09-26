/*
 * @lc app=leetcode id=101 lang=rust
 *
 * [101] Symmetric Tree
 *
 * https://leetcode.com/problems/symmetric-tree/description/
 *
 * algorithms
 * Easy (53.25%)
 * Likes:    12388
 * Dislikes: 280
 * Total Accepted:    1.5M
 * Total Submissions: 2.9M
 * Testcase Example:  '[1,2,2,3,4,4,3]'
 *
 * Given the root of a binary tree, check whether it is a mirror of itself
 * (i.e., symmetric around its center).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,2,3,4,4,3]
 * Output: true
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,2,2,null,3,null,3]
 * Output: false
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 1000].
 * -100 <= Node.val <= 100
 *
 *
 *
 * Follow up: Could you solve it both recursively and iteratively?
 */

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
    pub fn is_symmetric(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if root.is_none() {
            return true;
        }
        fn is_mirror(
            left: &Option<Rc<RefCell<TreeNode>>>,
            right: &Option<Rc<RefCell<TreeNode>>>,
        ) -> bool {
            if let Some(left) = left {
                if let Some(right) = right {
                    if left.borrow().val == right.borrow().val {
                        return is_mirror(&left.borrow().left, &right.borrow().right)
                            && is_mirror(&left.borrow().right, &right.borrow().left);
                    }
                }
            }
            return left == right;
        }
        return is_mirror(&root, &root);
    }
}
// @lc code=end

fn main() {}
