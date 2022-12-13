import pytest
from lc_872_easy_leaf_similar_trees import Solution


from utils.binary_tree import TreeNode, build_bt, null

# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "root1, root2, expected",
    [
        # testcases
        (
            build_bt([3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]),
            build_bt([3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]),
            True,
        ),
        (build_bt([1, 2, 3]), build_bt([1, 3, 2]), False),
    ],
)
def test_similarLeaf(solution: Solution, root1: TreeNode | None, root2: TreeNode | None, expected: bool) -> None:
    assert solution.leafSimilar(root1, root2) == expected
