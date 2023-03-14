#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (53.25%)
# Likes:    12388
# Dislikes: 280
# Total Accepted:    1.5M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
#
# Example 1:
#
#
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#
#
# Example 2:
#
#
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#
#
#
# Constraints:
#
#
# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100
#
#
#
# Follow up: Could you solve it both recursively and iteratively?
#

from __future__ import annotations
from collections import deque

from typing import Any


from utils.binary_tree import TreeNode, build_bt


# @lc code=start
# Definition for a binary tree node.
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_level_symmetric(arr: list[Any]) -> bool:
            for i in range(len(arr) // 2):
                if arr[i] != arr[-i - 1]:
                    return False
            return True

        q: deque[TreeNode | None] = deque([root])
        while q:
            size = len(q)
            level_list: list[int | None] = []
            for _ in range(size):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level_list.append(node.val)
                else:
                    level_list.append(None)
            if not is_level_symmetric(level_list):
                return False
        return True


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.isSymmetric(build_bt([1, 2, 2, None, 3, None, 3]))
    print(ans)


if __name__ == "__main__":
    main()
