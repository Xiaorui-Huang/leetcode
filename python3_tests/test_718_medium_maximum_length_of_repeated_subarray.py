import pytest
from lc_718_medium_maximum_length_of_repeated_subarray import Solution, has_matched_subarray_hash

# fixtures
@pytest.fixture
def solution() -> Solution:
    return Solution()


@pytest.mark.parametrize(
    "length, nums1, nums2, expected",
    [
        (3, [1, 2, 3], [1, 2, 3], True),
        (2, [1, 2], [1, 2, 3], True),
        (4, [1, 3, 6, 8, 1, 9, 2], [23, 2, 3, 422, 78, 6, 8, 1, 9, 5, 4, 3, 2, 445, 33], True),
        (5, [23, 2, 3, 422, 78, 6, 8, 1, 9, 5, 4, 3, 2, 445, 33], [1, 3, 6, 8, 1, 9, 2], False),
        (4, [0, 0, 0, 0, 1], [1, 0, 0, 0, 0], True),
        (2, [1, 2, 3, 1, 2, 3, 4, 2, 2, 3, 4, 5], [3, 2, 1, 3, 2, 1, 3, 2, 1, 4, 4, 2, 1], True),  # 4, 2
    ],
)
def test_hash_matched_subarray_hash(length: int, nums1: list[int], nums2: list[int], expected: bool) -> None:
    assert has_matched_subarray_hash(length, nums1, nums2) == expected


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 3], [1, 2, 3], 3),
        ([1, 2], [1, 2, 3], 2),
        ([1, 3, 6, 8, 1, 9, 2], [23, 2, 3, 422, 78, 6, 8, 1, 9, 5, 4, 3, 2, 445, 33], 4),
        ([1, 2, 3, 1, 2, 3, 4, 2, 2, 3, 4, 5], [3, 2, 1, 3, 2, 1, 3, 2, 1, 4, 4, 2, 1], 2),
        ([1, 2, 3, 4], [5, 6, 7, 8], 0),
        ([0, 0, 0, 0, 1], [1, 0, 0, 0, 0], 4),
    ],
)
def test_findLength(solution: Solution, nums1: list[int], nums2: list[int], expected: int) -> None:
    assert solution.findLength(nums1, nums2) == expected
