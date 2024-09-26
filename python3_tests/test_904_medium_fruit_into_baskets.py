import pytest
from lc_904_medium_fruit_into_baskets import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "fruits, expected",
    [
        # testcases
        ([1], 1),
        ([1, 2], 2),
        ([1, 1], 2),
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
        ([1, 2, 1, 1, 3, 2, 3, 3, 2, 1, 1, 2, 3], 5),
    ],
)
def test_totalFruits(solution: Solution, fruits: list[int], expected: int) -> None:
    assert solution.totalFruit(fruits) == expected
