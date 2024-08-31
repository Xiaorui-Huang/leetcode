"""
Creating a dynamic programming (DP) solution to minimize the total padding
required when batching strings with a constraint on the maximum number of
batches involves defining a DP state that captures the essence of the problem:
we want to minimize the sum of the differences between the maximum string length
in any batch and the lengths of all other strings in that batch.

### Problem Setup
Given:
- An array of string lengths: `L = [l1, l2, ..., ln]`
- A maximum number of batches `k`

Objective:
- Minimize the total padding required when strings are divided into up to `k`
  batches. Padding for a batch is calculated as the difference between the
  maximum string length in that batch and the sum of the lengths of all strings
  in that batch, scaled by the number of strings in that batch minus one.

### DP Definition
Define `dp[i][j]` as the minimum total padding when using the first `i` strings and dividing them into `j` batches.

### Base Cases
- `dp[0][0] = 0`: No strings and no batches means no padding.
- `dp[i][0] = ∞` for all `i > 0`: It's impossible to have batches when no batches are allowed.
- `dp[0][j] = ∞` for all `j > 0`: No strings can't be divided into batches.

### Transition
To compute `dp[i][j]`, consider every possible way to form the `j-th` batch from the first `i` strings. Specifically, if the `j-th` batch starts from string `m+1` to `i`, calculate the padding as:

$$ \text{padding from } m+1 \text{ to } i = (i - m) \times \max(l_{m+1}, ..., l_i) - \sum(l_{m+1}, ..., l_i) $$

Then:

$$ dp[i][j] = \min_{m < i} \left(dp[m][j-1] + \text{padding from } m+1 \text{ to } i\right) $$

This states that the optimal way to divide the first `i` strings into `j` batches is found by trying every possible starting point for the last batch and taking the one that minimizes the total padding incurred in any batch.

### Implementation
Here's a basic outline in pseudocode:
```pseudo
function minimizeTotalPadding(L, k):
    n = length of L
    dp = array of size (n+1) x (k+1) filled with ∞
    dp[0][0] = 0

    for j from 1 to k:
        for i from 1 to n:
            for m from 0 to i-1:
                maxLen = max(L[m+1:i])  // Compute max length from m+1 to i
                sumLen = sum(L[m+1:i])  // Compute sum of lengths from m+1 to i
                padding = (i - m) * maxLen - sumLen
                dp[i][j] = min(dp[i][j], dp[m][j-1] + padding)

    return dp[n][k]
```

### Complexity
The time complexity of this approach is $O(n^2 \times k)$ due to the three
nested loops: one for the batch count, one for the string count, and one to find
where to split the batches. This is feasible for moderate `n` and `k` but may
need optimization or a different approach (like greedy or heuristic methods) for
large inputs.

### Conclusion
This DP formulation provides a framework to solve the problem, but it might be complex for larger values of `n` and `k`. For practical applications, consider heuristic or approximation methods which can provide near-optimal solutions more efficiently.
```
This revised approach provides a complete and coherent description of how to tackle the problem using dynamic programming, while focusing on the specific objective of minimizing the total padding.
```

### Complexity
The time complexity of this approach is $O(n^2 \times k)$ due to the three
nested loops: one for the batch count, one for the string count, and one to find
where to split the batches. This is feasible for moderate `n` and `k` but may
need optimization or a different approach (like greedy or heuristic methods) for
large inputs.

### Conclusion
This DP formulation provides a framework to solve the problem, but it might be
complex for larger values of `n` and `k`. For practical applications, consider
heuristic or approximation methods which can provide near-optimal solutions more
efficiently. """

from functools import lru_cache
import numpy as np

__all__ = ["minimize_max_batch_length"]

METHOD = "KMEANS"
METHOD = "DP_OPT"
METHOD = "DP"


