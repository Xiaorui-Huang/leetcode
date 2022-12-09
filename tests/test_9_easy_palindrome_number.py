import pytest
from lc_9_easy_palindrome_number import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "number, expected",
    [
        # testcases
        (121, True),
        (-99, False),
        (788887, True),
        (0, True),
        (783927, False),
    ],
)
def test_isPalindrome(solution: Solution, number: int, expected: bool) -> None:
    assert solution.isPalindrome(number) == expected
