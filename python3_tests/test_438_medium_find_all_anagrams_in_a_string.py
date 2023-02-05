import pytest
from lc_438_medium_find_all_anagrams_in_a_string import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s, p, expected",
    [
        # testcases
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
    ],
)
def test_find_anagrams(solution: Solution, s: str, p: str, expected: list[int]) -> None:
    assert solution.findAnagrams(s, p) == expected
