/*
 * @lc app=leetcode id=238 lang=cpp
 *
 * [238] Product of Array Except Self
 *
 * https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * algorithms
 * Medium (64.66%)
 * Likes:    15308
 * Dislikes: 864
 * Total Accepted:    1.4M
 * Total Submissions: 2.2M
 * Testcase Example:  '[1,2,3,4]'
 *
 * Given an integer array nums, return an array answer such that answer[i] is
 * equal to the product of all the elements of nums except nums[i].
 *
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 *
 * You must write an algorithm that runs in O(n) time and without using the
 * division operation.
 *
 *
 * Example 1:
 * Input: nums = [1,2,3,4]
 * Output: [24,12,8,6]
 * Example 2:
 * Input: nums = [-1,1,0,-3,3]
 * Output: [0,0,9,0,0]
 *
 *
 * Constraints:
 *
 *
 * 2 <= nums.length <= 10^5
 * -30 <= nums[i] <= 30
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
 * integer.
 *
 *
 *
 * Follow up: Can you solve the problem in O(1) extra space complexity? (The
 * output array does not count as extra space for space complexity analysis.)
 *
 */

// @lc code=start
#include <iostream>
#include <vector>
using namespace std;

template <typename S>
ostream &operator<<(ostream &os, const vector<S> &vector) {
    // Printing all the elements
    // using <<
    for (auto element : vector) {
        os << element << " ";
    }
    return os;
}

class Solution {
  public:
    vector<int> productExceptSelf(vector<int> &nums) {
        // This problem can be thought of fixing number at index i
        // we multiply the prod of left (prefix prod) and
        // multiply the prod of the right (suffix prod)
        
        // ...left prod... i ...right prod...

        // initialize to 1 (identity for prod)
        auto res = vector<int>(nums.size(), 1);

        // get a const reversed reference iterator for nums - non-mutatble
        auto nums_rev = nums.crbegin();
        // get a non-const reverse iterator for res - mutatble
        auto res_rev = res.rbegin();

        // initialize identity for prod
        int left_prod = 1;
        int right_prod = 1;

        for (size_t i = 0; i < nums.size(); i++) {
            // the current res at i -> which is 1
            res[i] *= left_prod;      // times left
            res_rev[i] *= right_prod; // time right (res_rev[i] is equivalent to
                                      // res[n-1-i])
            // accumulate left and right prod
            left_prod *= nums[i];
            right_prod *= nums_rev[i];
        }

        return res;
    }
};
// @lc code=end