def minimize_max_batch_length_helper_DP(L, k):
    # L = sorted(L)
    # assumes that L is sorted
    for i in range(1, len(L)):
        assert L[i] >= L[i - 1], f"List is not sorted at index {i}"

    n = len(L)
    # Initialize the DP table with infinity for all entries except the base case dp[0][0]
    # we can actually use space optimized dp to get O(n) space complexity
    # since dp[i][j] only depends on dp[m][j-1] where m < i, so we can fix a column j(over k) and reuse the same array
    dp = [[float("inf")] * (k + 1) for _ in range(n + 1)]  # (n+1) x (k+1)
    dp[0][0] = 0

    # Precompute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + L[i - 1]

    # To trace back the partitions
    # partition[i][j] stores the index where the jth batch starts when using the first i strings
    partition = [[-1] * (k + 1) for _ in range(n + 1)]

    # O(n^2) time and space complexity
    # Precompute maximum for each subarray
    # max_in_subarray[i][j] = max(max_in_subarray[i][j-1], L[j])
    # therefore this can also be optimized to O(n) space complexity by reusing the same array
    max_in_subarray = [[0] * n for _ in range(n)]
    for start in range(n):
        current_max = L[start]
        for end in range(start, n):
            current_max = max(current_max, L[end])
            max_in_subarray[start][end] = current_max

    # Fill the DP table
    # k loops, each with n iterations, and each iteration has a loop from 0 to i-1 worst case O(n)
    # Therefore the time complexity is O(n^2 * k) + O(n log n) for sorting = O(n^2 * k)
    for j in range(1, k + 1):
        for i in range(
            1, n + 1 - (k - j)
        ):  # Optimization: the as m: 0 to i-1, and dp[a][j], a >= i are not needed for dp[i][j] (avoid compute for the lower k triangle - k^2/2 iterations)
            # Try every possible way to form the j-th batch from the first i strings
            for m in range(0, i):
                batch_max = max_in_subarray[m][i - 1]  # Compute the maximum in the jth batch
                batch_sum = prefix_sum[i] - prefix_sum[m]  # Compute the sum of lengths in the jth batch
                assert batch_max == max(L[m:i])
                assert batch_sum == sum(L[m:i])
                batch_padding = (i - m) * batch_max - batch_sum
                dp[i][j] = min(dp[i][j], dp[m][j - 1] + batch_padding)
                # record the partition index that minimizes the padding
                if dp[i][j] == dp[m][j - 1] + batch_padding:
                    partition[i][j] = m

    # Reconstruct partitions from the partition table
    partitions = []
    current_index = n
    current_batch = k
    for current_batch in range(k, 0, -1):
        start_index = partition[current_index][current_batch]
        # partitions.append((start_index, current_index))
        partitions.append(L[start_index:current_index])
        current_index = start_index

    partitions.reverse()  # reverse to show partitions in correct order from 0 to n

    padding_given_partition = sum([len(partition) * max(partition) - sum(partition) for partition in partitions])
    assert padding_given_partition == dp[n][k], f"Padding mismatch: {padding_given_partition} != {prev_dp[n]}"

    return dp[n][k], partitions


def minimize_max_batch_length_DP_OPT(L, k):
    # L = sorted(L)
    # assumes that L is sorted
    for i in range(1, len(L)):
        assert L[i] >= L[i - 1], f"List is not sorted at index {i}"
    n = len(L)

    # Prefix sums for constant-time sum queries
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + L[i - 1]

    # Only two arrays for DP
    prev_dp = [float("inf")] * (n + 1)
    curr_dp = [float("inf")] * (n + 1)
    prev_dp[0] = 0  # Base case: no strings, no batches, no padding

    # To trace back the partitions
    # partition[i][j] stores the index where the jth batch starts when using the first i strings
    partition = [[-1] * (k + 1) for _ in range(n + 1)]

    # Compute DP values
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            max_in_batch = float("-inf")
            # m runs from i-1 to 0, in order to compute max_in_batch - max(L[m:i]), since i is fixed and m varies
            for m in range(i - 1, 0 - 1, -1):
                max_in_batch = max(max_in_batch, L[m])
                next_batch_sum = prefix_sum[i] - prefix_sum[m]
                next_batch_padding = (i - m) * max_in_batch - next_batch_sum
                curr_dp[i] = min(curr_dp[i], prev_dp[m] + next_batch_padding)

                # record the partition index that minimizes the padding
                if curr_dp[i] == prev_dp[m] + next_batch_padding:
                    # partition_index[j] = m
                    partition[i][j] = m

        # reuse the same array for next iteration
        prev_dp, curr_dp = curr_dp, [float("inf")] * (n + 1)

    # Reconstruct partitions from the partition table
    partitions = []
    current_index = n
    current_batch = k
    for current_batch in range(k, 0, -1):
        start_index = partition[current_index][current_batch]
        # partitions.append((start_index, current_index))
        partitions.append(L[start_index:current_index])
        current_index = start_index

    partitions.reverse()  # reverse to show partitions in correct order from 0 to n

    # padding_given_partition = sum([len(partition) * max(partition) - sum(partition) for partition in partitions])
    # assert padding_given_partition == prev_dp[n], f"Padding mismatch: {padding_given_partition} != {prev_dp[n]}"

    return prev_dp[n], partitions

