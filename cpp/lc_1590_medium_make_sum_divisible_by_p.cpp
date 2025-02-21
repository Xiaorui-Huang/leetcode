/*
 * @lc app=leetcode id=1590 lang=cpp
 *
 * [1590] Make Sum Divisible by P
 *
 * https://leetcode.com/problems/make-sum-divisible-by-p/description/
 *
 * algorithms
 * Medium (29.20%)
 * Likes:    2389
 * Dislikes: 165
 * Total Accepted:    137.8K
 * Total Submissions: 348.2K
 * Testcase Example:  '[3,1,4,2]\n6'
 *
 * Given an array of positive integers nums, remove the smallest subarray
 * (possibly empty) such that the sum of the remaining elements is divisible by
 * p. It is not allowed to remove the whole array.
 * 
 * Return the length of the smallest subarray that you need to remove, or -1 if
 * it's impossible.
 * 
 * A subarray is defined as a contiguous block of elements in the array.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [3,1,4,2], p = 6
 * Output: 1
 * Explanation: The sum of the elements in nums is 10, which is not divisible
 * by 6. We can remove the subarray [4], and the sum of the remaining elements
 * is 6, which is divisible by 6.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [6,3,5,2], p = 9
 * Output: 2
 * Explanation: We cannot remove a single element to get a sum divisible by 9.
 * The best way is to remove the subarray [5,2], leaving us with [6,3] with sum
 * 9.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3], p = 3
 * Output: 0
 * Explanation: Here the sum is 6. which is already divisible by 3. Thus we do
 * not need to remove anything.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * 1 <= p <= 10^9
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
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    int minSubarray(vector<int>& nums,  int p) {
        int n = nums.size();

        int total = 0;
        for(auto num: nums)
            total = (total + num) % p;

        int target = total % p;
        // cout << "total: " << total << endl;
        // cout << "target: " << target << endl;
        if(target == 0)
            return 0;

        // we need to find smallest subarray between i and j, such that 
        // (cur_sum_i - cur_sum_j) % p == target
        // cur_sum_j === (cur_sum_i - target) % p
        // cur_sum_j === (cur_sum_i - target + p) % p

        // we keep a map that keep tracks key: pre_sum % p, value: last index
        unordered_map<int, int> mod_map;
        mod_map[0] = -1; // make an edge case for the entire prefix needed to be removed (i - (-1) == i + 1 == len up to i)

        int cur_mod_sum = 0;
        int min_len = n;
        for(int i = 0; i < n; i++){
            cur_mod_sum = (cur_mod_sum + nums[i]) % p;
            int needed_mod = (cur_mod_sum - target + p) % p;

            // cout << "at i: " << i << " we need " << needed << endl;

            if(mod_map.find(needed_mod) != mod_map.end()){
                // cout << "we have found prev needed at " << mod_map[needed] << endl;
                min_len = min(min_len, i - mod_map[needed_mod]);
                // cout << "min_len is now: " <<  min_len << endl;
            }
            mod_map[cur_mod_sum] = i;
        }

        if(min_len == n)
            return -1;
        return min_len;
    }
};
// @lc code=end

