import pytest
from lc_1129_medium_shortest_path_with_alternating_colors import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, red, blue, expected",
    [
        # testcases
        (3, [[0, 1], [0, 2]], [[1, 0]], [0, 1, 1]),
    ],
)
def test_shortest_alt_path(
    solution: Solution, n: int, red: list[list[int]], blue: list[list[int]], expected: list[int]
) -> None:
    assert solution.shortestAlternatingPaths(n, red, blue) == expected
