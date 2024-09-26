#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#
# https://leetcode.com/problems/minimize-deviation-in-array/description/
#
# algorithms
# Hard (51.96%)
# Likes:    1821
# Dislikes: 97
# Total Accepted:    49.7K
# Total Submissions: 94.8K
# Testcase Example:  '[1,2,3,4]'
#
# You are given an array nums of n positive integers.
#
# You can perform two types of operations on any element of the array any
# number of times:
#
#
# If the element is even, divide it by 2.
#
#
# For example, if the array is [1,2,3,4], then you can do this operation on the
# last element, and the array will be [1,2,3,2].
#
#
# If the element is odd, multiply it by 2.
#
# For example, if the array is [1,2,3,4], then you can do this operation on the
# first element, and the array will be [2,2,3,4].
#
#
#
#
# The deviation of the array is the maximum difference between any two elements
# in the array.
#
# Return the minimum deviation the array can have after performing some number
# of operations.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
# then the deviation will be 3 - 2 = 1.
#
#
# Example 2:
#
#
# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3],
# then the deviation will be 5 - 2 = 3.
#
#
# Example 3:
#
#
# Input: nums = [2,10,8]
# Output: 3
#
#
#
# Constraints:
#
#
# n == nums.length
# 2 <= n <= 5 * 10^4
# 1 <= nums[i] <= 10^9
#
#
#

import heapq

# TODO: understand this code


# @lc code=start
class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        max_heap: list[int] = []
        min_val = nums[0] if nums[0] % 2 == 0 else 2 * nums[0]
        n = len(nums)

        for num in nums:
            if num % 2 == 1:
                num = 2 * num
            heapq.heappush(max_heap, -num)
            min_val = min(min_val, num)

        min_deviation = -max_heap[0] - min_val

        # loop will end in the next iteration if max_val is odd
        while len(max_heap) == n:
            max_val = -heapq.heappop(max_heap)
            min_deviation = min(min_deviation, max_val - min_val)
            if max_val % 2 == 0:
                min_val = min(min_val, new_val := (max_val // 2))
                heapq.heappush(max_heap, -new_val)

        return min_deviation


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.minimumDeviation([1, 2, 3, 4])
    print(ans)


if __name__ == "__main__":
    main()
