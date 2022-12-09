import pytest
from lc_323_medium_number_of_connected_components_in_an_undirected_graph import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "num_nodes, edges, expected",
    [
        # testcases
        (5, [[0, 1], [1, 2], [3, 4]], 2),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4]], 1),
        (4, [[2, 3], [1, 2], [1, 3]], 2),
    ],
)
def test_countComponents(solution: Solution, num_nodes: int, edges: list[tuple[int, int]], expected: int) -> None:
    assert solution.countComponents(num_nodes, edges) == expected
