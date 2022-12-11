import pytest
from lc_1165_easy_single_row_keyboard import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "keyboard, word, expected",
    [
        # testcases
        ("abcdefghijklmnopqrstuvwxyz", "cba", 4),
        ("pqrstuvwxyzabcdefghijklmno", "leetcode", 73),
    ],
)
def test_calculateTime(solution: Solution, keyboard: str, word: str, expected: int) -> None:
    assert solution.calculateTime(keyboard, word) == expected
