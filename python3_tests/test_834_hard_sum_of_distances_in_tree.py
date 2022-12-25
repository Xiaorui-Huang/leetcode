import pytest
from lc_834_hard_sum_of_distances_in_tree import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        # testcases
        (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]], [8, 12, 6, 10, 10, 10]),
        (1, [], [0]),
        (2, [[1, 0]], [1, 1]),
    ],
)
def test_sumOfDistancesInTree(solution: Solution, n: int, edges: list[list[int]], expected: list[int]) -> None:
    assert solution.sumOfDistancesInTree(n, edges) == expected
