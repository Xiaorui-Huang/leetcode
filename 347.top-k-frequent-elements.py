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
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        order = sorted(zip(dic.values(), dic.keys()), reverse=True)
        _, ret = zip(*order)
        return list(ret)[:k]

# ===================== official provided solution ===============
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
#         # O(1) time 
#         if k == len(nums):
#             return nums
        
#         # 1. build hash map : character and how often it appears
#         # O(N) time
#         count = Counter(nums)   
#         # 2-3. build heap of top k frequent elements and
#         # convert it into an output array
#         # O(N log k) time
#         return heapq.nlargest(k, count.keys(), key=count.get) 
                
# @lc code=end

sol = Solution()
a = sol.topKFrequent([1,1,1,2,2,3], 2)
print(a)



