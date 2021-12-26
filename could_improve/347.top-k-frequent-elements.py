#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.91%)
# Likes:    6699
# Dislikes: 315
# Total Accepted:    742K
# Total Submissions: 1.2M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
#
# Constraints:
#
#
# 1 <= nums.length <= 10^5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
#
#
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
#
#
from typing import List

# @lc code=start
from enum import Enum
from collections import Counter
from heapq import nlargest

approaches = Enum("approaches", "SORTED_ZIP COUNTER_QUEUE")
APPROACH = approaches.COUNTER_QUEUE


class Solution:
    if APPROACH == approaches.SORTED_ZIP:

        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            dic = {}
            for num in nums:
                dic[num] = dic.get(num, 0) + 1

            order = sorted(zip(dic.values(), dic.keys()), reverse=True)
            _, ret = zip(*order)
            return list(ret)[:k]

    elif APPROACH == approaches.COUNTER_QUEUE:
        # ===================== official provided solution ===============
        def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # O(1) time
            if k == len(nums):

                return nums

            # 1. build hash map : character and how often it appears
            # O(N) time
            count = Counter(nums)
            # 2-3. build heap of top k frequent elements and
            # convert it into an output array
            # O(N log k) time
            return nlargest(k, count.keys(), key=count.get)


# @lc code=end

sol = Solution()
a = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
print(a)
