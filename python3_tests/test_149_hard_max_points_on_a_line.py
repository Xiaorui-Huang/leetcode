import pytest
from lc_149_hard_max_points_on_a_line import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "points, expected",
    [
        # testcases
        ([[1, 1]], 1),
        ([[1, 1], [4, 122]], 2),
        ([[0, 0], [1, 0]], 2),
        ([[0, 0], [0, 1], [0, -1]], 3),
        ([[0, 0], [0, 1], [1, -1]], 2),
        ([[1, 1], [2, 2], [3, 3]], 3),
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
        ([[1, 0], [1, 90], [1, -72], [-1, 1], [4, 0]], 3),
        ([[2, 3], [3, 3], [-5, 3]], 3),
    ],
)
def test_maxPoints(solution: Solution, points: list[tuple[int, int]], expected: int) -> None:
    assert solution.maxPoints(points) == expected
