import pytest
from lc_2492_medium_minimum_score_of_a_path_between_two_cities import Solution  # type: ignore


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, roads, expected",
    [
        # testcases
        (5, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
        (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
        (
            6,
            [
                [4, 5, 7468],
                [6, 2, 7173],
                [6, 3, 8365],
                [2, 3, 7674],
                [5, 6, 7852],
                [1, 2, 8547],
                [2, 4, 1885],
                [2, 5, 5192],
                [1, 3, 4065],
                [1, 4, 7357],
            ],
            1885,
        ),
        (
            20,
            [
                [18, 20, 9207],
                [14, 12, 1024],
                [11, 9, 3056],
                [8, 19, 416],
                [3, 18, 5898],
                [17, 3, 6779],
                [13, 15, 3539],
                [15, 11, 1451],
                [19, 2, 3805],
                [9, 8, 2238],
                [1, 16, 618],
                [16, 14, 55],
                [17, 7, 6903],
                [12, 13, 1559],
                [2, 17, 3693],
            ],
            55,
        ),
    ],
)
def test_minScore(solution: Solution, n: int, roads: list[tuple[int, int, int]], expected: int) -> None:
    assert solution.minScore(n, roads) == expected
