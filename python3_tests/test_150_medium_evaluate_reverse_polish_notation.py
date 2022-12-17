import pytest
from lc_150_medium_evaluate_reverse_polish_notation import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "tokens, expected",
    [
        # testcases
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ],
)
def test_evalRPN(solution: Solution, tokens: list[str], expected: int) -> None:
    assert solution.evalRPN(tokens) == expected
