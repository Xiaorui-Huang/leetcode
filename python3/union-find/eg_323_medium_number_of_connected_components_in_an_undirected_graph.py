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
class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        if xset == yset:
            return
        if self.rank[xset] > self.rank[yset]:
            self.parent[yset] = self.parent[xset]
        elif self.rank[xset] < self.rank[yset]:
            self.parent[xset] = self.parent[yset]
        else:
            self.parent[xset] = self.parent[yset]
            self.rank[yset] += 1


class Solution:
    def countComponents(self, n: int, edges: list[tuple[int, int]]) -> int:
        ds = DSU(n)
        for edge in edges:
            ds.union(*edge)

        parent = set()
        for i in range(n):
            parent.add(ds.find(i))
        return len(parent)


# @lc code=end
