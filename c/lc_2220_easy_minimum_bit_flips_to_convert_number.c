/*
 * @lc app=leetcode id=2220 lang=c
 *
 * [2220] Minimum Bit Flips to Convert Number
 *
 * https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/
 *
 * algorithms
 * Easy (85.45%)
 * Likes:    994
 * Dislikes: 22
 * Total Accepted:    123.9K
 * Total Submissions: 143.9K
 * Testcase Example:  '10\n7'
 *
 * A bit flip of a number x is choosing a bit in the binary representation of x
 * and flipping it from either 0 to 1 or 1 to 0.
 * 
 * 
 * For example, for x = 7, the binary representation is 111 and we may choose
 * any bit (including any leading zeros not shown) and flip it. We can flip the
 * first bit from the right to get 110, flip the second bit from the right to
 * get 101, flip the fifth bit from the right (a leading zero) to get 10111,
 * etc.
 * 
 * 
 * Given two integers start and goal, return the minimum number of bit flips to
 * convert start to goal.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: start = 10, goal = 7
 * Output: 3
 * Explanation: The binary representation of 10 and 7 are 1010 and 0111
 * respectively. We can convert 10 to 7 in 3 steps:
 * - Flip the first bit from the right: 1010 -> 1011.
 * - Flip the third bit from the right: 1011 -> 1111.
 * - Flip the fourth bit from the right: 1111 -> 0111.
 * It can be shown we cannot convert 10 to 7 in less than 3 steps. Hence, we
 * return 3.
 * 
 * Example 2:
 * 
 * 
 * Input: start = 3, goal = 4
 * Output: 3
 * Explanation: The binary representation of 3 and 4 are 011 and 100
 * respectively. We can convert 3 to 4 in 3 steps:
 * - Flip the first bit from the right: 011 -> 010.
 * - Flip the second bit from the right: 010 -> 000.
 * - Flip the third bit from the right: 000 -> 100.
 * It can be shown we cannot convert 3 to 4 in less than 3 steps. Hence, we
 * return 3.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= start, goal <= 10^9
 * 
 * 
 */

#include <stdio.h>


// @lc code=start
int count_bits_standard(int num){
    int count = 0;
    while(num){
        count += num & 1; // see last bit is 1 or not
        num >>= 1; // right shift it out
    } 
    return count;
}

int count_bits_Brian_Kernighan(int num){
    int count = 0;
    while(num){
        num &= num - 1; // this clears the rightmost bit 
                        // * num - 1 flips all bits after the rightmost bit (including the rightmost bit)
                        // & the two num, then clears the rightmost bit.
                        // therefore the loop only runs number-of-bits times
        count++;
    }
    return count;

}
int minBitFlips(int start, int goal) {
    // return __builtin_popcount(start ^ goal); // GCC Built-in Function
    // return count_bits_standard(start ^ goal);
    return count_bits_Brian_Kernighan(start ^ goal);
}
// @lc code=end

