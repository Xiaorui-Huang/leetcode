import pytest
from lc_290_easy_word_pattern import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "pattern, s, expected",
    [
        # testcases
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
    ],
)
def test_wordPattern(solution: Solution, pattern: str, s: str, expected: bool) -> None:

    assert solution.wordPattern(pattern, s) == expected
