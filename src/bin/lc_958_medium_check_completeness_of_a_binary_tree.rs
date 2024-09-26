/*
 * @lc app=leetcode id=958 lang=rust
 *
 * [958] Check Completeness of a Binary Tree
 *
 * https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
 *
 * algorithms
 * Medium (53.87%)
 * Likes:    2539
 * Dislikes: 34
 * Total Accepted:    138.1K
 * Total Submissions: 255.1K
 * Testcase Example:  '[1,2,3,4,5,6]'
 *
 * Given the root of a binary tree, determine if it is a complete binary tree.
 *
 * In a complete binary tree, every level, except possibly the last, is
 * completely filled, and all nodes in the last level are as far left as
 * possible. It can have between 1 and 2^h nodes inclusive at the last level
 * h.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3,4,5,6]
 * Output: true
 * Explanation: Every level before the last is full (ie. levels with
 * node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are
 * as far left as possible.
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1,2,3,4,5,null,7]
 * Output: false
 * Explanation: The node with value 7 isn't as far left as possible.
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 100].
 * 1 <= Node.val <= 1000
 *
 *
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
enum Approach {
    BFS,
    DFS,
}
const APPROACH: Approach = Approach::DFS;

use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;
impl Solution {
    pub fn is_complete_tree(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        match APPROACH {
            Approach::BFS => Self::is_complete_tree_BFS(root),
            Approach::DFS => Self::is_complete_tree_DFS(root),
        }
    }
    fn is_complete_tree_BFS(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut null_found = false;
        let mut queue = VecDeque::new();
        queue.push_back(root);
        while !queue.is_empty() {
            let node = queue.pop_front().unwrap();
            if let Some(node) = node {
                if null_found {
                    return false;
                }
                queue.push_back(node.borrow().left.clone());
                queue.push_back(node.borrow().right.clone());
            } else {
                null_found = true;
            }
        }
        return true;
    }

    fn is_complete_tree_DFS(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        // count the total number of nodes
        let n = count_nodes(root.clone());
        return dfs(root, 0, &n);

        fn dfs(node: Option<Rc<RefCell<TreeNode>>>, index: i32, count: &i32) -> bool {
            if let Some(node) = node {
                // misplaced node in a complete tree
                if index >= *count {
                    return false;
                }
                let (left_index, right_index) = (2 * index + 1, 2 * index + 2);
                return dfs(node.borrow().left.clone(), left_index, count)
                    && dfs(node.borrow().right.clone(), right_index, count);
            }
            return true;
        }
        fn count_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
            if let Some(node) = root {
                return 1
                    + count_nodes(node.borrow().left.clone())
                    + count_nodes(node.borrow().right.clone());
            }
            return 0;
        }
    }
}
// @lc code=end

fn main() {}
