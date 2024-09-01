
// #include <algorithm>
// #include <cmath>
#include <iostream>
// #include <limits>
// #include <unordered_map>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

// Implements Dijkstra's algorithm using a 'set' for the priority queue. The
// 'set' is chosen because it automatically orders its elements, ensuring the
// element with the smallest distance is always at the beginning. This property
// is essential for efficiently selecting the next vertex with the minimum
// distance from the source in Dijkstra's algorithm. The algorithm finds the
// shortest paths from a single source to all other nodes in a graph represented
// as an adjacency list of weighted edges.
//
vector<int> dijkstra(int n, int source, vector<pair<int, int>> G[]) {
    // Define "infinity" as a large number to represent unreachable distances
    // initially.
    int INF = (int)1e9;

    // Initialize distances from source to all nodes as infinity.
    vector<int> D(n, INF);

    D[source] = 0; // Set the distance from the source to itself to 0.

    // Use a set as a priority queue to maintain pairs of
    // (distance to a node, node ID) in sorted order by distance.
    set<pair<int, int>> Q;
    // Insert the source node with distance 0 into the queue.
    Q.insert({0, source});

    // While the queue is not empty, extract the node with the minimum distance
    // and examine its neighbors.
    while (!Q.empty()) {
        // 'begin()' points to the pair with the smallest distance due to set's
        // sorting.
        auto top = Q.begin();
        int u = top->second; // Current node to process.
        Q.erase(top);        // Remove this node from the priority queue.

        // Relaxation step: For each neighbor of u, check if we can improve the
        // distance to that neighbor.
        for (auto next : G[u]) {
            int v = next.first, weight = next.second;
            if (D[u] + weight < D[v]) {
                // If a shorter path from u to v is found, update its distance
                // and insert the new distance into the set.

                // First, remove the old pair associated with v if it exists.
                if (D[v] != INF)
                    Q.erase({D[v], v});

                // Update the distance to v.
                D[v] = D[u] + weight;
                // Insert the new distance and node pair into the set.
                Q.insert({D[v], v});
            }
        }
    }
    return D; // Return the vector of distances from source to all nodes.
}

int main() {
    int n, m, s, x, y, z;
    cin >> n >> m >> s;
    // Input the number of nodes(0 based), number of edges and the source
    // vertex.

    vector<pair<int, int>> *G = new vector<pair<int, int>>[n];
    vector<int> ans;
    for (int i = 0; i < m; i++) {
        cin >> x >> y >> z;
        // Input the starting vertex of the edge, the ending vertex and the cost
        // of the edge.
        G[x].push_back(make_pair(y, z));
    }
    ans = dijkstra(n, s, G); // ans has the cost from source to all the
                             // vertices.
    for (int i = 0; i < n; i++)
        cout << ans[i] << " ";
    cout << endl;
}