#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (45.34%)
# Likes:    955
# Dislikes: 109
# Total Accepted:    57.6K
# Total Submissions: 127.3K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array of integers arr, return true if we can partition the array
# into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i + 1 < j with
# (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1]
# == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
#
#
# Example 1:
#
#
# Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#
#
# Example 2:
#
#
# Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
#
#
# Example 3:
#
#
# Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
#
#
#
# Constraints:
#
#
# 3 <= arr.length <= 5 * 10^4
# -10^4 <= arr[i] <= 10^4
#
#
#


# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False

        part_sum, cur_sum, part = total // 3, 0, 0
        for num in arr:
            cur_sum += num
            if cur_sum == part_sum:
                if part == 2:
                    return True
                cur_sum = 0
                part += 1
        return False
        # Just as a side comment...
        # The solution doesn't require the final return False in Python, since
        # no return is equivalent to return None, i.e. False
        # Kinda dumb tho...


# @lc code=end
