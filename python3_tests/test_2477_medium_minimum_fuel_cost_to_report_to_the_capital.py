import pytest
from lc_2477_medium_minimum_fuel_cost_to_report_to_the_capital import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "roads, seats, expected",
    [
        # testcases
        ([], 1, 0),
        ([[0, 1], [0, 2], [0, 3]], 5, 3),
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7),
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6], [3, 7]], 2, 9),
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6], [3, 7], [1, 8]], 2, 11),
        ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6], [3, 7]], 3, 8),
    ],
)
def test_min_fuel_cost(solution: Solution, roads: list[list[int]], seats: int, expected: int) -> None:
    assert solution.minimumFuelCost(roads, seats) == expected
