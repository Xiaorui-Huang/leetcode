import pytest
from lc_433_medium_minimum_genetic_mutation import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "startGene, endGene, bank, expected",
    [
        # testcases
        ("AACCGGTT", "AACCGGTA", ["AACCGGTC"], -1),
        ("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1),
        ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2),
        ("AACCGGTT", "AACAGGTA", ["AACCGGTA", "AACAGGTA", "AAACGGTA", "AAAAGGTA"], 2),
        ("AACCGGTT", "AAAAGGTA", ["AACCGGTA", "AAACGGTA", "AAAAGGTA"], 3),
    ],
)
def test_minMutation(solution: Solution, startGene: str, endGene: str, bank: list[str], expected: int) -> None:
    assert solution.minMutation(startGene, endGene, bank) == expected
