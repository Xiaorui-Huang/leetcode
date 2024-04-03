#ifndef LC_713_MEDIUM_SUBARRAY_PRODUCT_LESS_THAN_K_H
#define LC_713_MEDIUM_SUBARRAY_PRODUCT_LESS_THAN_K_H
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
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

// @lc code=start
#include <limits>

#define LOG_BINARY_SEARCH 0
#define SLIDING_WINDOW 1 
#define LOG_SLIDING_WINDOW 2 // does not work due to floating point precision

// #define APPR LOG_SLIDING_WINDOW
#define APPR SLIDING_WINDOW

class Solution {
  public:
    int numSubarrayProductLessThanK(vector<int> &nums, int k) {
#if APPR == SLIDING_WINDOW
        /**
         * Something to note is that the Sliding Window approach will benefit
         * from logarithms as much as the Binary Search approach. Even though,
         * given constraints on k and nums[i], overflow can't really happen
         * under the Sliding Window strategy here, a slight change in the
         * constraints can make them possible, and then if you are interviewing
         * for a machine learning/data science position using logarithms will be
         * fully expected. You may actually fail such an interview if you don't
         * use them, and mentioning them will in any case impress the
         * interviewer. Whenever you need to compare potentially large products
         * (and products tend to get large very quickly!), the logarithm trick
         * is useful to remember.
         * 
         * https://leetcode.com/problems/subarray-product-less-than-k/editorial/comments/2320196
         */
        int count = 0, left = 0, prod = 1, len;

        for (size_t right = 0; right < nums.size(); right++) {
            prod *= nums[right];
            // left <= right and not just < is because we would like to
            // shift (if possible) all the way for left > right i.e. no values
            // in the current interval
            //
            // e.g. k = 100 and we suddenly mutiply 100
            // meaning we'd have to shift all the way to just have 100 nothing in the current interval
            // since 100 is not strictly less than 100
            // therefore we need the ability to have nothing in our interval
            while (prod >= k && left <= right)
                prod /= nums[left++];

            len = right - left + 1;
            count += len;
        }

        return count;
#elif APPR == LOG_SLIDING_WINDOW // !NB Does not work, due to floating point precision
        if (k == 0) // log and values below 1 don't mix well
            return 0;
        int count = 0;
        double log_k = log(k); // - std::numeric_limits<double>::epsilon(); // for numeric stability
        double log_sum = 0;    //since log(1) = 0;
        // log_sum += std::numeric_limits<double>::epsilon(); // numeric stability
        int left = 0, n = nums.size();
        int len;

        // floating pint
        for (int right = 0; right < n; right++) {
            log_sum += log(nums[right]);

            if (k <= nums[right]) {
                left = right + 1;
                continue; // new number is too big we will skip
            }
            while (!(log_sum < log_k) && left <= right)
                log_sum -= log(nums[left++]);

            len = right - left + 1;
            count += len;
        }
        return count;
#elif APPR == LOG_BINARY_SEARCH
        // binary search on log prefix sum - inginius
        // O(n log n)
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
#endif
    }
};
// @lc code=end
#endif
