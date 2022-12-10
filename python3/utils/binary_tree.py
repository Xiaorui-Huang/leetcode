from __future__ import annotations
from typing import Any, Optional
from collections import deque

null: None = None


class TreeNode:
    def __init__(self, val: Any = 0, left: TreeNode | None = None, right: TreeNode | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val: Any) -> None:
        # already exist => do nothing
        if self.val == val:
            return
        # insert to the left
        elif val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)
        # insert to the right
        else:  # self.val < val
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.insert(val)

    def __eq__(self, other: object) -> bool:
        # use recursive value equals or equality:)
        if not isinstance(other, TreeNode):
            return NotImplemented
        return self.val == other.val and self.left == other.left and self.right == self.right

    # BST display code source
    # https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
    def __str__(self) -> str:
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self) -> tuple[list[str], int, int, int]:
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "%s" % self.val
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()  # type: ignore
            s = "%s" % self.val
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "_" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "%s" % self.val
            u = len(s)
            first_line = s + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "%s" % self.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


def build_bt(node_lst: list[Any]) -> Optional[TreeNode]:
    # empty tree
    n = len(node_lst)
    if not n:
        return None
    root = TreeNode(node_lst[0])

    q: deque[TreeNode] = deque([root])

    index = 1
    while index < n:
        cur = q.popleft()

        # index + 1 should exist by the structure of the input (i.e. if the last
        # leaf in empty should give null and not omit it)
        left = node_lst[index]
        right = node_lst[index + 1] if index + 1 < n else None

        # check None, if not null add to tree and put on queue for processing
        if left is not None:
            cur.left = TreeNode(left)
            q.append(cur.left)
        if right is not None:
            cur.right = TreeNode(right)
            q.append(cur.right)

        index += 2  # processed two more nodes

    return root
