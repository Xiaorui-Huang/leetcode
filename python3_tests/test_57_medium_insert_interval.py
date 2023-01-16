import pytest
from lc_57_medium_insert_interval import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "intervals, newInterval, expected",
    [
        # testcases
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 7], [[1, 2], [3, 7], [8, 10], [12, 16]]),
        ([[1, 2], [3, 5], [6, 7], [9, 10], [15, 16]], [11, 14], [[1, 2], [3, 5], [6, 7], [9, 10], [11, 14], [15, 16]]),
        ([[1, 2], [3, 5], [6, 7], [9, 10], [15, 16]], [11, 200], [[1, 2], [3, 5], [6, 7], [9, 10], [11, 200]]),
        ([[1, 2], [3, 5], [6, 7], [9, 10], [12, 16]], [7, 8], [[1, 2], [3, 5], [6, 8], [9, 10], [12, 16]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [0, 1], [[0, 2], [3, 5], [6, 7], [8, 10], [12, 16]]),
        ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
        ([[1, 3], [6, 9]], [1, 9], [[1, 9]]),
        ([[1, 3], [6, 9]], [1, 10], [[1, 10]]),
        ([[1, 3], [6, 9]], [0, 111], [[0, 111]]),
        ([[1, 3], [6, 9]], [-1, 0], [[-1, 0], [1, 3], [6, 9]]),
        ([[1, 3], [6, 9]], [0, 0], [[0, 0], [1, 3], [6, 9]]),
        ([[1, 3], [6, 9]], [0, 1], [[0, 3], [6, 9]]),
        ([[1, 3], [6, 9]], [10, 11], [[1, 3], [6, 9], [10, 11]]),
        ([[1, 3], [6, 9]], [9, 11], [[1, 3], [6, 11]]),
        ([], [1, 3], [[1, 3]]),
    ],
)
def test_insert(
    solution: Solution, intervals: list[list[int]], newInterval: list[int], expected: list[list[int]]
) -> None:
    assert solution.insert(intervals, newInterval) == expected
