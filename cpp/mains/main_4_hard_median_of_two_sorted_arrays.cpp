#include "lc_4_hard_median_of_two_sorted_arrays.cpp"

int main() {
    vector<int> arr1{1, 3};
    vector<int> arr2{2};
    // vector<int> arr1{1, 2, 3, 4};
    // vector<int> arr2{1, 2, 3, 5, 6, 6, 7, 8, 10, 11};
    //  1,1,2,2,3,3,4, (5), 6,6,7,8,10,11,12

    auto ans = Solution().findMedianSortedArrays(arr1, arr2);
    std::cout << ans << std::endl;
}
