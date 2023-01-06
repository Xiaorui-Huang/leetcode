import pytest
from lc_520_easy_detect_capital import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "word, expected",
    [
        # testcases
        ("USA", True),
        ("leetcode", True),
        ("Google", True),
        ("GooGle", False),
        ("gooGle", False),
        ("google", True),
        ("A", True),
        ("z", True),
        ("zA", False),
        ("Az", True),
    ],
)
def test_detectCapitalUse(solution: Solution, word: str, expected: bool) -> None:
    assert solution.detectCapitalUse(word) == expected
