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

int main() {
    // Example usage:
    std::vector<int> A = {1, 3, 4, 1, 2, 3, 4, 1};
    std::vector<int> B = {3, 4, 1, 2, 1, 3, 4, 1, 2};

    int length = lcs_hunt_szymanski(A, B);
    std::cout << "Length of LCS (Hunt-Szymanski): " << length << std::endl;

    return 0;
}
