/*
 * @lc app=leetcode id=1508 lang=c
 *
 * [1508] Range Sum of Sorted Subarray Sums
 *
 * https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/description/
 *
 * algorithms
 * Medium (58.38%)
 * Likes:    1495
 * Dislikes: 250
 * Total Accepted:    169.2K
 * Total Submissions: 267.5K
 * Testcase Example:  '[1,2,3,4]\n4\n1\n5'
 *
 * You are given the array nums consisting of n positive integers. You computed
 * the sum of all non-empty continuous subarrays from the array and then sorted
 * them in non-decreasing order, creating a new array of n * (n + 1) / 2
 * numbers.
 * 
 * Return the sum of the numbers from index left to index right (indexed from
 * 1), inclusive, in the new array. Since the answer can be a huge number
 * return it modulo 10^9 + 7.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
 * Output: 13 
 * Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. After
 * sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4,
 * 5, 6, 7, 9, 10]. The sum of the numbers from index le = 1 to ri = 5 is 1 + 2
 * + 3 + 3 + 4 = 13. 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [1,2,3,4], n = 4, left = 3, right = 4
 * Output: 6
 * Explanation: The given array is the same as example 1. We have the new array
 * [1, 2, 3, 3, 4, 5, 6, 7, 9, 10]. The sum of the numbers from index le = 3 to
 * ri = 4 is 3 + 3 = 6.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3,4], n = 4, left = 1, right = 10
 * Output: 50
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == nums.length
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= 100
 * 1 <= left <= right <= n * (n + 1) / 2
 * 
 * 
 */

#include "quick_sort.h"
#include <stdlib.h>
// @lc code=start

// quick sort
// void swap(int *a, int *b) {
//     int temp = *a;
//     *a = *b;
//     *b = temp;
// }

// int partition(int arr[], int low, int high) {
//     int pivot = arr[high];
//     int swap_idx = low;

//     for (int i = low; i < high; i++) {
//         if (arr[i] < pivot) {
//             swap(&arr[i], &arr[swap_idx++]);
//         }
//     }

//     swap(&arr[high], &arr[swap_idx]);
//     return swap_idx;
// }

// void quick_sort(int arr[], int low, int high) {
//     if (low >= high)
//         return;
//     int pivot_idx = partition(arr, low, high);

//     quick_sort(arr, low, pivot_idx - 1);
//     quick_sort(arr, pivot_idx + 1, high);
// }

QUICKSORT_IMPL(int)

int rangeSum(int *nums, int numsSize, int n, int left, int right) {
    int num_ele = n * (n + 1) / 2, count = 0, sum = 0;
    int *arr = (int *)malloc(sizeof(int) * num_ele);

    for (int i = 0; i < n; i++) {
        sum = 0;
        for (int j = i; j < n; j++) {
            sum += nums[j];
            arr[count++] = sum;
        }
    }

    // quick_sort(arr, 0, num_ele - 1);
    quick_sort_int(arr, 0, num_ele - 1);

    sum = 0;
    for (int i = left - 1; i < right; i++) {
        sum = (sum + arr[i]) % 1000000007;
    }
    return sum;
}
// @lc code=end
