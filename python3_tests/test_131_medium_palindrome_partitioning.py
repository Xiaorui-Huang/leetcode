import pytest
from lc_131_medium_palindrome_partitioning import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s, expected",
    [
        # testcases
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
        ("aba", [["a", "b", "a"], ["aba"]]),
        (
            "aaaabbc",
            [
                ["a", "a", "a", "a", "b", "b", "c"],
                ["a", "a", "a", "a", "bb", "c"],
                ["a", "a", "aa", "b", "b", "c"],
                ["a", "a", "aa", "bb", "c"],
                ["a", "aa", "a", "b", "b", "c"],
                ["a", "aa", "a", "bb", "c"],
                ["a", "aaa", "b", "b", "c"],
                ["a", "aaa", "bb", "c"],
                ["aa", "a", "a", "b", "b", "c"],
                ["aa", "a", "a", "bb", "c"],
                ["aa", "aa", "b", "b", "c"],
                ["aa", "aa", "bb", "c"],
                ["aaa", "a", "b", "b", "c"],
                ["aaa", "a", "bb", "c"],
                ["aaaa", "b", "b", "c"],
                ["aaaa", "bb", "c"],
            ],
        ),
        (
            "abaclinilcuu",
            [
                ["a", "b", "a", "c", "l", "i", "n", "i", "l", "c", "u", "u"],
                ["a", "b", "a", "c", "l", "i", "n", "i", "l", "c", "uu"],
                ["a", "b", "a", "c", "l", "ini", "l", "c", "u", "u"],
                ["a", "b", "a", "c", "l", "ini", "l", "c", "uu"],
                ["a", "b", "a", "c", "linil", "c", "u", "u"],
                ["a", "b", "a", "c", "linil", "c", "uu"],
                ["a", "b", "a", "clinilc", "u", "u"],
                ["a", "b", "a", "clinilc", "uu"],
                ["aba", "c", "l", "i", "n", "i", "l", "c", "u", "u"],
                ["aba", "c", "l", "i", "n", "i", "l", "c", "uu"],
                ["aba", "c", "l", "ini", "l", "c", "u", "u"],
                ["aba", "c", "l", "ini", "l", "c", "uu"],
                ["aba", "c", "linil", "c", "u", "u"],
                ["aba", "c", "linil", "c", "uu"],
                ["aba", "clinilc", "u", "u"],
                ["aba", "clinilc", "uu"],
            ],
        ),
    ],
)
def test_partition(solution: Solution, s: str, expected: list[list[str]]) -> None:
    assert set(tuple(x) for x in solution.partition(s)) == set(tuple(x) for x in expected)
