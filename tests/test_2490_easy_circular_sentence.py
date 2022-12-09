import pytest
from lc_2490_easy_circular_sentence import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "sentence, expected",
    [
        ("leetcode exercises sound delightful", True),
        ("eetcode", True),
        ("Leetcode essensec cool", False),
        ("ab a", False),
    ],
)
def test_isCircularSentence(solution: Solution, sentence: str, expected: bool) -> None:
    assert solution.isCircularSentence(sentence) == expected
