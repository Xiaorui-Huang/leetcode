import pytest
from lc_1443_medium_minimum_time_to_collect_all_apples_in_a_tree import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


false = False
true = True


@pytest.mark.parametrize(
    "n, edges, hasApple, expected",
    [
        # testcases
        (3, [[0, 1], [0, 2]], [false, false, true], 2),
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [false, false, true, false, false, true, false], 6),
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [false, false, true, false, true, true, false], 8),
        (7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [false, false, false, false, false, false, false], 0),
    ],
)
def test_minTime(solution: Solution, n: int, edges: list[list[int]], hasApple: list[bool], expected: int) -> None:
    assert solution.minTime(n, edges, hasApple) == expected
