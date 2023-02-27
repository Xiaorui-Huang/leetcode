#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#
# https://leetcode.com/problems/construct-quad-tree/description/
#
# algorithms
# Medium (66.58%)
# Likes:    594
# Dislikes: 807
# Total Accepted:    52.7K
# Total Submissions: 78.8K
# Testcase Example:  '[[0,1],[1,0]]'
#
# Given a n * n matrix grid of 0's and 1's only. We want to represent the grid
# with a Quad-Tree.
#
# Return the root of the Quad-Tree representing the grid.
#
# Notice that you can assign the value of a node to True or False when isLeaf
# is False, and both are accepted in the answer.
#
# A Quad-Tree is a tree data structure in which each internal node has exactly
# four children. Besides, each node has two attributes:
#
#
# val: True if the node represents a grid of 1's or False if the node
# represents a grid of 0's.
# isLeaf: True if the node is leaf node on the tree or False if the node has
# the four children.
#
#
#
# class Node {
# ⁠   public boolean val;
# ⁠   public boolean isLeaf;
# ⁠   public Node topLeft;
# ⁠   public Node topRight;
# ⁠   public Node bottomLeft;
# ⁠   public Node bottomRight;
# }
#
# We can construct a Quad-Tree from a two-dimensional area using the following
# steps:
#
#
# If the current grid has the same value (i.e all 1's or all 0's) set isLeaf
# True and set val to the value of the grid and set the four children to Null
# and stop.
# If the current grid has different values, set isLeaf to False and set val to
# any value and divide the current grid into four sub-grids as shown in the
# photo.
# Recurse for each of the children with the proper sub-grid.
#
#
# If you want to know more about the Quad-Tree, you can refer to the wiki.
#
# Quad-Tree format:
#
# The output represents the serialized format of a Quad-Tree using level order
# traversal, where null signifies a path terminator where no node exists
# below.
#
# It is very similar to the serialization of the binary tree. The only
# difference is that the node is represented as a list [isLeaf, val].
#
# If the value of isLeaf or val is True we represent it as 1 in the list
# [isLeaf, val] and if the value of isLeaf or val is False we represent it as
# 0.
#
#
# Example 1:
#
#
# Input: grid = [[0,1],[1,0]]
# Output: [[0,1],[1,0],[1,1],[1,1],[1,0]]
# Explanation: The explanation of this example is shown below:
# Notice that 0 represnts False and 1 represents True in the photo representing
# the Quad-Tree.
#
#
#
# Example 2:
#
#
#
#
# Input: grid =
# [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
# Output:
# [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
# Explanation: All values in the grid are not the same. We divide the grid into
# four sub-grids.
# The topLeft, bottomLeft and bottomRight each has the same value.
# The topRight have different values so we divide it into 4 sub-grids where
# each has the same value.
# Explanation is shown in the photo below:
#
#
#
#
# Constraints:
#
#
# n == grid.length == grid[i].length
# n == 2^x where 0 <= x <= 6
#
#
#

"""
# Definition for a QuadTree node.
"""
from __future__ import annotations


class Node:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        topLeft: Node | None = None,
        topRight: Node | None = None,
        bottomLeft: Node | None = None,
        bottomRight: Node | None = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


# @lc code=start
class Solution:
    def construct(self, grid: list[list[bool]]) -> "Node":
        def quad_divide(start_x: int = 0, start_y: int = 0, length: int = len(grid)) -> "Node":
            """recursively construct a quad tree

            Args:
                start_x (int): the x coord upper left corner of the partition to construct
                start_y (int): the y coord upper left corner of the partition to construct
                length (int): the size of the current partition to construct

            Returns:
                Node that is constructed
            """
            # base case
            if length == 1:
                return Node(val=grid[start_x][start_y], isLeaf=True)

            half = length // 2
            children = [
                quad_divide(start_x, start_y, half),
                quad_divide(start_x, start_y + half, half),
                quad_divide(start_x + half, start_y, half),
                quad_divide(start_x + half, start_y + half, half),
            ]
            val = children[0].val

            # if not all are leafs and the value is the same -> this is also a leaf
            if not (is_leaf := all((child.val == val and child.isLeaf) for child in children)):
                # val is just a placeholder here, where it's value doesn't matter
                return Node(val, is_leaf, *children)

            return Node(val=val, isLeaf=True)

        return quad_divide()


# @lc code=end


def main() -> None:
    sol = Solution()
    grid = [
        [True, True, True, True, False, False, False, False],
        [True, True, True, True, False, False, False, False],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True],
        [True, True, True, True, False, False, False, False],
        [True, True, True, True, False, False, False, False],
        [True, True, True, True, False, False, False, False],
        [True, True, True, True, False, False, False, False],
    ]
    ans = sol.construct(grid)
    print(ans)


if __name__ == "__main__":
    main()
