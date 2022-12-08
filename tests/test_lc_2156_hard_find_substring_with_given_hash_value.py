import pytest

from python3.lc_2156_hard_find_substring_with_given_hash_value import Solution


# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "s, power, modulo, k, hashValue, expected_substr",
    [
        ("leetcode", 7, 20, 2, 0, "ee"),
        ("fbxzaad", 31, 100, 3, 32, "fbx"),
        ("xxterzixjqrghqyeketqeynekvqhc", 15, 94, 4, 16, "nekv"),
    ],
)
def test_subStrHash(
    solution: Solution, s: str, power: int, modulo: int, k: int, hashValue: int, expected_substr: str
) -> None:
    assert solution.subStrHash(s, power, modulo, k, hashValue) == expected_substr
