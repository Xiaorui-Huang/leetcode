#include "lc_713_medium_subarray_product_less_than_k.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 713_medium_subarray_product_less_than_k) {
    auto sol = Solution();
    vector<int> arr = {10, 3, 3, 7, 2, 9, 7, 4, 7, 2, 8, 6, 5, 1, 5};
    EXPECT_EQ(sol.numSubarrayProductLessThanK(arr, 30), 26);
}
