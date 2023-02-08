import pytest
from lc_300_medium_longest_increasing_subsequence import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # testcases
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([10, 9, 2, 5, 3, 7, 101, 18, 19, 7, 22], 6),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ],
)
def test_length_of_LIS(solution: Solution, nums: list[int], expected: int) -> None:
    assert solution.lengthOfLIS(nums) == expected
