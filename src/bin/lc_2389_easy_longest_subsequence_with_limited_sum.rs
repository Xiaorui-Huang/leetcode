/*
 * @lc app=leetcode id=2389 lang=rust
 *
 * [2389] Longest Subsequence With Limited Sum
 *
 * https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/
 *
 * algorithms
 * Easy (65.01%)
 * Likes:    613
 * Dislikes: 69
 * Total Accepted:    36K
 * Total Submissions: 53.1K
 * Testcase Example:  '[4,5,2,1]\n[3,10,21]'
 *
 * You are given an integer array nums of length n, and an integer array
 * queries of length m.
 * 
 * Return an array answer of length m where answer[i] is the maximum size of a
 * subsequence that you can take from nums such that the sum of its elements is
 * less than or equal to queries[i].
 * 
 * A subsequence is an array that can be derived from another array by deleting
 * some or no elements without changing the order of the remaining elements.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [4,5,2,1], queries = [3,10,21]
 * Output: [2,3,4]
 * Explanation: We answer the queries as follows:
 * - The subsequence [2,1] has a sum less than or equal to 3. It can be proven
 * that 2 is the maximum size of such a subsequence, so answer[0] = 2.
 * - The subsequence [4,5,1] has a sum less than or equal to 10. It can be
 * proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
 * - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be
 * proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [2,3,4,5], queries = [1]
 * Output: [0]
 * Explanation: The empty subsequence is the only subsequence that has a sum
 * less than or equal to 1, so answer[0] = 0.
 * 
 * 
 * Constraints:
 * 
 * 
 * n == nums.length
 * m == queries.length
 * 1 <= n, m <= 1000
 * 1 <= nums[i], queries[i] <= 10^6
 * 
 * 
 */

//use bisection::bisect_right as lib_bisect;
struct Solution;
// @lc code=start
impl Solution {
    pub fn answer_queries(nums: Vec<i32>, queries: Vec<i32>) -> Vec<i32> {
        let mut prefix_sum = nums;
        prefix_sum.sort();
        for i in 1..prefix_sum.len(){
            prefix_sum[i] += prefix_sum[i-1];
        }
        
        let bisect = |query: &i32|{
            let(mut lo, mut hi) = (0, prefix_sum.len());
            while lo < hi {
                let mid = (lo + hi) / 2;
                if &prefix_sum[mid] > query {
                    hi = mid
                } else {
                    lo = mid + 1
                }
            }
            lo as i32
        };

        return queries.iter().map(|query|bisect(query)).collect();
        //return queries.iter().map(|query|lib_bisect(& prefix_sum, query) as i32).collect();
    }

}
// @lc code=end

fn main(){
   let ans = Solution::answer_queries(vec![4,5,2,1], vec![3,10,21]);
   println!("{:?}", ans);
}