#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (44.70%)
# Likes:    7795
# Dislikes: 311
# Total Accepted:    737.4K
# Total Submissions: 1.6M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
#
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
#
#
# Return true if you can finish all courses. Otherwise, return false.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
#
#
# Example 2:
#
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 10^5
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
#
#
#
# @lc code=start
from enum import Enum
from typing import List

approaches = Enum("app", "DFS OPT_DFS")
APPROACH = approaches.OPT_DFS


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the adjacency matrix
        if APPROACH == approaches.DFS:
            return self.canFinish_DFS(numCourses, prerequisites)
        elif APPROACH == approaches.OPT_DFS:
            return self.canFinish_OPT_DFS(numCourses, prerequisites)

    # lc discussion sol src: https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation/60058
    def canFinish_OPT_DFS(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs_util(i):
            # if ith node is marked as being visited, then a cycle is found
            if visited[i] == -1:
                return False
            # if it is done visted, then do not visit again
            if visited[i] == 1:
                return True
            # mark as being visited
            visited[i] = -1
            # visit all the neighbours
            for j in graph[i]:
                if not dfs_util(j):
                    return False
            # after visit all the neighbours, mark it as done visited
            visited[i] = 1
            return True

        for i in range(numCourses):
            if not dfs_util(i):
                return False
        return True

    def canFinish_DFS(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = set()
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            second, first = pre
            if first == second:
                return False
            adj[first].append(second)
            courses.add(first)
            courses.add(second)

        def dfs_util(cur: int, visited: List[bool]):
            for node in adj[cur]:
                if not visited[node]:
                    # we mark the nodes later, as we only want the course to be
                    # required as a prereq to be avoided
                    visited[node] = True
                    dfs_util(node, visited)
            # should not have visited itself
            # i.e. there is not directed cycle starting at cur
            return not visited[cur]

        for course in courses:
            visited = [False] * numCourses
            if not dfs_util(course, visited):
                return False
        return True


# @lc code=end


def main():
    sol = Solution()
    a = sol.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]])
    print(a)

    a = sol.canFinish(2, [[1, 0]])
    print(a)

    a = sol.canFinish(2, [[1, 0], [0, 1]])
    print(a)


if __name__ == "__main__":
    main()
