#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#
# https://leetcode.com/problems/lfu-cache/description/
#
# algorithms
# Hard (40.47%)
# Likes:    4338
# Dislikes: 268
# Total Accepted:    188.7K
# Total Submissions: 455.7K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' + '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for a Least Frequently Used (LFU)
# cache.
#
# Implement the LFUCache class:
#
#
# LFUCache(int capacity) Initializes the object with the capacity of the data
# structure.
# int get(int key) Gets the value of the key if the key exists in the cache.
# Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or
# inserts the key if not already present. When the cache reaches its capacity,
# it should invalidate and remove the least frequently used key before
# inserting a new item. For this problem, when there is a tie (i.e., two or
# more keys with the same frequency), the least recently used key would be
# invalidated.
#
#
# To determine the least frequently used key, a use counter is maintained for
# each key in the cache. The key with the smallest use counter is the least
# frequently used key.
#
# When a key is first inserted into the cache, its use counter is set to 1 (due
# to the put operation). The use counter for a key in the cache is incremented
# either a get or put operation is called on it.
#
# The functions get and put must each run in O(1) average time complexity.
#
#
# Example 1:
#
#
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element
# is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
# ⁠                // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest,
# invalidate 2.
# // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
# ⁠                // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate
# 1.
# ⁠                // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
# ⁠                // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
# ⁠                // cache=[4,3], cnt(4)=2, cnt(3)=3
#
#
#
# Constraints:
#
#
# 0 <= capacity <= 10^4
# 0 <= key <= 10^5
# 0 <= value <= 10^9
# At most 2 * 10^5 calls will be made to get and put.
#
#
#
#
#

# @lc code=start
from collections import defaultdict
from typing import Annotated


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.min_freq = 0
        # key: frequency - value
        self.cache: dict[int, Annotated[list[int], 2]] = {}
        # frequency: Ordered set of keys (implemented with dict)
        self.frequencies: dict[int, dict[int, None]] = defaultdict(dict)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # increment frequency
        frequency, value = self.cache[key]
        self.cache[key][0] += 1

        # move the key from the current frequency group to the next
        self.frequencies[frequency].pop(key)
        self.frequencies[frequency + 1][key] = None

        # if this is the last item in the frequency group and frequency is min_freq
        # then increment min_freq
        if len(self.frequencies[frequency]) == 0 and self.min_freq == frequency:
            self.min_freq += 1

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return

        # if value is in cache, update the value and frequency of key (using get method)
        if key in self.cache:
            self.cache[key][1] = value
            self.get(key)  # updates the frequency using get
            return

        # evict when at max capacity
        if len(self.cache) == self.capacity:
            min_freq_group = self.frequencies[self.min_freq]
            ordered_set_iter = iter(min_freq_group)
            # since dict are ordered, we pop the first item to find the least recently used key
            evict_target = next(ordered_set_iter)
            # evict the target from both cache and frequencies
            min_freq_group.pop(evict_target)
            self.cache.pop(evict_target)

        # inserting new items
        self.min_freq = 1
        self.cache[key] = [1, value]
        self.frequencies[1][key] = None


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end


def main() -> None:
    # cache = LFUCache(2)
    # cache.put(1, 1)
    # cache.put(2, 2)
    # print(cache.get(1))
    # cache.put(3, 3)
    # print(cache.get(2))
    # print(cache.get(3))
    # cache.put(4, 4)
    # print(cache.get(1))
    # print(cache.get(3))
    # print(cache.get(4))

    c = LFUCache(2)
    print(c.get(2))
    c.put(2, 6)
    print(c.get(1))
    c.put(1, 5)
    c.put(1, 2)
    print(c.get(1))
    print(c.get(2))


if __name__ == "__main__":
    main()
