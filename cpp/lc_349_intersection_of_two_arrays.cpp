/*
 * @lc app=leetcode id=349 lang=cpp
 *
 *
 * https://leetcode.com/problems/intersection-of-two-arrays/description/
 *
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any
order.



Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 */

#include <algorithm>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

#define DIRECT_MAP 0
#define HASH_SET 1

// #define APPROACH DIRECT_MAP
#define APPROACH HASH_SET

// there is also the sort and count method, but it is not theoretically efficient
// with O(nlogn + mlogm)

class Solution {
  public:
    vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
        vector<int> intersection;
#if APPROACH == DIRECT_MAP
        bool map[1000] = {false};
        for (auto &num : nums1)
            map[num] = true;

        for (auto num : nums2)
            if (map[num]) {
                intersection.push_back(num);
                map[num] = false; // take away the membership, it already exist
                                  // (avoids duplicates)
            }
#elif APPROACH == HASH_SET
        std::unordered_set<int> set;
        // always hash the smaller array
        if (nums1.size() > nums2.size())
            std::swap(nums1, nums2);

        for (auto &num : nums1)
            set.insert(num);

        for (auto &num : nums2) {
            if (set.count(num)) {
                intersection.push_back(num);
                set.erase(num);
            }
        }

#endif
        return intersection;
    }
};

// @lc code=end
