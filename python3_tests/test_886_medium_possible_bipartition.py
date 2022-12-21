import pytest
from lc_886_medium_possible_bipartition import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, dislikes, expected",
    [
        # testcases
        (4, [[1, 2], [1, 3], [2, 4]], True),
        (3, [[1, 2], [1, 3], [2, 3]], False),
        (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False),
        (10, [[1, 2], [3, 4], [5, 6], [6, 7], [8, 9], [7, 8]], True),
        (
            10,
            [
                [4, 7],
                [4, 8],
                [5, 6],
                [1, 6],
                [3, 7],
                [2, 5],
                [5, 8],
                [1, 2],
                [4, 9],
                [6, 10],
                [8, 10],
                [3, 6],
                [2, 10],
                [9, 10],
                [3, 9],
                [2, 3],
                [1, 9],
                [4, 6],
                [5, 7],
                [3, 8],
                [1, 8],
                [1, 7],
                [2, 4],
            ],
            True,
        ),
    ],
)
def test_possibleBipartition(solution: Solution, n: int, dislikes: list[list[int]], expected: bool) -> None:
    assert solution.possibleBipartition(n, dislikes) == expected
