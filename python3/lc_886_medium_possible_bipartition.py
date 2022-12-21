#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (48.50%)
# Likes:    2919
# Dislikes: 65
# Total Accepted:    130.8K
# Total Submissions: 269K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# We want to split a group of n people (labeled from 1 to n) into two groups of
# any size. Each person may dislike some other people, and they should not go
# into the same group.
#
# Given the integer n and the array dislikes where dislikes[i] = [ai, bi]
# indicates that the person labeled ai does not like the person labeled bi,
# return true if it is possible to split everyone into two groups in this
# way.
#
#
# Example 1:
#
#
# Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4] and group2 [2,3].
#
#
# Example 2:
#
#
# Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
#
# Example 3:
#
#
# Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2000
# 0 <= dislikes.length <= 10^4
# dislikes[i].length == 2
# 1 <= dislikes[i][j] <= n
# ai < bi
# All the pairs of dislikes are unique.
#
#
#

# @lc code=start
class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        graph: dict[int, list[int]] = {}
        for a, b in dislikes:
            graph.setdefault(a, []).append(b)
            graph.setdefault(b, []).append(a)

        red: set[int] = set()
        blue: set[int] = set()
        seen: set[int] = set()
        for node in range(1, n + 1):
            # skip components that are visited already
            if node in seen:
                continue

            red.add(node)
            stack: list[tuple[int, set[int]]] = [(node, red)]
            while stack:
                cur, color = stack.pop()
                composite = blue if color is red else red
                seen.add(cur)
                for neighbor in graph.get(cur, ()):
                    # if neighbor has the same color as parent then it's not 2 colorable
                    if neighbor in color:
                        return False
                    if neighbor in seen:
                        continue
                    composite.add(neighbor)
                    stack.append((neighbor, composite))
        return True


# @lc code=end
