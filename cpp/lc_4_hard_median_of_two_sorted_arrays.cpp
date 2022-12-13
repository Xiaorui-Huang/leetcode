/*
 * @lc app=leetcode id=4 lang=cpp
 *
 * [4] Median of Two Sorted Arrays
 *
 * https://leetcode.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (35.14%)
 * Likes:    20256
 * Dislikes: 2297
 * Total Accepted:    1.6M
 * Total Submissions: 4.7M
 * Testcase Example:  '[1,3]\n[2]'
 *
 * Given two sorted arrays nums1 and nums2 of size m and n respectively, return
 * the median of the two sorted arrays.
 *
 * The overall run time complexity should be O(log (m+n)).
 *
 *
 * Example 1:
 *
 *
 * Input: nums1 = [1,3], nums2 = [2]
 * Output: 2.00000
 * Explanation: merged array = [1,2,3] and median is 2.
 *
 *
 * Example 2:
 *
 *
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 2.50000
 * Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 *
 *
 *
 * Constraints:
 *
 *
 * nums1.length == m
 * nums2.length == n
 * 0 <= m <= 1000
 * 0 <= n <= 1000
 * 1 <= m + n <= 2000
 * -10^6 <= nums1[i], nums2[i] <= 10^6
 *
 *
 */
#include <iostream>
#include <limits>
#include <math.h>
#include <vector>
using namespace std;
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector) {
        os << element << " ";
    }
    return os;
}

// @lc code=start
class Solution {
  public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2) {
        if (nums1.size() > nums2.size())
            nums1.swap(nums2);
        int m = nums1.size(), n = nums2.size();
        int total = m + n;
        int half = total / 2;
        bool is_odd = total % 2;

        int low = 0, high = m - 1;
        // since we are guaranteed to have a medium
        while (true) {
            // using some tricks for c++ integer divide... annoying nonetheless
            int part_index = floor((low + high) / 2.0);    // index in nums1
            int bound_index = half - (part_index + 1) - 1; // index in nums2

            double nums1_left = (part_index >= 0) ? nums1[part_index] : -numeric_limits<double>::infinity();
            double nums1_right = (part_index + 1 < m) ? nums1[part_index + 1] : numeric_limits<double>::infinity();
            double nums2_left = (bound_index >= 0) ? nums2[bound_index] : -numeric_limits<double>::infinity();
            double nums2_right = (bound_index + 1 < n) ? nums2[bound_index + 1] : numeric_limits<double>::infinity();

            if (nums1_left <= nums2_right && nums2_left <= nums1_right)
                if (is_odd)
                    return min(nums1_right, nums2_right);
                else
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0;
            else if (nums1_left > nums2_right) // too many element in nums1 partition
                high = part_index - 1;
            else // (nums2_left > nums1_right) // too many elements in nums partition
                 //
                low = part_index + 1;
        }
    }
};
// @lc code=end