# https://en.wikipedia.org/wiki/K-means++
# complexity 
def initialize_centroids_kmeans_plusplus(lengths, k):
    # Randomly choose the first centroid from the data points
    centroids = [np.random.choice(lengths)]
    
    
    for _ in range(1, k):
        # O(n) time complexity for each iteration - We calculate the squared distances from the centroids
        distances = np.min((lengths[:, None] - centroids) ** 2, axis=1)
        probabilities = distances / distances.sum()
        # create a cumulative distribution from squared distances probabilities
        cumulative_probabilities = probabilities.cumsum()
        # a random number between 0 and 1
        r = np.random.rand() 
        
        # Find the next centroid by selecting the first point that fits into the cumulative distribution
        for i, p in enumerate(cumulative_probabilities):
            if r < p:
                centroids.append(lengths[i])
                break
    
    return np.array(centroids)
# there is also a parallel version of kmeans++ initialization
# keams||
"""  toy example
def k_means_parallel(lengths, k, l=2, r=5):
    # Convert lengths to a numpy array for easier manipulation
    lengths = np.array(lengths)
    
    # Step 1: Initialize by selecting one centroid randomly
    centroids = [np.random.choice(lengths)]
    
    # Step 2: Parallel sampling phase
    for _ in range(r):
        distances = np.array([min((l - c) ** 2 for c in centroids) for l in lengths])
        probabilities = l * distances / distances.sum()
        new_centroids = np.random.choice(lengths, size=len(lengths), replace=True, p=probabilities)
        centroids = np.unique(np.concatenate((centroids, new_centroids)))  # Unique to avoid duplicates

    # Step 3: Reduction step to reduce to k centroids using k-means++
    centroids = initialize_centroids_kmeans_plusplus(centroids, k)

    # Perform k-means with these centroids
    return k_means_1d(lengths.tolist(), k, initial_centroids=centroids)
"""

# O(nki) time complexity
# where n is the number of strings, k is the number of batches, and i is the number of iterations
# and i is a small constant in practice, depending on the distribution of string lengths and a good initial guess
def k_means_1d(lengths, k, lambda_reg=0.01, max_iterations=20, use_kmeans_plusplus=True):
    # Convert lengths to a numpy array for easier manipulation
    lengths = np.array(lengths)

    # # Initialize centroids to k random lengths
    # equal_indices_k = np.linspace(0, len(lengths) - 1, k, dtype=int)
    # # percentile based initialization
    # centroids = lengths[equal_indices_k]

    # percentile based initialization
    centroids = initialize_centroids_kmeans_plusplus(lengths, k) if use_kmeans_plusplus else np.percentile(lengths, np.linspace(0, 100, k))
    
    assignments = None

    iterations = 0
    for _ in range(max_iterations):
        # Step 2: Assign strings to the nearest centroid
        # O(nk) time complexity for each iteration - We calculate assignements for each string with each centroid
        new_assignments = np.argmin(np.abs(lengths[:, None] - centroids), axis=1)

        # Check for convergence
        if np.array_equal(assignments, new_assignments):
            break
        assignments = new_assignments
        iterations += 1

        # Step 3: Update centroids to be the mean of assigned lengths
        # O(n) time complexity for each iteration - We calculate the mean of the assigned strings to each centroid
        for i in range(k):
            if np.any(assignments == i):  # Check if any string is assigned to this centroid to avoid division by zero
                centroids[i] = np.mean(lengths[assignments == i])

    # Form the final clusters
    clusters = [lengths[assignments == i].tolist() for i in range(k)]
    for i in range(k):
        clusters[i].sort()
    clusters.sort(key=lambda x: x[0] if x else float("inf"))
    paddings = sum([np.sum(max(lengths[assignments == i]) - lengths[assignments == i] if np.any(assignments == i) else 0) for i in range(k)])

    # return paddings, centroids, clusters, iterations
    return paddings, clusters, iterations


