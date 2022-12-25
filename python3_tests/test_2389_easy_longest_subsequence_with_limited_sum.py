import pytest
from lc_2389_easy_longest_subsequence_with_limited_sum import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "nums, queries, expected",
    [
        # testcases
        ([4, 5, 2, 1], [3, 10, 21], [2, 3, 4]),
        ([2, 3, 4, 5], [1], [0]),
    ],
)
def test_answerQueries(solution: Solution, nums: list[int], queries: list[int], expected: list[int]) -> None:
    assert solution.answerQueries(nums, queries) == expected
