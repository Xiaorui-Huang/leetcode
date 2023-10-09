/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 *
 * https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
 *
 * algorithms
 * Medium (42.80%)
 * Likes:    18822
 * Dislikes: 453
 * Total Accepted:    1.7M
 * Total Submissions: 4M
 * Testcase Example:  '[5,7,7,8,8,10]\n8'
 *
 * Given an array of integers nums sorted in non-decreasing order, find the
 * starting and ending position of a given target value.
 *
 * If target is not found in the array, return [-1, -1].
 *
 * You must write an algorithm with O(log n) runtime complexity.
 *
 *
 * Example 1:
 * Input: nums = [5,7,7,8,8,10], target = 8
 * Output: [3,4]
 * Example 2:
 * Input: nums = [5,7,7,8,8,10], target = 6
 * Output: [-1,-1]
 * Example 3:
 * Input: nums = [], target = 0
 * Output: [-1,-1]
 *
 *
 * Constraints:
 *
 *
 * 0 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * nums is a non-decreasing array.
 * -10^9 <= target <= 10^9
 *
 *
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S>
ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// @lc code=start
class Solution {
  public:
    vector<int> searchRange(vector<int> &nums, int target) {
        /**
         * @brief Return the lowest index of the target, if target exists.
         *
         * if not, return the index of the first number > target
         */
        auto binarySearchLeft = [&]() -> int {
            int mid;
            int lo = 0, hi = nums.size() - 1;
            while (lo <= hi) {
                mid = (lo + hi) / 2;
                // finding the highest element less than target (which is at
                // mid) we plus one to make it in range with target, if target
                // exists if not it will be bigger than target
                if (nums.at(mid) < target)
                    lo = mid + 1;
                else
                    hi = mid - 1;
            }
            return lo;
        };

        /**
         * @brief Return the highest index of the target, if target exists.
         *
         * if not, return the index of the largest number < target
         */
        auto binarySearchRight = [&]() -> int {
            int mid;
            int lo = 0, hi = nums.size() - 1;

            while (lo <= hi) {
                mid = (lo + hi) / 2;
                
                // find the highest number <= target
                if (nums.at(mid) <= target)
                    lo = mid + 1;
                else
                    hi = mid - 1;
            }
            return hi;
        };

        auto left = binarySearchLeft(), right = binarySearchRight();

        if (left > right)
            return {-1, -1};

        return {left, right};
    }
};
// @lc code=end
