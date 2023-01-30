import pytest
from lc_1137_easy_n_th_tribonacci_number import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, expected",
    [
        # testcases
        (4, 4),
        (25, 1389537),
    ],
)
def test_tribonacci(solution: Solution, n: int, expected: int) -> None:
    assert solution.tribonacci(n) == expected
