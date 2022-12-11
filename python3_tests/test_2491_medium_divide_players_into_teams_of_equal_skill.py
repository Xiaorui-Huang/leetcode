import pytest
from lc_2491_medium_divide_players_into_teams_of_equal_skill import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "skill, expected",
    [
        # testcases
        ([3, 2, 5, 1, 3, 4], 22),
        ([3, 4], 12),
        ([1, 1, 2, 3], -1),
        ([1, 1, 2, 4], -1),
        ([1, 100, 50, 51], 2650),
    ],
)
def test_dividePlayers(solution: Solution, skill: list[int], expected: int) -> None:
    assert solution.dividePlayers(skill) == expected
