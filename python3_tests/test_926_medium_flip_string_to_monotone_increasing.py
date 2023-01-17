import pytest
from lc_926_medium_flip_string_to_monotone_increasing import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s, expected",
    [
        # testcases
        ("00110", 1),
        ("0101110", 2),
        ("00011000", 2),
        ("01111010", 2),
        ("11011", 1),
        ("0101100011", 3),
        ("10011111110010111011", 5),
        ("101010111001010000011101101110", 11),
    ],
)
def test_minFlipsMonoIncr(solution: Solution, s: str, expected: int) -> None:
    assert solution.minFlipsMonoIncr(s) == expected
