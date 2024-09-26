#
# @lc app=leetcode id=1539 lang=python3
#
# [1539] Kth Missing Positive Number
#
# https://leetcode.com/problems/kth-missing-positive-number/description/
#
# algorithms
# Easy (56.09%)
# Likes:    3638
# Dislikes: 267
# Total Accepted:    216.5K
# Total Submissions: 384.8K
# Testcase Example:  '[2,3,4,7,11]\n5'
#
# Given an array arr of positive integers sorted in a strictly increasing
# order, and an integer k.
#
# Return the k^th positive integer that is missing from this array.
#
#
# Example 1:
#
#
# Input: arr = [2,3,4,7,11], k = 5
# Output: 9
# Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The
# 5^th missing positive integer is 9.
#
#
# Example 2:
#
#
# Input: arr = [1,2,3,4], k = 2
# Output: 6
# Explanation: The missing positive integers are [5,6,7,...]. The 2^nd missing
# positive integer is 6.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 1 <= k <= 1000
# arr[i] < arr[j] for 1 <= i < j <= arr.length
#
#
#
# Follow up:
#
# Could you solve this problem in less than O(n) complexity?
#
#


# @lc code=start
class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        # O(n + k) is the naive solution and can be accepted, BUT
        # O(log n) solution uses the fact that:
        # number of missing at arr[i] == arr[i] - (i + 1) == value at i minus the number of item in front of index i
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] - (mid + 1) < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k


# @lc code=end
