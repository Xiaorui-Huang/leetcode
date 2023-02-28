/*
 * @lc app=leetcode id=652 lang=rust
 *
 * [652] Find Duplicate Subtrees
 *
 * https://leetcode.com/problems/find-duplicate-subtrees/description/
 *
 * algorithms
 * Medium (56.51%)
 * Likes:    4064
 * Dislikes: 341
 * Total Accepted:    183.9K
 * Total Submissions: 324.4K
 * Testcase Example:  '[1,2,3,4,null,2,4,null,null,4]'
 *
 * Given the root of a binary tree, return all duplicate subtrees.
 *
 * For each kind of duplicate subtrees, you only need to return the root node
 * of any one of them.
 *
 * Two trees are duplicate if they have the same structure with the same node
 * values.
 *
 *
 * Example 1:
 *
 *
 * Input: root = [1,2,3,4,null,2,4,null,null,4]
 * Output: [[2,4],[4]]
 *
 *
 * Example 2:
 *
 *
 * Input: root = [2,1,1]
 * Output: [[1]]
 *
 *
 * Example 3:
 *
 *
 * Input: root = [2,2,2,3,null,3,null]
 * Output: [[2,3],[3]]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of the nodes in the tree will be in the range [1, 5000]
 * -200 <= Node.val <= 200
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
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::Rc;
impl Solution {
    pub fn find_duplicate_subtrees(
        root: Option<Rc<RefCell<TreeNode>>>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let mut duplicates = vec![];
        let mut counts = HashMap::new();
        let mut triplet_ids = HashMap::new();

        fn dfs(
            root: Option<Rc<RefCell<TreeNode>>>,
            counts: &mut HashMap<usize, usize>,
            triplet_ids: &mut HashMap<(usize, i32, usize), usize>,
            duplicates: &mut Vec<Option<Rc<RefCell<TreeNode>>>>,
        ) -> usize {
            let mut id = 0;
            let root_clone = root.clone();
            if let Some(node) = root {
                let node = node.borrow();
                let left = dfs(node.left.clone(), counts, triplet_ids, duplicates);
                let right = dfs(node.right.clone(), counts, triplet_ids, duplicates);
                let triplet = (left, node.val, right);

                let cur_max_id = triplet_ids.len();
                id = *triplet_ids.entry(triplet).or_insert(cur_max_id + 1);

                let occurrences = counts.entry(id).and_modify(|c| *c += 1).or_insert(1);
                if *occurrences == 2 {
                    duplicates.push(root_clone);
                }
            }
            return id;
        }
        dfs(root, &mut counts, &mut triplet_ids, &mut duplicates);

        return duplicates;
    }
}
// @lc code=end
fn main() {}
