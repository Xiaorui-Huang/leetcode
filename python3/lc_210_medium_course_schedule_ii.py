#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (45.12%)
# Likes:    5276
# Dislikes: 203
# Total Accepted:    516.4K
# Total Submissions: 1.1M
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
#
#
# Example 1:
#
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
#
#
# Example 2:
#
#
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
#
#
# Example 3:
#
#
# Input: numCourses = 1, prerequisites = []
# Output: [0]
#
#
#
# Constraints:
#
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
#
#
#
from enum import Enum

approaches = Enum("app", "DFS")
APPROACH = approaches.DFS

# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if APPROACH == approaches.DFS:
            return self.findOrder_DFS(numCourses, prerequisites)
        return []  # never reached

    def findOrder_DFS(self, n: int, prereq: list[list[int]]) -> list[int]:
        # refer to the lc 207. for decision problem implementation
        graph: list[list[int]] = [[] for _ in range(n)]
        visited = [0] * n

        for post, pre in prereq:
            graph[pre].append(post)

        def dfs(i: int) -> bool:
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True

            visited[i] = -1
            for node in graph[i]:
                if not dfs(node):
                    return False
            visited[i] = 1
            return True

        for course in range(n):
            if not dfs(course):
                return []
        order = []
        picked = [0] * n
        for pre in range(n):
            if not picked[pre]:
                order.append(pre)
                picked[pre] = 1
            for post in graph[pre]:
                if not picked[post]:
                    order.append(post)
                    picked[post] = 1

        # collecting all the left-over courses
        for course in range(n):
            if not picked[course]:
                order.append(course)

        return order


# @lc code=end


def main() -> None:
    sol = Solution()
    a = sol.findOrder(5, [[1, 4], [2, 4], [3, 1], [3, 2]])
    print(a)


if __name__ == "__main__":
    main()
