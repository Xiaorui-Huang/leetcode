import pytest
from lc_72_hard_edit_distance import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "word1, word2, expected",
    [
        # testcases
        ("abc", "aqc", 1),
        ("abc", "abe", 1),
        ("abc", "abc", 0),
        ("horse", "ros", 3),
        ("ros", "horse", 3),
        ("intention", "execution", 5),
        ("execution", "intention", 5),
    ],
)
def test_min_distance(solution: Solution, word1: str, word2: str, expected: int) -> None:
    assert solution.minDistance(word1, word2) == expected
