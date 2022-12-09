#
# @lc app=leetcode id=323 lang=python3
#
# [323] Number of Connected Components in an Undirected Graph
#
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
#
# algorithms
# Medium (62.13%)
# Likes:    2320
# Dislikes: 80
# Total Accepted:    310.1K
# Total Submissions: 499.1K
# Testcase Example:  '5\n[[0,1],[1,2],[3,4]]'
#
# You have a graph of n nodes. You are given an integer n and an array edges
# where edges[i] = [ai, bi] indicates that there is an edge between ai and bi
# in the graph.
#
# Return the number of connected components in the graph.
#
#
# Example 1:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
#
#
# Example 2:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
#
#
#
# Constraints:
#
#
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.
#
#
#

# @lc code=start
# TODO: implement with DSU
class Solution:
    def countComponents(self, n: int, edges: list[tuple[int, int]]) -> int:
        adjacency_list: dict[int, list[int]] = {}
        for a, b in edges:
            adjacency_list.setdefault(a, []).append(b)
            adjacency_list.setdefault(b, []).append(a)

        seen: set[int] = set()

        def dfs(node: int) -> None:
            stack: list[int] = [node]
            while stack:
                cur_node = stack.pop()
                seen.add(cur_node)
                for neighbor in adjacency_list.get(cur_node, []):
                    if neighbor not in seen:
                        stack.append(neighbor)

        connected = 0
        for node in range(n):
            if node not in seen:
                dfs(node)
                connected += 1

        return connected


# @lc code=end
