#
# @lc app=leetcode id=1443 lang=python3
#
# [1443] Minimum Time to Collect All Apples in a Tree
#
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/
#
# algorithms
# Medium (56.06%)
# Likes:    1204
# Dislikes: 95
# Total Accepted:    33.4K
# Total Submissions: 59.4K
# Testcase Example:  '7\n' + '[[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]\n' + '[false,false,true,false,true,true,false]'
#
# Given an undirected tree consisting of n vertices numbered from 0 to n-1,
# which has some apples in their vertices. You spend 1 second to walk over one
# edge of the tree. Return the minimum time in seconds you have to spend to
# collect all apples in the tree, starting at vertex 0 and coming back to this
# vertex.
#
# The edges of the undirected tree are given in the array edges, where edges[i]
# = [ai, bi] means that exists an edge connecting the vertices ai and bi.
# Additionally, there is a boolean array hasApple, where hasApple[i] = true
# means that vertex i has an apple; otherwise, it does not have any apple.
#
#
# Example 1:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,true,true,false]
# Output: 8
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.
#
#
# Example 2:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,true,false,false,true,false]
# Output: 6
# Explanation: The figure above represents the given tree where red vertices
# have an apple. One optimal path to collect all apples is shown by the green
# arrows.
#
#
# Example 3:
#
#
# Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple =
# [false,false,false,false,false,false,false]
# Output: 0
#
#
#
# Constraints:
#
#
# 1 <= n <= 10^5
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai < bi <= n - 1
# fromi < toi
# hasApple.length == n
#
#
#

# @lc code=start
# using python 3.10 typing syntax
class Solution:
    time = 0

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        # construct graph, list is faster than hashmap/dictionaries
        graph: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, parent: int | None) -> bool:
            """return if there are any apple in the tree rooted at node to collect"""
            has_apple_here: bool = hasApple[node]

            for child in graph[node]:
                # avoid visiting the parent again
                # and only count time if we need to visit this neighbor for apple
                if child != parent and dfs(child, node):
                    # there are apples in tree at child, so this this tree has apple too
                    has_apple_here = True
                    self.time += 2  # it takes 2 sec to get there and come back

            return has_apple_here

        dfs(0, None)
        return self.time


# @lc code=end
