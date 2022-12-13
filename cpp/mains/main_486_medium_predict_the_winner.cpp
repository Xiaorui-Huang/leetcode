#include "lc_486_medium_predict_the_winner.cpp"

int main() {
    vector<int> nums{1, 5, 233, 7};
    auto ans = Solution().PredictTheWinner(nums);
    std::cout << std::boolalpha << ans << std::endl;
}