import pytest
from lc_6_medium_zigzag_conversion import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s, num_rows, expected",
    [
        # testcases
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("AB", 1, "AB"),
    ],
)
def test_convert(solution: Solution, s: str, num_rows: int, expected: str) -> None:
    assert solution.convert(s, num_rows) == expected
