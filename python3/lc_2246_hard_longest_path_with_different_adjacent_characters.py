#
# @lc app=leetcode id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/
#
# algorithms
# Hard (45.21%)
# Likes:    898
# Dislikes: 22
# Total Accepted:    21.6K
# Total Submissions: 44.1K
# Testcase Example:  '[-1,0,0,1,1,2]\n"abacbe"'
#
# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
# represented by a 0-indexed array parent of size n, where parent[i] is the
# parent of node i. Since node 0 is the root, parent[0] == -1.
#
# You are also given a string s of length n, where s[i] is the character
# assigned to node i.
#
# Return the length of the longest path in the tree such that no pair of
# adjacent nodes on the path have the same character assigned to them.
#
#
# Example 1:
#
#
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters in the tree is the path: 0 -> 1 -> 3. The length of this path is
# 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the
# conditions.
#
#
# Example 2:
#
#
# Input: parent = [-1,0,0,0], s = "aabc"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is
# returned.
#
#
#
# Constraints:
#
#
# n == parent.length == s.length
# 1 <= n <= 10^5
# 0 <= parent[i] <= n - 1 for all i >= 1
# parent[0] == -1
# parent represents a valid tree.
# s consists of only lowercase English letters.
#
#
#


# @lc code=start
class Solution:
    def longestPath(self, parents: list[int], s: str) -> int:
        graph: list[list[int]] = [[] for _ in range(len(parents) + 1)]  # +1 to get rid of -1 as parent

        # this is a directed graph now
        for i, parent in enumerate(parents):
            graph[parent].append(i)
        graph.pop()  # get rid of -1 as parent

        max_path = 1

        def find_path(node: int) -> int:
            """return longest path starting at node for the subtree, and update the max_path along the way"""
            nonlocal max_path
            if not graph[node]:  # this a leaf
                return 1

            # record the longest 2 child path as it may combine with node to form a path
            longest_path = second_longest_path = 0
            label = s[node]
            for child in graph[node]:
                child_path = find_path(child)  # need to run find_path for every node
                if label == s[child]:  # ensure no repeating characters in path
                    continue
                if child_path >= longest_path:
                    second_longest_path, longest_path = longest_path, child_path
                elif child_path > second_longest_path:
                    second_longest_path = child_path

            # if the max path includes this current node, then update it
            max_path = max(max_path, 1 + longest_path + second_longest_path)

            # only return to the parent the longest path, since path cannot diverge, i.e. a node in the path have 2 edges
            return 1 + longest_path

        find_path(0)
        return max_path


# @lc code=end
