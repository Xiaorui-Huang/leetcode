from typing import Optional
import pytest
from lc_297_hard_serialize_and_deserialize_binary_tree import Codec
from utils.binary_tree import TreeNode, build_bt, null


# fixtures
@pytest.fixture
def codec() -> Codec:
    return Codec()


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        (build_bt([1, 2, 3, null, null, 4, 5]), "1 2 3 None None 4 5"),
        (build_bt([]), ""),
    ],
)
def test_serialize(codec: Codec, root: Optional[TreeNode], expected: str) -> None:
    assert codec.serialize(root) == expected


@pytest.mark.parametrize(
    "data, expected",
    [
        # testcases
        ("1 2 3 None None 4 5", build_bt([1, 2, 3, null, null, 4, 5])),
        ("", None),
    ],
)
def test_deserialize(codec: Codec, data: str, expected: Optional[TreeNode]) -> None:
    assert codec.deserialize(data) == expected


@pytest.mark.parametrize(
    "root, expected",
    [
        # testcases
        (build_bt([1, 2, 3, null, null, 4, 5]), build_bt([1, 2, 3, null, null, 4, 5])),
        (None, None),
    ],
)
def test_encode_decode(codec: Codec, root: Optional[TreeNode], expected: Optional[TreeNode]) -> None:
    assert codec.deserialize(codec.serialize(root)) == expected
