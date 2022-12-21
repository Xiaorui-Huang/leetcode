import pytest
from lc_841_medium_keys_and_rooms import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "rooms, expected",
    [
        # testcases
        ([[1], [2], [3], []], True),
        ([[1, 3], [3, 0, 1], [2], [0]], False),
    ],
)
def test_canVisitAllRooms(solution: Solution, rooms: list[list[int]], expected: bool) -> None:
    assert solution.canVisitAllRooms(rooms) == expected
