/*
 * @lc app=leetcode id=1514 lang=c
 *
 * [1514] Path with Maximum Probability
 *
 * https://leetcode.com/problems/path-with-maximum-probability/description/
 *
 * algorithms
 * Medium (54.66%)
 * Likes:    3535
 * Dislikes: 95
 * Total Accepted:    242.2K
 * Total Submissions: 394.7K
 * Testcase Example:  '3\n[[0,1],[1,2],[0,2]]\n[0.5,0.5,0.2]\n0\n2'
 *
 * You are given an undirected weighted graph of n nodes (0-indexed),
 * represented by an edge list where edges[i] = [a, b] is an undirected edge
 * connecting the nodes a and b with a probability of success of traversing
 * that edge succProb[i].
 * 
 * Given two nodes start and end, find the path with the maximum probability of
 * success to go from start to end and return its success probability.
 * 
 * If there is no path from start to end, return 0. Your answer will be
 * accepted if it differs from the correct answer by at most 1e-5.
 * 
 * 
 * Example 1:
 * 
 * 
 * 
 * 
 * Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start =
 * 0, end = 2
 * Output: 0.25000
 * Explanation: There are two paths from start to end, one having a probability
 * of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
 * 
 * 
 * Example 2:
 * 
 * 
 * 
 * 
 * Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start =
 * 0, end = 2
 * Output: 0.30000
 * 
 * 
 * Example 3:
 * 
 * 
 * 
 * 
 * Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
 * Output: 0.00000
 * Explanation: There is no path between 0 and 2.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= n <= 10^4
 * 0 <= start, end < n
 * start != end
 * 0 <= a, b < n
 * a != b
 * 0 <= succProb.length == edges.length <= 2*10^4
 * 0 <= succProb[i] <= 1
 * There is at most one edge between every two nodes.
 * 
 * 
 */

 
#include "vector.h"
// @lc code=start
// ##################################################################################################
#define VEC_IMPL(T)                                                                                 \
    typedef struct {                                                                                \
        int size;                                                                                   \
        int cap;                                                                                    \
        T *data;                                                                                    \
    } Vec_##T;                                                                                      \
                                                                                                    \
    static Vec_##T *vec_new_##T(int init_cap) {                                                     \
        assert(init_cap > 0);                                                                       \
        Vec_##T *vec = (Vec_##T *)malloc(sizeof(Vec_##T));                                          \
        vec->size = 0;                                                                              \
        vec->cap = init_cap;                                                                        \
        vec->data = (T *)malloc(sizeof(T) * init_cap);                                              \
        return vec;                                                                                 \
    }                                                                                               \
                                                                                                    \
    static void vec_free_##T(Vec_##T *vec) {                                                        \
        free(vec->data);                                                                            \
        free(vec);                                                                                  \
    }                                                                                               \
                                                                                                    \
    static void vec_push_##T(Vec_##T *vec, T item) {                                                \
        if (vec->size == vec->cap) {                                                                \
            vec->cap *= 2;                                                                          \
            vec->data = (T *)realloc(vec->data, sizeof(T) * vec->cap);                              \
        }                                                                                           \
        vec->data[vec->size++] = item;                                                              \
    }                                                                                               \
                                                                                                    \
    static T vec_pop_##T(Vec_##T *vec) {                                                            \
        assert(vec->size > 0);                                                                      \
        return vec->data[--vec->size];                                                              \
    }
// ##################################################################################################
#include <float.h>
#include <stdbool.h>
#include <string.h>

typedef struct {
    int to;
    double prob;
} Edge;

typedef struct {
    int node;
    int parent;
    double cur_prob;
} Layer;

// VECTOR_IMPL(int)
VEC_IMPL(Edge)
VEC_IMPL(Layer)

#define DFS 0
#define BELLMAN_FORD 1

#define APPR BELLMAN_FORD
// #define APPR DFS

