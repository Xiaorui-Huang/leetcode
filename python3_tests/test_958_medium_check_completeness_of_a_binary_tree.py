import pytest
from lc_958_medium_check_completeness_of_a_binary_tree import Solution
from utils.binary_tree import TreeNode, build_bt, null


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        (build_bt([1, 2]), True),
        (build_bt([1, 2, 3, null, null, 7]), False),
        (build_bt([1, 2, 3, 5]), True),
        (build_bt([1, 2, 3, 5, null, 7]), False),
        (build_bt([1, 2, 3, 5, null, 7, 8]), False),
        (build_bt([1, 2, 3, 4, 5, 6]), True),
        (build_bt([1, 2, null, 5, 6]), False),
        (build_bt([1, 2, 3, 4, 5, null, 7]), False),
    ],
)
def test_is_complete_tree(solution: Solution, root: TreeNode | None, expected: bool) -> None:
    print(root)  # for visualization when debugging tests
    assert solution.isCompleteTree(root) == expected
