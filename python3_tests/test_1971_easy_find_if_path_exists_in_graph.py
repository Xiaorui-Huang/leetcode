import pytest
from lc_1971_easy_find_if_path_exists_in_graph import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "n, edges, source, destination, expected",
    [
        # testcases
        (3, [[0, 1], [1, 2], [2, 0]], 0, 2, True),
        (6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5, False),
    ],
)
def test_validPath(
    solution: Solution, n: int, edges: list[list[int]], source: int, destination: int, expected: bool
) -> None:
    assert solution.validPath(n, edges, source, destination) == expected
