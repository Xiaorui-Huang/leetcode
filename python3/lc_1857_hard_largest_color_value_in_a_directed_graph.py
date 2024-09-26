#
# @lc app=leetcode id=1857 lang=python3
#
# [1857] Largest Color Value in a Directed Graph
#
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
#
# algorithms
# Hard (40.77%)
# Likes:    723
# Dislikes: 22
# Total Accepted:    16.6K
# Total Submissions: 39.8K
# Testcase Example:  '"abaca"\n[[0,1],[0,2],[2,3],[3,4]]'
#
# There is a directed graph of n colored nodes and m edges. The nodes are
# numbered from 0 to n - 1.
#
# You are given a string colors where colors[i] is a lowercase English letter
# representing the color of the i^th node in this graph (0-indexed). You are
# also given a 2D array edges where edges[j] = [aj, bj] indicates that there is
# a directed edge from node aj to node bj.
#
# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk
# such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The
# color value of the path is the number of nodes that are colored the most
# frequently occurring color along that path.
#
# Return the largest color value of any valid path in the given graph, or -1 if
# the graph contains a cycle.
#
#
# Example 1:
#
#
#
#
# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a"
# (red in the above image).
#
#
# Example 2:
#
#
#
#
# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
#
#
#
# Constraints:
#
#
# n == colors.length
# m == edges.length
# 1 <= n <= 10^5
# 0 <= m <= 10^5
# colors consists of lowercase English letters.
# 0 <= aj, bj < n
#
#


# @lc code=start
class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        graph: list[list[int]] = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)

        count = [([0] * 26) for _ in range(n)]
        seen = [False] * n
        in_stack = [False] * n

        def dfs(node: int) -> int | float:
            if in_stack[node]:
                return float("inf")

            if seen[node]:
                return count[node][ord(colors[node]) - ord("a")]

            seen[node] = True
            in_stack[node] = True
            for neighbor in graph[node]:
                if dfs(neighbor) == float("inf"):
                    return float("inf")
                for i in range(26):
                    count[node][i] = max(count[node][i], count[neighbor][i])

            in_stack[node] = False
            count[node][ord(colors[node]) - ord("a")] += 1
            return count[node][ord(colors[node]) - ord("a")]

        max_color_val: int | float = 0
        for i in range(n):
            max_color_val = max(max_color_val, dfs(i))
        return -1 if max_color_val == float("inf") else int(max_color_val)


# @lc code=end


def main() -> None:
    sol = Solution()
    ans = sol.largestPathValue(
        "hhqhuqhqff",
        [
            [0, 1],
            [0, 2],
            [2, 3],
            [3, 4],
            [3, 5],
            [5, 6],
            [2, 7],
            [6, 7],
            [7, 8],
            [3, 8],
            [5, 8],
            [8, 9],
            [3, 9],
            [6, 9],
        ],
    )
    print(ans)


if __name__ == "__main__":
    main()
