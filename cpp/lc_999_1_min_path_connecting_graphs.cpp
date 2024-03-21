/*
### Problem Title: Minimize Longest Path in Connected Graph

**Problem Description:**

Given an undirected, disconnected graph consisting of `n` vertices numbered from
`0` to `n-1` and a list of edges where `edges[i] = [a, b]` indicates an
undirected edge between vertices `a` and `b`, your task is to add the minimum
number of edges to make the graph connected. Among all possible ways to make the
graph connected, you should choose a way that minimizes the number of vertices
on the longest simple path in the resulting graph. Return the number of vertices
on this longest path after making the graph connected.

**Note:**
- A *simple path* in a graph is a path that does not contain repeating vertices.
- The given graph is guaranteed to have no duplicate edges and does not contain
self-loops.
- The resulting graph after adding edges must be connected.

**Function Signature:** `def minimizeLongestPath(n: int, edges: List[List[int]])
-> int:`

**Input:**
- `n`: An integer representing the number of vertices in the graph.
- `edges`: A list of lists, where each sublist contains two integers `[a, b]`
representing an undirected edge between vertices `a` and `b`.

**Output:**
- An integer representing the number of vertices on the longest simple path in
the connected graph formed by adding the minimum number of edges.

**Constraints:**
- `1 <= n <= 10^6`
- `0 <= edges.length <= min(n* (n - 1) / 2, 10^5)`
- `edges[i].length == 2`
- `0 <= a, b < n`
- `a != b`
- There are no duplicate edges in the input.

**Example 1:**

**Input:** `n = 6, edges = [[1, 0], [2, 0], [4, 3], [5, 3]]`

**Output:** `4`

**Explanation:**
Adding an edge between vertices `0` and `3` connects all components while
minimizing the longest path. The longest path could be `2 -> 0 -> 3 -> 5`, which
contains `4` vertices.

**Example 2:**

**Input:** `n = 7, edges = [[0, 1], [1, 2], [3, 4], [5, 6]]`

**Output:** `5`

**Explanation:**
Two edges need to be added: between `1` and `3`, and between `3` and `5` to
connect all components. The longest path could be `0 -> 1 -> 3 -> 5 -> 6`, which
contains `5` vertices.
*/
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <queue>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
  public:
    int min_path_connecting_graphs(int n, vector<vector<int>> &edges) {
        // Create a graph using adjacency list
        vector<vector<int>> graph(n);
        for (auto &edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }

        // Create a visited array to keep track of visited nodes
        vector<bool> visited(n, false);

        // Create a queue to keep track of nodes to visit
        queue<int> q;

        // Add the first node to the queue
        q.push(0);
        visited[0] = true;

        // BFS to find the longest path
        while (!q.empty()) {
            int node = q.front();
            q.pop();
            for (auto &neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    q.push(neighbor);
                    visited[neighbor] = true;
                }
            }
        }

        // Check if all nodes are visited
        for (auto &node : visited) {
            if (!node) {
                return -1;
            }
        }

        // Return the number of vertices on the longest path
        return n - 1;
    }
};

/**
 * @brief Idead for the algorithm
 To solve the problem of adding the minimum number of edges to make an undirected graph connected while minimizing the number of vertices on the longest path, a strategic approach is required. Here’s a possible algorithm, broken down into steps:

### 1. Identify Components and Find Centers
- **Find Connected Components:** Use Depth-First Search (DFS) or Breadth-First Search (BFS) to identify all disconnected components in the graph.
- **Find Longest Path in Each Component:** For each component, find the longest path. This can be done using two BFS/DFS operations:
  - First, start a BFS/DFS from any node in the component and find the farthest node from it. 
  - Second, start another BFS/DFS from the farthest node found in step one to find the actual longest path in that component.
- **Find Centers:** Determine the middle vertex (or two middle vertices) of the longest path in each component. If the path length is odd, there will be one middle vertex. If even, take two middle vertices. These are considered as potential connection points to minimize the longest path in the final graph.

### 2. Connect Components Optimally
- **Form a Virtual Tree of Components:** Consider each component as a node in a virtual tree, where the goal is to connect these nodes in a way that minimizes the height of the tree.
- **Connect Centers to Minimize Height:** Connect the centers of components in a manner that keeps the tree as balanced as possible. Since we only have the centers of components as potential connection points, the idea is to connect them linearly or in a star configuration, depending on the number of components.
  - For a small number of components, a star configuration (connecting all components to a central one) might minimize the longest path.
  - For many components, connecting them linearly or in small groups to form a shallow tree can be more effective.

### 3. Calculate the Longest Path in the Final Graph
- After connecting the components as described, the graph will be connected. 
- Perform a BFS/DFS from any vertex to find the farthest vertex, then perform another BFS/DFS from that vertex to determine the longest path in the now connected graph.

### Remarks and Complexity
- This algorithm focuses on minimizing the longest path by strategically choosing connection points based on the centers of the longest paths in each component.
- The complexity primarily depends on the BFS/DFS operations. Identifying components and the longest paths within them requires up to O(V+E) time for each component, where V is the number of vertices and E is the number of edges in the graph.
- Connecting components and calculating the final longest path also take up to O(V+E) time, making the overall time complexity approximately O(V+E), albeit with a higher constant factor due to the multiple passes over the graph.

This approach aims to balance the graph's connectivity with the objective of minimizing the longest path, leveraging the structure of the components and their intrinsic paths to guide the addition of new edges. Given the constraint of potentially having up to 10^6 vertices, efficiency in identifying components and calculating paths is crucial, making BFS/DFS suitable choices for the core operations. 
 */