#ifndef LC_2540_MINIMUM_COMMON_VALUE_H
#define LC_2540_MINIMUM_COMMON_VALUE_H
/*
 * @lc app=leetcode id=2540 lang=cpp
 *
 * [2540] Minimum Common Value
 *
 * https://leetcode.com/problems/minimum-common-value/description/
 *
 * Given two integer arrays `num1` and `num2`, sorted in non-decreasing order,
 * return the minimum integer common to both arrays. If there is no common
 * integer amongst `num1` and `num2`, return -1.
 *
 * Note that an integer is said to be common to nums1 and nums2 if both arrays
 * have at least one occurrence of that integer.
 *
 * Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2
is the smallest, so 2 is returned.

Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
 */

#include <algorithm>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S>
ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// not used because of complexity
/**
 * @brief Insert item into sorted vector
 *
 * @tparam T
 * @param vec the vector
 * @param item the item to be inserted
 * @return std::vector<T>::iterator at which the item is inserted
 */
template <typename T>
typename std::vector<T>::iterator insert_sorted(std::vector<T> &vec,
                                                T const &item) {
    return vec.insert(std::upper_bound(vec.begin(), vec.end(), item), item);
}
// @lc code=start
//

#define SLIDING_WINDOW 1
#define BINARY_SEARCH 2

// Then define APPROACH as one of the above
#define APPROACH BINARY_SEARCH
// #define APPROACH SLIDING_WINDOW

class Solution {
  public:
#if APPROACH == SLIDING_WINDOW
    int getCommon(vector<int> &nums1, vector<int> &nums2) {
        if (nums1.at(0) > nums2.at(0)) {
            std::swap(nums1, nums2);
        }
        size_t i = 0, j = 0;
        while (i < nums1.size() && j < nums2.size()) {
            if (nums1.at(i) == nums2.at(j))
                return nums1.at(i);

            if (nums1.at(i) < nums2.at(j))
                i++;
            else
                j++;
        }
        return -1;
    }
#elif APPROACH == BINARY_SEARCH
    int binary_search(vector<int> &nums, int target) {
        int low = 0, high = nums.size() - 1, mid;

        while (low <= high) {
            mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                return mid;
            }
            if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return -1;
    }
    int getCommon(vector<int> &nums1, vector<int> &nums2) {
        // always binary search the larger array - nums1
        if (nums1.size() < nums2.size())
            std::swap(nums1, nums2);

        for (auto &num : nums2) {
            if (binary_search(nums1, num) != -1)
                return num;
        }
        
        return -1;
    }
#endif
};

/* class Solution {
  public:
    vector<vector<int>> findWinners(vector<vector<int>> &matches) {
        std::unordered_map<int, int> records;
        vector<int> undefeated{}, lost_once{};
        for (auto &&match : matches) {
            auto &winner = match[0], &loser = match[1];
            if (records.find(winner) == records.end()) // not in records
                records[winner] = 0;

            if (records.find(loser) == records.end()) // not in records
                records[loser] = 0;
            records[loser]++;
        }
        for (auto &&record : records) {
            if (record.second == 0)
                undefeated.emplace_back(record.first);
            if (record.second == 1)
                lost_once.emplace_back(record.first);
        }
        sort(undefeated.begin(), undefeated.end());
        sort(lost_once.begin(), lost_once.end());
        return vector<vector<int>>{undefeated, lost_once};
    }
}; */
// @lc code=end

#endif
