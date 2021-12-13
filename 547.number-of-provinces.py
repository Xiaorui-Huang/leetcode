#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#
# https://leetcode.com/problems/number-of-provinces/description/
#
# algorithms
# Medium (62.32%)
# Likes:    4241
# Dislikes: 215
# Total Accepted:    376.9K
# Total Submissions: 604.9K
# Testcase Example:  '[[1,1,0],[1,1,0],[0,0,1]]'
#
# There are n cities. Some of them are connected, while some are not. If city a
# is connected directly with city b, and city b is connected directly with city
# c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other
# cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the
# i^th city and the j^th city are directly connected, and isConnected[i][j] = 0
# otherwise.
#
# Return the total number of provinces.
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
#
#
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
#
#
#

# @lc code=start
from typing import List
from enum import Enum

approaches = Enum("approaches", "DFS BFS")

APPROACH = approaches.BFS
APPROACH = approaches.DFS
import queue


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        count = 0

        if APPROACH == approaches.BFS:
            q = queue.Queue()
            # BFS loop every node and search
            for i in range(n):
                if not visited[i]:
                    q.put(i)

                    while not q.empty():
                        cur = q.get()
                        visited[cur] = 1
                        for j in range(n):
                            if isConnected[cur][j] and not visited[j]:
                                q.put(j)

                    count += 1
        elif APPROACH == approaches.DFS:

            def dfs_util(node, visited, adj_mat):
                visited[node] = 1
                for i in range(n):
                    if adj_mat[node][i] and not visited[i]:
                        dfs_util(i, visited, adj_mat)

            for i in range(n):
                if not visited[i]:
                    count += 1
                    dfs_util(i, visited, isConnected)

        return count


s = Solution()
a = s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(a)


# @lc code=end
