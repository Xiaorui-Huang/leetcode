import pytest
from lc_144_easy_binary_tree_preorder_traversal import Solution
from utils.binary_tree import TreeNode, build_bt, null


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        ([1, null, 2, 3], [1, 2, 3]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7]),
    ],
)
def test_preorderTraversal(solution: Solution, root: list[int | None], expected: list[int]) -> None:
    assert solution.preorderTraversal(build_bt(root)) == expected
