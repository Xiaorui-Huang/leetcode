import pytest
from lc_1519_medium_number_of_nodes_in_the_sub_tree_with_the_same_label import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, edges, labels, expected",
    [
        # testcases
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd", [2, 1, 1, 1, 1, 1, 1]),
        (4, [[0, 1], [1, 2], [0, 3]], "bbbb", [4, 2, 1, 1]),
        (5, [[0, 1], [0, 2], [1, 3], [0, 4]], "aabab", [3, 2, 1, 1, 1]),
    ],
)
def test_coungSubTrees(solution: Solution, n: int, edges: list[list[int]], labels: str, expected: list[int]) -> None:
    assert solution.countSubTrees(n, edges, labels) == expected
