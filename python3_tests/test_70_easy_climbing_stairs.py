import pytest
from lc_70_easy_climbing_stairs import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "num_stairs, expected",
    [
        # testcases
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (6, 13),
        (7, 21),
        (8, 13 + 21),
    ],
)
def test_climbStairs(solution: Solution, num_stairs: int, expected: int) -> None:
    assert solution.climbStairs(num_stairs) == expected
