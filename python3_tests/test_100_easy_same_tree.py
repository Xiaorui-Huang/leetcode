import pytest
from lc_100_easy_same_tree import Solution
from utils.binary_tree import null, build_bt


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "p, q, expected",
    [
        # testcases
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, null, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
    ],
)
def test_isSameTree(solution: Solution, p: list[int | None], q: list[int | None], expected: bool) -> None:
    assert solution.isSameTree(build_bt(p), build_bt(q)) == expected
