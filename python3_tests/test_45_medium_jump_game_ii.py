import pytest
from lc_45_medium_jump_game_ii import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # testcases
        ([0], 0),
        ([1, 0], 1),
        ([1, 2, 3], 2),
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
        ([2, 0, 2, 0, 1], 2),
        ([1, 1, 1, 3, 2, 5, 0], 4),
        ([1, 2, 1, 3, 2, 5, 0], 3),
    ],
)
def test_jump(solution: Solution, nums: list[int], expected: int) -> None:
    assert solution.jump(nums) == expected
