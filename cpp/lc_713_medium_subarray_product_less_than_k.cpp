/*
 * @lc app=leetcode id=713 lang=cpp
 *
 * [713] Subarray Product Less Than K
 *
 * https://leetcode.com/problems/subarray-product-less-than-k/description/
 *
 * algorithms
 * Medium (45.04%)
 * Likes:    4841
 * Dislikes: 155
 * Total Accepted:    207.3K
 * Total Submissions: 458.3K
 * Testcase Example:  '[10,5,2,6]\n100'
 *
 * Given an array of integers nums and an integer k, return the number of
 * contiguous subarrays where the product of all the elements in the subarray
 * is strictly less than k.
 *
 *
 * Example 1:
 *
 *
 * Input: nums = [10,5,2,6], k = 100
 * Output: 8
 * Explanation: The 8 subarrays that have product less than 100 are:
 * [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
 * Note that [10, 5, 2] is not included as the product of 100 is not strictly
 * less than k.
 *
 *
 * Example 2:
 *
 *
 * Input: nums = [1,2,3], k = 0
 * Output: 0
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= nums.length <= 3 * 10^4
 * 1 <= nums[i] <= 1000
 * 0 <= k <= 10^6
 *
 *
 */

#include <algorithm>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// @lc code=start
#define APPR sliding_window
enum appr { log_binary_search, sliding_window };

class Solution {
  public:
    int numSubarrayProductLessThanK(vector<int> &nums, int k) {
        if (APPR == log_binary_search)
            return numSubarrayProductLessThanK_log_binary_search(nums, k);
        if (APPR == sliding_window)
            return numSubarrayProductLessThanK_sliding_window(nums, k);
        return 0; // never reached
    }
    int numSubarrayProductLessThanK_sliding_window(vector<int> &nums, int k) {
        int count = 0, left = 0, prod = 1;

        for (size_t right = 0; right < nums.size(); right++) {
            prod *= nums[right];
            // left <= right and not just < is because we would like to
            // shift (if possible) all the way for left == right with
            // interval of width 1, otherwise there would be a bug
            while (prod >= k && left <= right)
                prod /= nums[left++];

            count += right - left + 1;
        }
        return count;
    }

    int numSubarrayProductLessThanK_log_binary_search(vector<int> &nums, int k) {
        if (k == 0)
            return 0;

        auto log_k = log(k);
        vector<double> log_sums(nums.size() + 1, 0);
        for (size_t i = 1; i < log_sums.size(); i++)
            log_sums[i] = log_sums[i - 1] + log(nums[i - 1]);

        /**
         * @brief given log_sums is sorted find index i such that
         * i is the largest index for which log_sums[i] < target
         * @pre lo <= hi
         */
        auto bisect = [&log_sums](double target, int lo, int hi) -> int {
            // when target is less than all numbers
            if (log_sums[lo] >= target)
                return lo - 1;

            while (lo < hi) {
                auto mid = (lo + hi) / 2;
                if (log_sums[mid] < target) {
                    if (log_sums[mid + 1] >= target)
                        return mid;
                    lo = mid + 1;
                } else
                    hi = mid - 1;
            }
            return lo;
        };

        int count = 0;
        for (size_t i = 0; i < log_sums.size() - 1; i++) {
            auto j_plus_one = bisect(log_k + log_sums[i], i + 1, log_sums.size() - 1);
            count += j_plus_one - i;
        }
        return count;
    }
};
// @lc code=end
