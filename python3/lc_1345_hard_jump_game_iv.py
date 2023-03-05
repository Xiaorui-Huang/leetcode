#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#
# https://leetcode.com/problems/jump-game-iv/description/
#
# algorithms
# Hard (43.87%)
# Likes:    3132
# Dislikes: 108
# Total Accepted:    114.6K
# Total Submissions: 247K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# Given an array of integers arr, you are initially positioned at the first
# index of the array.
#
# In one step you can jump from index i to index:
#
#
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
#
#
# Return the minimum number of steps to reach the last index of the array.
#
# Notice that you can not jump outside of the array at any time.
#
#
# Example 1:
#
#
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that
# index 9 is the last index of the array.
#
#
# Example 2:
#
#
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.
#
#
# Example 3:
#
#
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last
# index of the array.
#
#
#
# Constraints:
#
#
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
#
#
#

# @lc code=start

from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        portals = defaultdict(list)
        # original implementation for tracking -> no need we can use a set. since bfs always gives shortest path here
        # will use a set for rust implementation
        step_tracker = [n] * n  # can always get to the last index in n - 1 steps, so set upper bound to be n
        step_tracker[0] = 0

        # key: arr values; value: index to connected portals
        for i, key in enumerate(arr):
            portals[key].append(i)

        q: deque[tuple[int, int]] = deque([(0, 0)])
        while q:
            index, steps = q.popleft()
            if index == n - 1:  # a better solution is to just use set to track visited and not use step tracker
                return steps
            portal_key = arr[index]
            if index - 1 >= 0 and steps + 1 < step_tracker[index - 1]:
                q.append((index - 1, steps + 1))
                step_tracker[index - 1] = steps + 1

            for portal_index in portals[portal_key]:
                if steps + 1 < step_tracker[portal_index]:
                    q.append((portal_index, steps + 1))
                    step_tracker[portal_index] = steps + 1
            portals[portal_key].clear()  # only use the portals once

            if index + 1 < n and steps + 1 < step_tracker[index + 1]:
                q.append((index + 1, steps + 1))
                step_tracker[index + 1] = steps + 1

        return step_tracker[-1]


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.minJumps([100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
    # ans = sol.minJumps([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8])
    print(ans)


if __name__ == "__main__":
    main()
