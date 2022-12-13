import pytest
from lc_124_hard_binary_tree_maximum_path_sum import Solution

from utils.binary_tree import TreeNode, build_bt

# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        (build_bt([-10, 9, 20, None, None, 15, 7]), 42),
        (build_bt([1, 2, 3]), 6),
    ],
)
def test_maxPathSum(solution: Solution, root: TreeNode, expected: int) -> None:
    assert solution.maxPathSum(root) == expected
