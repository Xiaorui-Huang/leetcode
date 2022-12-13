#include "lc_42_hard_trapping_rain_water.cpp"

int main() {
    // vector<int> arr{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    vector<int> arr{4, 2, 0, 3, 2, 5};
    auto ans = Solution().trap(arr);
    std::cout << ans << std::endl;
}