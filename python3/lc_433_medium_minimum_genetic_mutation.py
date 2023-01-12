#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (52.11%)
# Likes:    2337
# Dislikes: 251
# Total Accepted:    111.2K
# Total Submissions: 213.3K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from 'A', 'C', 'G', and 'T'.
#
# Suppose we need to investigate a mutation from a gene string startGene to a
# gene string endGene where one mutation is defined as one single character
# changed in the gene string.
#
#
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
#
#
# There is also a gene bank bank that records all the valid gene mutations. A
# gene must be in bank to make it a valid gene string.
#
# Given the two gene strings startGene and endGene and the gene bank bank,
# return the minimum number of mutations needed to mutate from startGene to
# endGene. If there is no such a mutation, return -1.
#
# Note that the starting point is assumed to be valid, so it might not be
# included in the bank.
#
#
# Example 1:
#
#
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1
#
#
# Example 2:
#
#
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank =
# ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2
#
#
#
# Constraints:
#
#
# 0 <= bank.length <= 10
# startGene.length == endGene.length == bank[i].length == 8
# startGene, endGene, and bank[i] consist of only the characters ['A', 'C',
# 'G', 'T'].
#
#
#

# @lc code=start
from collections import deque

# Intuition - From solution

# We can imagine the problem as a graph. Each gene string is a node, and
# mutations are the edges. Two nodes have an edge (are neighbors) if they differ
# by one character. The added constraints are that the characters must be one of
# "ACGT", and each node must be in bank.

# Then, the problem is simplified: what is the shortest path between start and
# end? When a graph problem involves finding a shortest path, BFS should be used
# over DFS. This is because with BFS, all nodes at distance x from start will be
# visited before any node at distance x + 1 will be visited. Once we find the
# target (end), we know that we found it in the shortest number of steps
# possible.


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        visited = set(startGene)
        q: deque[tuple[str, int]] = deque([(startGene, 0)])

        while q:
            node_gene, steps = q.popleft()
            if node_gene == endGene:
                return steps

            for mutation in "ACGT":
                for i in range(8):  # I kinda hate this loop... this doesn't feel like a BFS...😅
                    if (  #          0...(i - 1)      + c +      (i + 1)...
                        neighbor := node_gene[:i] + mutation + node_gene[i + 1 :]  # assignment & condition
                    ) in bank and neighbor not in visited:  # not using set since 0 <= bank.length <= 10
                        visited.add(neighbor)
                        q.append((neighbor, steps + 1))

        return -1


# @lc code=end
def main() -> None:
    sol = Solution()
    ans = sol.minMutation("AACCGGTT", "AACAGGTA", ["AACCGGTA", "AACAGGTA", "AAACGGTA", "AAAAGGTA"])  # ans is 2
    print(ans)


if __name__ == "__main__":
    main()
