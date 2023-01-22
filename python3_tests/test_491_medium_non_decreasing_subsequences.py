import pytest
from lc_491_medium_non_decreasing_subsequences import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # testcases
        ([4, 6, 7, 7], [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]),
        ([4, 4, 3, 2, 1], [[4, 4]]),
    ],
)
def test_findSubsequences(solution: Solution, nums: list[int], expected: list[list[int]]) -> None:
    assert solution.findSubsequences(nums) == set([tuple(x) for x in expected])
