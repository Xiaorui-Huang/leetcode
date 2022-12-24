import pytest
from lc_2506_easy_count_pairs_of_similar_strings import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "words, expected",
    [
        # testcases
        (["aba", "aabb", "abcd", "bac", "aabc"], 2),
        (["aabb", "ab", "ba"], 3),
    ],
)
def test_similarPairs(solution: Solution, words: list[str], expected: int) -> None:
    assert solution.similarPairs(words) == expected
