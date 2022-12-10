#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (48.65%)
# Likes:    9151
# Dislikes: 402
# Total Accepted:    651.9K
# Total Submissions: 1.3M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
#
# You must write an algorithm that runs in O(n) time.
#
#
# Example 1:
#
#
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
# Example 2:
#
#
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "HASH DISJOINT_SET")
APPR = appr.DISJOINT_SET


class Solution:
    def __init__(self) -> None:
        if APPR == appr.HASH:
            self.longestConsecutive = self.longestConsecutive_hash_implicit_disjoint_set
        elif APPR == appr.DISJOINT_SET:
            self.longestConsecutive = self.longestConsecutive_union_find

    def longestConsecutive_union_find(self, nums: list[int]) -> int:
        dset = DisjointSet()
        nodes = {}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num + 1 in nodes:
                    size = dset.union(node, nodes[num + 1])
                if num - 1 in nodes:
                    size = dset.union(node, nodes[num - 1])
                max_size = max(max_size, size)

        return max_size

    def longestConsecutive_hash_implicit_disjoint_set(self, nums: list[int]) -> int:
        hashset = set(nums)
        longest_streak = 0

        for num in hashset:
            # check if num belong to a streak
            # only proceed to check for streak if it's not already part of a streak
            if (num - 1) not in hashset:
                # count the current streak from num (i.e. a starting streak of 1)
                cur_streak = 1
                while (num + cur_streak) in hashset:
                    cur_streak += 1
                longest_streak = max(longest_streak, cur_streak)

        return longest_streak


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.parent = self
        self.size = 1


class DisjointSet:
    def find(self, node: Node) -> Node:
        if node.parent != node:
            node.parent = self.find(node.parent)
        return node.parent

    def union(self, node1: Node, node2: Node) -> int:
        parent_1 = self.find(node1)
        parent_2 = self.find(node2)
        if parent_1 != parent_2:
            parent_2.parent = parent_1
            parent_1.size += parent_2.size
        return parent_1.size


# @lc code=end


def main() -> None:
    sol = Solution()
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    ans = sol.longestConsecutive(nums)
    print(ans)


if __name__ == "__main__":
    main()
