import pytest
from lc_20_easy_valid_parentheses import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s, expected",
    [
        # testcases
        ("()", True),
        ("()[]", True),
        ("{()[]}", True),
        ("{(][]}", False),
        ("[", False),
        ("]", False),
        ("((", False),
        ("))", False),
        ("()}]", False),
    ],
)
def test_isValid(solution: Solution, s: str, expected: bool) -> None:
    assert solution.isValid(s) == expected
