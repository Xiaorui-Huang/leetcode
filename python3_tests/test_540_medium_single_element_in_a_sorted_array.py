import pytest
from lc_540_medium_single_element_in_a_sorted_array import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # testcases
        ([1, 1, 2], 2),
        ([3, 4, 4], 3),
        ([3, 3, 4, 6, 6], 4),
        ([3, 5, 5, 7, 7], 3),
        ([3, 3, 7, 7, 8], 8),
        ([3, 3, 7, 7, 8, 9, 9], 8),
    ],
)
def test_single_non_duplicate(solution: Solution, nums: list[int], expected: int) -> None:
    assert solution.singleNonDuplicate(nums) == expected
