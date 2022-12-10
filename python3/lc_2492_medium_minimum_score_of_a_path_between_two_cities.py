#
# @lc app=leetcode id=2492 lang=python3
#
# [2492] Minimum Score of a Path Between Two Cities
#
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/
#
# algorithms
# Medium (45.39%)
# Likes:    209
# Dislikes: 30
# Total Accepted:    11.5K
# Total Submissions: 25.4K
# Testcase Example:  '4\n[[1,2,9],[2,3,6],[2,4,5],[1,4,7]]'
#
# You are given a positive integer n representing n cities numbered from 1 to
# n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei]
# indicates that there is a bidirectional road between cities ai and bi with a
# distance equal to distancei. The cities graph is not necessarily connected.
#
# The score of a path between two cities is defined as the minimum distance of
# a road in this path.
#
# Return the minimum possible score of a path between cities 1 and n.
#
# Note:
#
#
# A path is a sequence of roads between two cities.
# It is allowed for a path to contain the same road multiple times, and you can
# visit cities 1 and n multiple times along the path.
# The test cases are generated such that there is at least one path between 1
# and n.
#
#
#
# Example 1:
#
#
# Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
# Output: 5
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 ->
# 4. The score of this path is min(9,5) = 5.
# It can be shown that no other path has less score.
#
#
# Example 2:
#
#
# Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
# Output: 2
# Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1
# -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
#
#
#
# Constraints:
#
#
# 2 <= n <= 10^5
# 1 <= roads.length <= 10^5
# roads[i].length == 3
# 1 <= ai, bi <= n
# ai != bi
# 1 <= distancei <= 10^4
# There are no repeated edges.
# There is at least one path between 1 and n.
#
#
#

# @lc code=start
from enum import Enum

# other possible approaches
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solutions/2874954/simple-bfs/?languageTags=python3
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/solutions/2874976/python-union-find-minimum-spanning-tree/?page=2
appr = Enum("approaches", "disjoint_set graph")
APPR = appr.graph


class Solution:
    def minScore(self, n: int, roads: list[tuple[int, int, int]]) -> int:
        if APPR == appr.disjoint_set:
            return self.minScore_disjoint_set(n, roads)
        if APPR == appr.graph:
            return self.minScore_graph(n, roads)
        return 0  # Never Reached

    def minScore_graph(self, n: int, roads: list[tuple[int, int, int]]) -> int:
        # reframe question... can we get to some node with a small distance first then to node n?
        # O(E) - process data -> adjacency list and list of scores
        # O(V) - DFS and store distance edges
        # O(E) - find min out of distances
        adjacency_list: dict[int, list[tuple[int, int]]] = {}

        for city_a, city_b, distance in roads:
            set_a = adjacency_list.setdefault(city_a, [])
            set_b = adjacency_list.setdefault(city_b, [])
            set_a.append((city_b, distance))
            set_b.append((city_a, distance))

        def find_path_to_cities() -> list[int]:
            # DFS to find all connected cities and return their scores
            distances: list[int] = []
            seen: set[int] = set([1])
            stack: list[int] = [1]
            while stack:
                cur_city = stack.pop()
                neighbors = adjacency_list[cur_city]
                for neighbor, distance in neighbors:
                    distances.append(distance)
                    if neighbor not in seen:
                        stack.append(neighbor)
                        seen.add(neighbor)
            return distances

        return min(find_path_to_cities())

    def minScore_disjoint_set(self, n: int, roads: list[tuple[int, int, int]]) -> int:
        # TIME LIMIT EXCEEDED - O(|E|^2 + |E||V|)

        # disjoint set problem
        connected_graphs: list[tuple[set[int], int]] = []

        # O(|E|)
        for city_a, city_b, distance in roads:
            # gather info about city
            graph_a, graph_b = None, None
            # O(|E|)
            for i, (graph, min_score) in enumerate(connected_graphs):
                if city_a in graph:
                    graph_a = graph
                    i_a = i
                    min_score_a = min_score
                if city_b in graph:
                    graph_b = graph
                    i_b = i
                    min_score_b = min_score

            # if neither graph belongs to any existing graph, create a new graph
            if graph_a is None and graph_b is None:
                connected_graphs.append((set([city_a, city_b]), distance))

            # O(|V|)
            elif graph_a and graph_b:
                # merge two sets
                if graph_a is not graph_b:
                    graph_a.update(graph_b)
                    connected_graphs[i_a] = (graph_a, min(distance, min_score_a, min_score_b))
                    connected_graphs.pop(i_b)
                else:  # new edge within the same graph, use the min
                    connected_graphs[i_a] = (graph_a, min(min_score_a, distance))

            # add to set a
            elif graph_a:
                graph_a.add(city_b)
                connected_graphs[i_a] = (graph_a, min(min_score_a, distance))

            # add to set b
            elif graph_b:  # graph_b
                graph_b.add(city_a)
                connected_graphs[i_b] = (graph_b, min(min_score_b, distance))
            else:
                print("we have a situation")  # Never Reached

        # O(|E|) - usually quite small
        for graph, min_score in connected_graphs:
            if 1 in graph:
                return min_score
        return 10**4  # Never Reached


# @lc code=end
