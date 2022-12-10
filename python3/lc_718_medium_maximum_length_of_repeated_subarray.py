#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (51.60%)
# Likes:    5844
# Dislikes: 148
# Total Accepted:    249.4K
# Total Submissions: 484.7K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
#
#
# Example 1:
#
#
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
#
#
# Example 2:
#
#
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
#
#
#
# Constraints:
#
#
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
#
#
#

# @lc code=start

# https://codeforces.com/blog/entry/52697 - just using a single hash, this is rolling hash and a hash function after all
from typing import Iterator


P = 137
MOD = 10**9 + 9


def hash_list(nums: list[int], power: int, modulo: int) -> int:
    """Calculate the hash for the given input

    ONLY used for naive verification or brute force approach
    """
    return sum(nums[i] * pow(power, i, modulo) for i in range(len(nums))) % modulo


def has_matched_subarray_hash(length: int, nums1: list[int], nums2: list[int]) -> bool:
    """Determine if a subarray of length exists in both nums1 and nums2

    Precondition:
        length <= len(nums1) <= len(nums2)

    Args:
        length (int): length of the subarray to search
        nums1 (list[int]): array 1
        nums2 (list[int]): array 2

    Returns:
        bool: if a subarray of length exists in both nums1 and nums2
    """
    # given substring length calculate the hash using rolling hash
    # store all hashes of current length for nums1 in set
    # calculate the rolling hash from nums2 and match with set
    p_k_mod = pow(P, length, MOD)

    def roll_hash(nums: list[int], length: int) -> Iterator[tuple[int, int]]:
        """Return a Iterator of hashes for subarray of size length

        Args:
            nums (list[int]): the array to calculate hashes for subarray from
            length (int): the length of the sub array

        Yields:
            Iterator[int]: iterator of subarray hashes
        """
        rolling_hash = 0
        for i in range(len(nums) - 1, -1, -1):
            rolling_hash = (rolling_hash * P + nums[i]) % MOD
            if i + length < len(nums):
                rolling_hash = (rolling_hash - (p_k_mod * nums[i + length])) % MOD
            if i + length <= len(nums):
                yield (rolling_hash, i)

    # construction
    hashes: dict[int, int] = {}
    for k, v in roll_hash(nums1, length):
        hashes[k] = v

    # verification
    for rolling_hash, i in roll_hash(nums2, length):
        if rolling_hash in hashes:
            j = hashes[rolling_hash]
            if nums1[j : j + length] == nums2[i : i + length]:
                return True

    return False


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        # ensure nums1 is shorter
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # binary search on length...
        low, high = 1, len(nums1) + 1
        while low < high:
            mid = (low + high) // 2
            if has_matched_subarray_hash(mid, nums1, nums2):
                low = mid + 1
            else:
                high = mid
        return low - 1


# @lc code=end
def main() -> None:
    sol = Solution()
    arr1 = [0, 0, 0, 0, 1]
    arr2 = [1, 0, 0, 0, 0]
    # arr1 = [1, 2, 3, 2, 0, 0]
    # arr2 = [3, 2, 1, 4, 7, 5]
    # print(hash_list([3, 2, 1], P, MOD))
    # ans = has_matched_subarray_hash(3, arr1, arr2)
    ans = sol.findLength(arr1, arr2)
    print(ans)


if __name__ == "__main__":
    main()
