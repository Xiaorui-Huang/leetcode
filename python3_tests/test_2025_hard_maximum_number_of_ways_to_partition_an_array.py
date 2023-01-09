import pytest
from lc_2025_hard_maximum_number_of_ways_to_partition_an_array import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        # testcases
        ([0, 0, 0], 1, 2),
        ([0, 0, 0, 3], 1, 0),
        ([0, 0, 0, 3], 0, 3),
        ([0, 0, 0, 3, 0], 0, 4),
        ([0, 0, 0, 3], -3, 2),
        ([2, -1, 2], 3, 1),
        ([2, 1, 3, 1, 3, 0, -4, 5, 2], 4, 2),
        ([22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], -33, 4),  # harder test case
    ],
)
def test_waysToPartition(solution: Solution, nums: list[int], k: int, expected: int) -> None:
    assert solution.waysToPartition(nums, k) == expected
