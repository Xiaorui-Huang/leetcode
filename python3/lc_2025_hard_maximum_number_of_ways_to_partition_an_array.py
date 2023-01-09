#
# @lc app=leetcode id=2025 lang=python3
#
# [2025] Maximum Number of Ways to Partition an Array
#
# https://leetcode.com/problems/maximum-number-of-ways-to-partition-an-array/description/
#
# algorithms
# Hard (32.62%)
# Likes:    371
# Dislikes: 38
# Total Accepted:    6.6K
# Total Submissions: 20.3K
# Testcase Example:  '[2,-1,2]\n3'
#
# You are given a 0-indexed integer array nums of length n. The number of ways
# to partition nums is the number of pivot indices that satisfy both
# conditions:
#
#
# 1 <= pivot < n
# nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] +
# ... + nums[n - 1]
#
#
# You are also given an integer k. You can choose to change the value of one
# element of nums to k, or to leave the array unchanged.
#
# Return the maximum possible number of ways to partition nums to satisfy both
# conditions after changing at most one element.
#
#
# Example 1:
#
#
# Input: nums = [2,-1,2], k = 3
# Output: 1
# Explanation: One optimal approach is to change nums[0] to k. The array
# becomes [3,-1,2].
# There is one way to partition the array:
# - For pivot = 2, we have the partition [3,-1 | 2]: 3 + -1 == 2.
#
#
# Example 2:
#
#
# Input: nums = [0,0,0], k = 1
# Output: 2
# Explanation: The optimal approach is to leave the array unchanged.
# There are two ways to partition the array:
# - For pivot = 1, we have the partition [0 | 0,0]: 0 == 0 + 0.
# - For pivot = 2, we have the partition [0,0 | 0]: 0 + 0 == 0.
#
#
# Example 3:
#
#
# Input: nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
# Output: 4
# Explanation: One optimal approach is to change nums[2] to k. The array
# becomes [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14].
# There are four ways to partition the array.
#
#
#
# Constraints:
#
#
# n == nums.length
# 2 <= n <= 10^5
# -10^5 <= k, nums[i] <= 10^5
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def waysToPartition(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        for i, num in enumerate(nums):
            prefix_sum[i] = prefix_sum[i - 1] + num

        total = prefix_sum.pop()  # skip the last pivot

        count = 0

        # without changing any elements
        for cur_sum in prefix_sum:
            if cur_sum == (total - cur_sum):  # <=> to cur_sum == total / 2
                count += 1

        # for performance/complexity reasons we only store the original prefix counts (before adjusting for k)
        prefix_counter: Counter[int | float] = Counter()
        suffix_counter: Counter[int | float] = Counter(prefix_sum)

        # if we change most most one number to k
        #   the trick is to adjust the goal instead of modifying the suffix key and we automatically have the counts by referring to the original counts
        prefix_sum.append(total)  # add back the total since to check if replacing it will have better results
        for num, cur_sum in zip(nums, prefix_sum):
            goal = (total + k - num) / 2  # if a prefix sum is half of the total it's a valid pivot
            adjusted_goal = goal - k + num  # adjust if to before prefix
            count_if_replaced = prefix_counter.get(goal, 0) + suffix_counter.get(adjusted_goal, 0)
            count = max(count, count_if_replaced)

            # move the counts across
            suffix_counter.subtract([cur_sum])
            prefix_counter.update([cur_sum])

        return count


# @lc code=end
