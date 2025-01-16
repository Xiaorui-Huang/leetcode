/*
 * @lc app=leetcode id=2425 lang=cpp
 *
 * [2425] Bitwise XOR of All Pairings
 *
 * https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/
 *
 * algorithms
 * Medium (58.22%)
 * Likes:    416
 * Dislikes: 14
 * Total Accepted:    22.5K
 * Total Submissions: 38.7K
 * Testcase Example:  '[2,1,3]\n[10,2,5,0]'
 *
 * You are given two 0-indexed arrays, nums1 and nums2, consisting of
 * non-negative integers. There exists another array, nums3, which contains the
 * bitwise XOR of all pairings of integers between nums1 and nums2 (every
 * integer in nums1 is paired with every integer in nums2 exactly once).
 * 
 * Return the bitwise XOR of all integers in nums3.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
 * Output: 13
 * Explanation:
 * A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
 * The bitwise XOR of all these numbers is 13, so we return 13.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,2], nums2 = [3,4]
 * Output: 0
 * Explanation:
 * All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^
 * nums2[1], nums1[1] ^ nums2[0],
 * and nums1[1] ^ nums2[1].
 * Thus, one possible nums3 array is [2,5,1,6].
 * 2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums1.length, nums2.length <= 10^5
 * 0 <= nums1[i], nums2[j] <= 10^9
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

// @lc code=start
class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int ans = 0;
        if(nums1.size() % 2 == 1)
            for(auto num: nums2)      
                ans ^= num;

        if(nums2.size() % 2 == 1)
            for(auto num: nums1)      
                ans ^= num;
        
        return ans;


        
        // original hash map idea
        // unordered_map<int, long> freq;
        
        // for(int num: nums1)
        //     freq[num] += n2;

        // for(int num: nums2)
        //     freq[num] += n1;
        
        // int ans = 0;
        // for(auto &[num, count]: freq)
        //     if(count% 2 == 1)
        //         ans ^= num;
        
        // return ans;
        
    }
};
// @lc code=end

