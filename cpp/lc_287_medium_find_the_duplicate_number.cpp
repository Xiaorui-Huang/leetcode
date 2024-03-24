/*
 * @lc app=leetcode id=287 lang=cpp
 *
 * [287] Find the Duplicate Number
 *
 * https://leetcode.com/problems/find-the-duplicate-number/description/
 *
 * algorithms
 * Medium (59.50%)
 * Likes:    22823
 * Dislikes: 4305
 * Total Accepted:    1.7M
 * Total Submissions: 2.7M
 * Testcase Example:  '[1,3,4,2,2]'
 *
 * Given an array of integers nums containing n + 1 integers where each integer
 * is in the range [1, n] inclusive.
 * 
 * There is only one repeated number in nums, return this repeated number.
 * 
 * You must solve the problem without modifying the array nums and uses only
 * constant extra space.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,3,4,2,2]
 * Output: 2
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,1,3,4,2]
 * Output: 3
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [3,3,3,3,3]
 * Output: 3
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10^5
 * nums.length == n + 1
 * 1 <= nums[i] <= n
 * All the integers in nums appear only once except for precisely one integer
 * which appears two or more times.
 * 
 * 
 * 
 * Follow up:
 * 
 * 
 * How can we prove that at least one duplicate number must exist in nums?
 * Can you solve the problem in linear runtime complexity?
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
    int findDuplicate(vector<int>& nums) {
        int slow = 0;
        int fast = 0;
        do {
            slow = nums[slow];
            fast = nums[nums[fast]];
        } while (slow != fast);

        /*
         * First Meeting
         * Slow and fast pointers will eventually meet inside the cycle due to the nature of their movement speeds. Let's denote the start of the cycle as point S, and the first meeting point as point M.
         * Let the distance from the start of the list to the start of the cycle (0 to S) be d. The distance from the start of the cycle to the meeting point (S to M) be p, and the length of the cycle be c.
         * When they meet, slow has traveled d + p, and fast has traveled d + p + n*c for some integer n, having gone around the cycle n times more than slow.
         *
         * Since fast is twice as fast as slow, we can write the distance
         * traveled by fast as 2(d + p) = d + p + n*c. Simplifying this, we get d
         * + p = n*c, which means 
         * 
         * Therefore: d is a multiple of the cycle length c minus p.
         *
         * Second Loop
         * After the first meeting, the slow pointer is set back to the start of
         * the list, and both pointers now move one step at a time.
         *
         * The crucial insight is that the distance from the start of the list
         * to the start of the cycle d is the same as the distance from the
         * meeting point M around the cycle back to the start of the cycle S.
         * This is because d = n*c - p.
         *
         * Hence, if both start moving one step at a time, the slow pointer,
         * starting at 0, and the fast pointer, starting at M, will both have to
         * travel d steps to meet at the start of the cycle S.
         *
         * This is why they will meet at the cycle's entry if they move at the
         * same pace, proving that the second loop will indeed cause them to
         * meet at the duplicate number (or the cycle's start).
         */
            
        slow = 0;
        while (slow != fast) {
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
    }
};

// @lc code=end

