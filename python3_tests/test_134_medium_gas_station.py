import pytest
from lc_134_medium_gas_station import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "gas, cost, expected",
    [
        # testcases
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),
        ([1, 2, 3, 3, 6], [3, 4, 5, 1, 2], 3),
        ([2, 3, 4], [3, 4, 3], -1),
    ],
)
def test_canCompleteCircuit(solution: Solution, gas: list[int], cost: list[int], expected: int) -> None:
    assert solution.canCompleteCircuit(gas, cost) == expected
