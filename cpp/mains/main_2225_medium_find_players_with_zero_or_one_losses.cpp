#include "lc_2225_medium_find_players_with_zero_or_one_losses.cpp"
int main() {
    vector<vector<int>> arr{{1, 3}, {2, 3}, {3, 6}, {5, 6}, {5, 7}, {4, 5}, {4, 8}, {4, 9}, {10, 4}, {10, 9}};
    auto ans = Solution().findWinners(arr);
    std::cout << ans << std::endl;
}
