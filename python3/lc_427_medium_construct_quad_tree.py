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
""" Saw this comment and thought it was a good idea to implement it

I met the follow up question in a microsoft interview. Assuming you have got a
constructed quad tree, now you are required to implement a public Node
set(int[][] grid, int x, int y, int val) to reconstruct the quad tree. 

posted it here: https://leetcode.com/problems/construct-quad-tree/description/comments/1816089
"""


class QuadTree:
    def __init__(
        self,
        val: bool,
        isLeaf: bool,
        # the level of the node in the whole QuadTree, block of size 1 is level
        # 0, block of size 2 is level 1, block of size 4 is level 2
        # in essence, the QuadTree represents a (2^level) * (2^level) matrix
        level: int,
        topLeft: QuadTree | None = None,
        topRight: QuadTree | None = None,
        bottomLeft: QuadTree | None = None,
        bottomRight: QuadTree | None = None,
    ):
        self.val = val
        self.isLeaf = isLeaf
        self.level = level
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def set_val(self, x: int, y: int, val: bool) -> None:
        """Set the value at (x, y) to val"""
        # base case set value is unchanged from what is already in the QuadTree
        if self.isLeaf and self.val == val:
            return

        # base case lowest level TODO: might not need this
        if self.level == 0:
            self.val = val
            self.isLeaf = True
            return

        # checking bounds first
        n = 2**self.level
        if x < 0 or n <= x or y < 0 or n <= y:
            return

        # if self is leaf but val is different or if self is not a leaf, we
        # would always need to have 4 children at this level
        self._divide_if_necessary()
        containing_sub: QuadTree
        containing_sub, new_x, new_y = self._get_containing_quad_and_coord(x, y)  # type: ignore
        containing_sub.isLeaf = False
        containing_sub.set_val(new_x, new_y, val)

        # merging after set_val if necessary
        children: list[QuadTree] = [self.topLeft, self.topRight, self.bottomLeft, self.bottomRight]  # type: ignore
        is_leaf = all((child.val == val and child.isLeaf) for child in children)
        if is_leaf:
            self.val = children[0].val
            self.isLeaf = True
            self.topLeft = None
            self.topRight = None
            self.bottomLeft = None
            self.bottomRight = None

    def _divide_if_necessary(self) -> None:
        if not self.topLeft:
            self.topLeft = QuadTree(self.val, True, self.level - 1)
        if not self.topRight:
            self.topRight = QuadTree(self.val, True, self.level - 1)
        if not self.bottomLeft:
            self.bottomLeft = QuadTree(self.val, True, self.level - 1)
        if not self.bottomRight:
            self.bottomRight = QuadTree(self.val, True, self.level - 1)

        self.isLeaf = False

    def _get_containing_quad_and_coord(self, x: int, y: int) -> tuple[QuadTree | None, int, int]:
        """Given the x, y coordinate of the representing matrix, return which
        sub quad contains the coord and the new coord in that sub quad

        Returns:
            tuple[QuadTree, int, int]: (x,y) coord containing sub quad, and ne w coord (x, y)
        """

        n = 2**self.level
        half = n // 2
        if x < half and y < half:
            return self.topLeft, x, y

        if x < half and y >= half:
            return self.topRight, x, y - half

        if x >= half and y < half:
            return self.bottomLeft, x - half, y

        return self.bottomRight, x - half, y - half

    def to_matrix(self) -> list[list[bool]]:
        """Convert the QuadTree to a matrix"""
        n = 2**self.level
        mat: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]
        self._quad_fill(0, 0, n, mat)
        return mat

    def _quad_fill(self, start_x: int, start_y: int, length: int, mat: list[list[bool]]) -> None:
        """recursively fill the matrix

        Args:
            start_x (int): the x coord upper left corner of the partition to fill
            start_y (int): the y coord upper left corner of the partition to fill
            length (int): the size of the current partition to fill
        """
        if self.isLeaf:
            for x in range(start_x, start_x + length):
                for y in range(start_y, start_y + length):
                    mat[x][y] = self.val
            return

        half = length // 2
        self.topLeft._quad_fill(start_x, start_y, half, mat)  # type: ignore
        self.topRight._quad_fill(start_x, start_y + half, half, mat)  # type: ignore
        self.bottomLeft._quad_fill(start_x + half, start_y, half, mat)  # type: ignore
        self.bottomRight._quad_fill(start_x + half, start_y + half, half, mat)  # type: ignore

    def __str__(self) -> str:
        return str([[int(x) for x in row] for row in self.to_matrix()])

    @classmethod
    def from_matrix(cls, mat: list[list[bool]]) -> QuadTree:
        """Construct a QuadTree from a matrix"""

        def quad_divide(start_x: int = 0, start_y: int = 0, length: int = len(mat)) -> QuadTree:
            """recursively construct a quad tree

            Args:
                start_x (int): the x coord upper left corner of the partition to construct
                start_y (int): the y coord upper left corner of the partition to construct
                length (int): the size of the current partition to construct

            Returns:
                QuadTree that is constructed
            """
            # base case
            if length == 1:
                return QuadTree(val=mat[start_x][start_y], isLeaf=True, level=0)

            half = length // 2
            children = [
                quad_divide(start_x, start_y, half),
                quad_divide(start_x, start_y + half, half),
                quad_divide(start_x + half, start_y, half),
                quad_divide(start_x + half, start_y + half, half),
            ]
            val = children[0].val
            level = children[0].level + 1

            # if not all are leafs and the value is the same -> this is also a leaf
            if not (is_leaf := all((child.val == val and child.isLeaf) for child in children)):
                # val is just a placeholder here, where it's value doesn't matter
                return QuadTree(val, is_leaf, level, *children)

            return QuadTree(val=val, isLeaf=True, level=level)

        return quad_divide()


def main() -> None:
    grid_int = [
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 0, 0, 0, 0],
    ]
    grid = [[bool(x) for x in row] for row in grid_int]

    root = QuadTree.from_matrix(grid)
    print(root)
    root.set_val(4, 6, False)
    root.set_val(5, 4, False)
    root.set_val(6, 5, False)
    root.set_val(6, 7, False)
    print(root)


if __name__ == "__main__":
    main()
