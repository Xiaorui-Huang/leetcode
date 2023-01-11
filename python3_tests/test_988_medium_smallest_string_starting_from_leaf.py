import pytest
from lc_988_medium_smallest_string_starting_from_leaf import Solution
from utils.binary_tree import TreeNode, build_bt, null


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        (build_bt([0, 1, 2, 3, 4, 3, 4]), "dba"),
        (build_bt([25, 1, 3, 1, 3, 0, 2]), "adz"),
        (build_bt([2, 2, 1, null, 1, 0, null, 0]), "abc"),
        (build_bt([0, 1, 2, 3, 4, 3, 4, 1, 2, null, 5]), "bdba"),
        (build_bt([0, 1, 2, 1, 4]), "bba"),
    ],
)
def test_smallestFromLeaf(solution: Solution, root: TreeNode | None, expected: str) -> None:
    assert solution.smallestFromLeaf(root) == expected
