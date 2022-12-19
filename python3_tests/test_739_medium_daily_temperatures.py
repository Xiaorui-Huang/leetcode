import pytest
from lc_739_medium_daily_temperatures import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


# Constraints:
#
#
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        # testcases
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
    ],
)
def test_dailyTemperatures(solution: Solution, temperatures: list[int], expected: list[int]) -> None:
    assert solution.dailyTemperatures(temperatures) == expected
