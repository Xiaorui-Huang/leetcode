#
# @lc app=leetcode id=1129 lang=python3
#
# [1129] Shortest Path with Alternating Colors
#
# https://leetcode.com/problems/shortest-path-with-alternating-colors/description/
#
# algorithms
# Medium (42.95%)
# Likes:    1810
# Dislikes: 90
# Total Accepted:    51.1K
# Total Submissions: 117.6K
# Testcase Example:  '3\n[[0,1],[1,2]]\n[]'
#
# You are given an integer n, the number of nodes in a directed graph where the
# nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph,
# and there could be self-edges and parallel edges.
#
# You are given two arrays redEdges and blueEdges where:
#
#
# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node
# ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from
# node uj to node vj in the graph.
#
#
# Return an array answer of length n, where each answer[x] is the length of the
# shortest path from node 0 to node x such that the edge colors alternate along
# the path, or -1 if such a path does not exist.
#
#
# Example 1:
#
#
# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
#
#
# Example 2:
#
#
# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n
#
#
#

# @lc code=start
from collections import deque
from typing import Annotated


RED = 1
BLUE = 0
NO_COLOR = None
NOT_FOUND = -1


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        shortest_color_path = [NOT_FOUND] * n
        graph: list[list[tuple[int, int]]] = [[] for _ in range(n)]

        visited: list[Annotated[list[bool], 2]] = [[False, False] for _ in range(n)]

        for a, b in redEdges:
            graph[a].append((b, RED))

        for a, b in blueEdges:
            graph[a].append((b, BLUE))

        # node, distance and prev_color
        q: deque[tuple[int, int, int | None]] = deque([])
        q.append((0, 0, NO_COLOR))
        visited[0] = [True, True]
        shortest_color_path[0] = 0

        while q:
            node, distance, prev_color = q.popleft()
            for neighbor, color in graph[node]:
                if not visited[neighbor][color] and color != prev_color:
                    visited[neighbor][color] = True
                    q.append((neighbor, distance + 1, color))
                    if shortest_color_path[neighbor] == NOT_FOUND:
                        shortest_color_path[neighbor] = 1 + distance

        return shortest_color_path


# @lc code=end
