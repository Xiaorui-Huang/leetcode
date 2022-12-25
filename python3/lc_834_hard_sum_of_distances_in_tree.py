#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#
# https://leetcode.com/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (54.25%)
# Likes:    4236
# Dislikes: 100
# Total Accepted:    76K
# Total Submissions: 128.4K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# There is an undirected connected tree with n nodes labeled from 0 to n - 1
# and n - 1 edges.
#
# You are given the integer n and the array edges where edges[i] = [ai, bi]
# indicates that there is an edge between nodes ai and bi in the tree.
#
# Return an array answer of length n where answer[i] is the sum of the
# distances between the i^th node in the tree and all other nodes.
#
#
# Example 1:
#
#
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
#
#
# Example 2:
#
#
# Input: n = 1, edges = []
# Output: [0]
#
#
# Example 3:
#
#
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
#
#
#
# Constraints:
#
#
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
#
#
#

# @lc code=start
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        # sum and count strategy
        graph: list[list[int]] = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # first get the count for all subtree and the dist-sum of the root (then use this info to calculate each node's dist-sum)
        counts: list[int] = [1] * n
        ans: list[int] = [0] * n

        def dfs_count_and_root_dist(node: int, parent: int | None) -> None:
            """traverse the tree and set the total distance number count of the tree at root and the node count for each node

            i.e. After this ans[0] will be the correct answer and count[i] for all i will be set

            Args:
                node (int): tree rooted at node
                parent (int | None): parent of this node, or None if node is root
            """
            for child in graph[node]:
                if child != parent:
                    dfs_count_and_root_dist(child, node)
                    ans[node] += ans[child] + counts[child]
                    counts[node] += counts[child]

        def dfs_infer_dist(node: int, parent: int | None) -> None:
            """from the dist sum of root at ans[0] ans counts infer ans[i] for all i

            Intuition:
                a child node's dist sum compare to it's parent is
                    1. counts[child] less than ans[parent], since child is 1 closer to counts[child] number of nodes
                    2. (n - counts[child]) more than ans[parent], since child is 1 further away from (n - counts[child]) number of nodes

            Args:
                node (int): the node to calculate ans[node] for
                parent (int | None): parent of node, or None if node is root
            """
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - counts[child] + (n - counts[child])
                    dfs_infer_dist(child, node)

        dfs_count_and_root_dist(0, None)
        dfs_infer_dist(0, None)
        return ans


# @lc code=end
def main() -> None:
    sol = Solution()
    ans = sol.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]])
    print(ans)


if __name__ == "__main__":
    main()
