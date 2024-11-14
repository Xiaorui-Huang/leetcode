#include <algorithm>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

int lcs_dp(const std::vector<int> &A, const std::vector<int> &B) {
    // Get the lengths of the input sequences
    int m = A.size(), n = B.size();

    // Create a 2D vector to store the lengths of the LCS
    std::vector<std::vector<int>> dp(m + 1, std::vector<int>(n + 1, 0));

    // Fill the dp table in a bottom-up manner
    for (int i = 1; i <= m; ++i)
        for (int j = 1; j <= n; ++j)
            if (A[i - 1] == B[j - 1])
                dp[i][j] = 1 + dp[i - 1][j - 1];
            else
                dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);

    // The length of the LCS is stored in dp[m][n]
    return dp[m][n];
}

int lcs_dp_space_optimized(const std::vector<int> &A, const std::vector<int> &B) {
    // Get the lengths of the input sequences
    int m = A.size(), n = B.size();

    // Create a 1D vector to store the lengths of the LCS
    std::vector<int> dp(n + 1, 0);

    // Fill the dp table in a bottom-up manner
    for (int i = 1; i <= m; ++i) {
        int prev = 0;
        for (int j = 1; j <= n; ++j) {
            int temp = dp[j];
            if (A[i - 1] == B[j - 1])
                dp[j] = 1 + prev;
            else
                dp[j] = std::max(dp[j], dp[j - 1]);
            prev = temp;
        }
    }

    // The length of the LCS is stored in dp[n]
    return dp[n];
}

int lcs_hunt_szymanski(const std::vector<int> &A, const std::vector<int> &B) {
    // Step 1: Preprocess B to create a mapping from element to its positions in B
    std::unordered_map<int, std::vector<int>> element_to_indices;
    for (size_t j = 0; j < B.size(); ++j)
        element_to_indices[B[j]].push_back(j);

    // Step 2: Initialize an empty list to store the ends of potential LCS
    /*
     * The tails list is a dynamic list that maintains the smallest possible
     * ending indices of increasing subsequences found so far. Each element in
     * tails represents the end position of an increasing subsequence of a
     * particular length.
     *
     * Example: 
     *      tails[0] holds the smallest possible end index of an LCS of length 1. 
     *      tails[1] holds the smallest possible end index of an LCS of length 2.
    */
    std::vector<int> tails;

    // Step 3: Iterate through A and process matching indices in B
    for (const int &element : A) {
        // If the element is not in B, skip
        if (element_to_indices.find(element) == element_to_indices.end())
            continue;

        // Retrieve the list of indices in B where this element appears
        const std::vector<int> &indices_in_B = element_to_indices[element];

        // Iterate through the indices in reverse to maintain the correct order
        for (auto it = indices_in_B.rbegin(); it != indices_in_B.rend(); ++it) {
            // Binary search to find the insertion point (first index >= *it)
            auto pos = std::lower_bound(tails.begin(), tails.end(), *it);

            // if the element is not found, insert it at the end
            if (pos == tails.end())
                tails.push_back(*it);
            else
                *pos = *it;
            /*
             * When we replace an element in tails (using *pos =
             * current_index), we're effectively updating the end index of a
             * subsequence of that particular length to a smaller index.
             *
             * This is beneficial because:
             *
             * Flexibility: A smaller end index allows for longer subsequences to be built upon it. (achieved by iterating through the indices in reverse)
             * Optimality: Ensures that for each subsequence length, we
             *   maintain the smallest possible end index, maximizing the
             *   chance to extend the subsequence.
             */
        }
    }

    // The size of tails is the length of the LCS
    return tails.size();
}

// Function to compute LCS length using the Hunt-Szymanski algorithm
int lcs_hunt_szymanski_string(const std::string &A, const std::string &B) {
    // Step 1: Preprocess B to create a mapping from character to its positions in B
    std::unordered_map<char, std::vector<int>> char_to_indices;
    for (size_t j = 0; j < B.size(); ++j)
        char_to_indices[B[j]].push_back(j);

    // Step 2: Initialize an empty list to store the ends of potential LCS
    std::vector<int> tails;

    // Step 3: Iterate through A and process matching indices in B
    for (const char &ch : A) {
        // If the character is not in B, skip
        if (char_to_indices.find(ch) == char_to_indices.end())
            continue;

        // Retrieve the list of indices in B where this character appears
        const std::vector<int> &indices_in_B = char_to_indices[ch];

        // Iterate through the indices in reverse to maintain the correct order
        for (auto it = indices_in_B.rbegin(); it != indices_in_B.rend(); ++it) {
            // Binary search to find the insertion point
            auto pos = std::lower_bound(tails.begin(), tails.end(), *it);
            if (pos == tails.end())
                tails.push_back(*it);
            else
                *pos = *it;
        }
    }

    // The size of tails is the length of the LCS
    return tails.size();
}

// Function to compute the LCS string using the Hunt-Szymanski algorithm
std::string get_lcs_hunt_szymanski_string(const std::string &A, const std::string &B) {
    // Step 1: Preprocess B to create a mapping from character to its positions in B
    std::unordered_map<char, std::vector<int>> char_to_indices;
    for (size_t j = 0; j < B.size(); ++j)
        char_to_indices[B[j]].push_back(j);

    // Step 2: Initialize an empty list to store the ends of potential LCS
    std::vector<int> tails;
    std::vector<int> predecessor(A.size(), -1);
    std::vector<int> pos_in_a(A.size(), -1);

    // Step 3: Iterate through A and process matching indices in B
    for (size_t i = 0; i < A.size(); ++i) {
        const char &ch = A[i];

        // If the character is not in B, skip
        if (char_to_indices.find(ch) == char_to_indices.end())
            continue;

        // Retrieve the list of indices in B where this character appears
        const std::vector<int> &indices_in_B = char_to_indices[ch];

        // Iterate through the indices in reverse to maintain the correct order
        for (auto it = indices_in_B.rbegin(); it != indices_in_B.rend(); ++it) {
            // Binary search to find the insertion point
            auto pos = std::lower_bound(tails.begin(), tails.end(), *it);
            int index = pos - tails.begin();

            if (pos == tails.end()) {
                if (!tails.empty())
                    predecessor[index] = pos_in_a[tails.size() - 1];

                tails.push_back(*it);
                pos_in_a[tails.size() - 1] = i;
            } else {
                *pos = *it;
                pos_in_a[index] = i;
                predecessor[index] = (index > 0) ? pos_in_a[index - 1] : -1;
            }
        }
    }

    // Step 4: Reconstruct the LCS string from pos_in_a and predecessor arrays
    std::string lcs(tails.size(), ' ');
    for (int k = pos_in_a[tails.size() - 1], index = tails.size() - 1; index >= 0; k = predecessor[index--])
        lcs[index] = A[k];

    return lcs;
}

int main() {
    // Example usage:
    std::vector<int> A = {1, 3, 4, 1, 2, 3, 4, 1};
    std::vector<int> B = {3, 4, 1, 2, 1, 3, 4, 1, 2};

    int length = lcs_hunt_szymanski(A, B);
    std::cout << "Length of LCS (Hunt-Szymanski): " << length << std::endl;

    return 0;
}
