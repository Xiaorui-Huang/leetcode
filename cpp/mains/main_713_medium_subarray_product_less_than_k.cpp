#include "lc_713_medium_subarray_product_less_than_k.cpp"
int main() {
    // vector<int> nums{10, 5, 2, 6};
    // int k = 100;
    vector<int> nums{1, 1, 1};
    int k = 1;
    auto ans = Solution().numSubarrayProductLessThanK(nums, k);
    std::cout << ans << std::endl;
}
