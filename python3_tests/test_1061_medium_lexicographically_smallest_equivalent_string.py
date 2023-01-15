import pytest
from lc_1061_medium_lexicographically_smallest_equivalent_string import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s1, s2, baseStr, expected",
    [
        # testcases
        ("hello", "world", "hold", "hdld"),
    ],
)
def test_smallestequivalentString(solution: Solution, s1: str, s2: str, baseStr: str, expected: str) -> None:
    assert solution.smallestEquivalentString(s1, s2, baseStr) == expected
