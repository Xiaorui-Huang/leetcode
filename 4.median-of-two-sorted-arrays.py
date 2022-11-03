#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (35.14%)
# Likes:    20256
# Dislikes: 2297
# Total Accepted:    1.6M
# Total Submissions: 4.7M
# Testcase Example:  '[1,3]\n[2]'
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return
# the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
#
# Example 1:
#
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
#
# Example 2:
#
#
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
#
#
# Constraints:
#
#
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6
#
#
#

# @lc code=start
class Solution:
    # binary search
    def findMedianSortedArrays(self, l1: list[int], l2: list[int]) -> float:
        # BOOTSTRAP the lists
        # make len(nums1) <= len(nums2)
        if len(l2) < len(l1):
            l1, l2 = l2, l1

        # get the target size for partition to find median
        total = len(l1) + len(l2)
        target_half_size = total // 2
        is_odd = bool(total % 2)

        low, high = 0, len(l1) - 1
        # (could also use while True, since it guarantees a medium)
        while low <= high:
            partition_index = (low + high) // 2
            # from number of elements to index we subtract 1
            bound_index = target_half_size - (partition_index + 1) - 1

            # to determine if a position is the medium, use
            # l1 : [...a | b ...]
            # l2 : [...c | d ...]
            # b >= c and d >= a -> min(b, d) is the medium (for the odd case)

            l1_left = l1[partition_index]
            l1_right = l1[partition_index + 1] if (partition_index + 1) < len(l1) else float("inf")
            l2_left = l2[bound_index] if bound_index >= 0 else float("-inf")
            l2_right = l2[bound_index + 1] if (bound_index + 1) < len(l2) else float("inf")

            if l1_left <= l2_right and l2_left <= l1_right:
                if is_odd:
                    return min(l1_right, l2_right)
                # is even
                return (max(l1_left, l2_left) + min(l1_right, l2_right)) / 2
            # last value of l1 is too big, need to reduce the size of l1 partition
            elif l1_left > l2_right:
                high = partition_index - 1
            # last value of l2 is too big, need to increase the size of l1 partition
            else:  # (l2_left > l1_right)
                low = partition_index + 1
        print("an error occurred")


# @lc code=end


def main():
    sol = Solution()
    # # 1,1,2,2,3,3   (3.5)   4,5,6,6,7,8
    # arr1 = [1, 2, 3, 4]
    # arr2 = [1, 2, 3, 5, 6, 6, 7, 8]

    # 1,1,2,2,3,3,4, (5), 6,6,7,8,10,11,12

    arr1 = [1, 2, 3, 5]
    arr2 = [1, 2, 3, 4, 6, 6, 7, 8, 10, 11, 12]
    ans = sol.findMedianSortedArrays(arr1, arr2)
    print(ans)


if __name__ == "__main__":
    main()
