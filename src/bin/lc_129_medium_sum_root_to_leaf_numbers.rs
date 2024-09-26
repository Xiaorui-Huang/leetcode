/*
 * @lc app=leetcode id=129 lang=rust
 *
 * [129] Sum Root to Leaf Numbers
 *
 * https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
 *
 * algorithms
 * Medium (59.02%)
 * Likes:    5472
 * Dislikes: 96
 * Total Accepted:    535.6K
 * Total Submissions: 903.6K
 * Testcase Example:  '[1,2,3]'
 *
 * You are given the root of a binary tree containing digits from 0 to 9 only.
 *
 * Each root-to-leaf path in the tree represents a number.
 *
 *
 * For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
 *
 *
 * Return the total sum of all root-to-leaf numbers. Test cases are generated
 * so that the answer will fit in a 32-bit integer.
 *
 * A leaf node is a node with no children.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3]
 * Output: 25
 * Explanation:
 * The root-to-leaf path 1->2 represents the number 12.
 * The root-to-leaf path 1->3 represents the number 13.
 * Therefore, sum = 12 + 13 = 25.
 *
 *
 * Example 2:
 *
 *
 * Input: root = [4,9,0,5,1]
 * Output: 1026
 * Explanation:
 * The root-to-leaf path 4->9->5 represents the number 495.
 * The root-to-leaf path 4->9->1 represents the number 491.
 * The root-to-leaf path 4->0 represents the number 40.
 * Therefore, sum = 495 + 491 + 40 = 1026.
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 1000].
 * 0 <= Node.val <= 9
 * The depth of the tree will not exceed 10.
 *
 *
 */
struct Solution;

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
// @lc code=start
use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    pub fn sum_numbers(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut total = 0;
        fn dfs(node: &Option<Rc<RefCell<TreeNode>>>, num: i32, total: &mut i32) {
            if let Some(node) = node {
                let cur = num * 10 + node.borrow().val;
                if node.borrow().left.is_none() && node.borrow().right.is_none() {
                    *total += cur
                }
                dfs(&node.borrow().left, cur, total);
                dfs(&node.borrow().right, cur, total);
            }
        }
        dfs(&root, 0, &mut total);
        return total;
    }
}
// @lc code=end
fn main() {}