// ignore edgesColSize...
double maxProbability(int n,
                      int **edges,
                      int edgesSize,
                      int *edgesColSize,
                      double *succProb,
                      int succProbSize,
                      int start_node,
                      int end_node) {
#if APPR == DFS
    // building the graph
/*
 *
 *
 * To analyze the worst-case time complexity of this DFS-based approach for finding the maximum probability path, let's break down the algorithm:
 * 
 * 1. Graph Construction:
 *    - Time: O(V + E), where V is the number of vertices (n) and E is the number of edges (edgesSize)
 *    - Space: O(V + E) for the adjacency list representation
 * 
 * 2. DFS Traversal:
 *    In the worst case, the DFS might explore all possible paths in the graph. 
 * 
 *    The worst-case scenario occurs when:
 *    - The graph is complete (every node is connected to every other node)
 *    - The end_node is never reached or is the last node to be reached
 *    - Each path exploration increases the probability, forcing us to explore all paths
 * 
 *    In this case:
 *    - Time: O(V!) 
 *      Explanation: In a complete graph with V nodes, from each node, we have V-1 choices for the next node, then V-2 for the next, and so on. This leads to V * (V-1) * (V-2) * ... * 1 = V! paths.
 *    - Space: O(V!) In the worst case, the stack could contain multiple entries
 *          for the same node, each representing a different path to that node with a
 *          different probability. The number of possible paths in a graph can be
 *          exponential in the number of nodes. In a complete graph with V nodes,
 *          there could be up to (V)! simple paths between any two nodes. 
 *
 * 3. Overall:
 *    - Time Complexity: O(V! + E)
 *    - Space Complexity: O(V! + E)
 * 
 * The V! factor makes this algorithm exponential in the worst case, which is extremely inefficient for large graphs. This is why depth-first search is generally not recommended for finding optimal paths in weighted graphs, especially when negative weights (or in this case, probabilities less than 1) are involved.
 * 
 * For this problem, a more efficient approach would be to use Dijkstra's algorithm (for graphs with non-negative weights) or the Bellman-Ford algorithm (if negative weights are possible). These algorithms have polynomial time complexities:
 * 
 * - Dijkstra's algorithm: O((V + E) log V) with a priority queue
 * - Bellman-Ford algorithm: O(VE)
 * 
 * Both would be significantly more efficient than the current DFS approach for larger graphs.
 * 
 * Would you like me to explain how to implement a more efficient solution using one of these algorithms?
 * 
*/
    Vec_Edge **graph = (Vec_Edge **)malloc(sizeof(Vec_Edge *) * n);
    for (int i = 0; i < n; i++)
        graph[i] = vec_new_Edge(1);

    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        vec_push_Edge(graph[a], (Edge){.to = b, .prob = succProb[i]});
        vec_push_Edge(graph[b], (Edge){.to = a, .prob = succProb[i]});
    }
    // dfs
    double max_prob = DBL_MIN;
    double *max_probs = (double *)malloc(sizeof(double) * n);
    memset(max_probs, 0, sizeof(double) * n);
    Vec_Layer *stack = vec_new_Layer(1);
    // -1 for no parent
    vec_push_Layer(stack, (Layer){.node = start_node, .parent = -1, .cur_prob = 1});
    while (stack->size != 0) {
        // pop next nodes
        Layer layer = vec_pop_Layer(stack);
        Vec_Edge *edges = graph[layer.node];
        // iter over neighbours
        for (int i = 0; i < edges->size; i++) {
            Edge edge = edges->data[i];
            int neighbour = edge.to;
            double prob = edge.prob * layer.cur_prob;
            // check if we have arrived
            if (neighbour == end_node) {
                max_prob = (prob > max_prob) ? prob : max_prob;
            }
            // Don't go back to parent
            // Don't explore after reaching end_node
            // Don't explore useless path that has low probs
            if (neighbour != layer.parent && neighbour != end_node && prob > max_probs[neighbour]) {
                vec_push_Layer(stack, (Layer){.cur_prob = prob, .node = neighbour, .parent = i});
                max_probs[neighbour] = prob;
            }
        }
    }
    return max_prob;
#elif APPR == BELLMAN_FORD
    // complexity O(VE)
    double *max_probs = (double *)malloc(sizeof(double) * n);
    memset(max_probs, 0, sizeof(double) * n);
    max_probs[start_node] = 1;

    for (int _ = 1; _ <= n - 1; _++) { // V - 1 iterations, since the longest path length in G(V, E) is V - 1
        bool updated = false;
        for (int i = 0; i < edgesSize; i++) {
            int u = edges[i][0], v = edges[i][1];
            // check both directions with undirected graph
            if (max_probs[u] * succProb[i] > max_probs[v]) {
                max_probs[v] = max_probs[u] * succProb[i];
                updated = true;
            }
            if (max_probs[v] * succProb[i] > max_probs[u]) {
                max_probs[u] = max_probs[v] * succProb[i];
                updated = true;
            }
        }
        if (!updated)
            break;
    }
    // we skip the final relaxation step since all probs are >= 0
    return max_probs[end_node];
#endif
}
// @lc code=end