def minimize_max_batch_length_brute_force(L, k):
    @lru_cache(maxsize=None)
    def minimize_max_batch_length_brute_force_helper(L, k):
        L = tuple(L)
        n = len(L)
        if k == 1:
            # Only one batch, return the sum of padding for this single batch
            return sum(max(L) - x for x in L), [L]  # Entire array is one batch

        min_padding = float("inf")
        best_partition = None

        # Try every possible way to split the array into the first batch and the rest
        for i in range(1, n - k + 2):  # Ensure there's enough room for remaining k-1 batches
            first_batch = L[:i]
            remaining_batches = L[i:]

            # Calculate the current batch padding
            current_batch_padding = sum([max(first_batch) - x for x in first_batch])

            # Recursive call to process the remaining part of the list
            remaining_padding, remaining_partition = minimize_max_batch_length_brute_force_helper(remaining_batches, k - 1)

            # Calculate total padding if this partitioning is chosen
            total_padding = current_batch_padding + remaining_padding

            # Update minimum padding found and best partitioning
            if total_padding < min_padding:
                min_padding = total_padding
                best_partition = [first_batch] + remaining_partition

        return min_padding, best_partition

    padding, unprocessed = minimize_max_batch_length_brute_force_helper(L, k)
    return padding, [[int(x) for x in part] for part in unprocessed]

def equal_partition(L, k):
    # split into k paritions exactly
    n = len(L)
    partitions = []
    for i in range(k):
        partitions.append(L[i * n // k : (i + 1) * n // k])
    padding = sum(len(partition) * max(partition) - sum(partition) for partition in partitions)
    return padding, partitions

def minimize_max_batch_length(L, k, method=METHOD):
    L.sort()
    match method:
        case "DP":
            ans = minimize_max_batch_length_helper_DP(L, k)
        case "DP_OPT":
            ans = minimize_max_batch_length_DP_OPT(L, k)
        case "KMEANS":
            ans = k_means_1d(L, k)
        case "KMEANS++":
            ans = k_means_1d(L, k, use_kmeans_plusplus=True)
        case "BRUTE_FORCE":
            L = tuple(L)
            ans = minimize_max_batch_length_brute_force(L, k)
        case "EQUAL_PARTITION":
            ans = equal_partition(L, k)
        case _:
            raise ValueError(f"Invalid method: {METHOD}")
    assert len(ans[1]) == k, f"Number of partitions mismatch: {len(ans[1])} != {k}"
    return ans


if __name__ == "__main__":
    # Test cases
    L1 = [5, 3, 5, 2, 4, 4, 1, 7]  # expects 5 and [[1, 2, 3], [4, 4, 5, 5], [7]]
    k1 = 3
    L2 = [10, 5, 2, 3, 8, 7, 6, 1]
    k2 = 4
    L3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k3 = 5

    # Parameters for the gamma distribution
    shape = 2.0  # Shape parameter (k > 0, the higher the less skewed)
    scale = 10.0  # Scale parameter (theta > 0)

    # Generate the data
    np.random.seed(42)  # Seed for reproducibility
    L4 = np.random.gamma(shape, scale, 40).astype(int)
    k4 = 8

    # Print results of the test cases
    print("Test Case 1:", minimize_max_batch_length(L1, k1))
    print("Test Case 2:", minimize_max_batch_length(L2, k2))
    print("Test Case 3:", minimize_max_batch_length(L3, k3))
    print("Test Case 4:", minimize_max_batch_length(L4, k4))
