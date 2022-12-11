import pytest
from lc_1026_medium_maximum_difference_between_node_and_ancestor import Solution
from utils.binary_tree import TreeNode, build_bt, null


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        (build_bt([8, 3, 10, 1, 6, null, 14, null, null, 4, 7, 13]), 7),
        (build_bt([1, null, 2, null, 0, 3]), 3),
    ],
)
def test_maxAncestorDiff(solution: Solution, root: TreeNode, expected: int) -> None:
    assert solution.maxAncestorDiff(root) == expected
