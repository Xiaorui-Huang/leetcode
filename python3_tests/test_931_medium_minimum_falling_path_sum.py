from typing import TypeAlias
import pytest
from lc_931_medium_minimum_falling_path_sum import Solution

Matrix: TypeAlias = list[list[int]]

# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "matrix, expected",
    [
        # testcases
        (
            [
                #
                [2, 1, 3],
                [6, 5, 4],
                [7, 8, 9],
            ],
            13,
        ),
        (
            [
                #
                [-19, 57],
                [-40, -5],
            ],
            -59,
        ),
        (
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30],
            ],
            65,
        ),
        (
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [40, 40, 27, 28, 29, 30],
            ],
            68,
        ),
    ],
)
def test_case_name(solution: Solution, matrix: Matrix, expected: int) -> None:
    assert solution.minFallingPathSum(matrix) == expected
