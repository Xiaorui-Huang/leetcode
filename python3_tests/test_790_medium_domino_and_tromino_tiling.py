import pytest
from lc_790_medium_domino_and_tromino_tiling import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, expected",
    [
        # testcases
        (4, 11),
        (5, 24),
        (6, 53),
    ],
)
def test_numTilings(solution: Solution, n: int, expected: int) -> None:
    assert solution.numTilings(n) == expected
