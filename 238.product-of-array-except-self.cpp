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

template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
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
        vector<int> res(nums.size(), 1);
        auto nums_reverse = nums.rbegin(), res_reverse = res.rbegin();
        int prefixProd = 1, suffixProd = 1;

        for (size_t i = 1; i < nums.size(); i++) {
            prefixProd *= nums[i - 1];
            suffixProd *= nums_reverse[i - 1];
            res[i] *= prefixProd;
            res_reverse[i] *= suffixProd;
        }

        return res;
    }
};
// @lc code=end

int main() {
    vector<int> nums{1, 2, 3, 4};
    auto ans = Solution().productExceptSelf(nums);
    std::cout << ans << std::endl;
    return 0;
}