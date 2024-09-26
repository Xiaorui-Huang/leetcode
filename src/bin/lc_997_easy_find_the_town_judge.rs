/*
 * @lc app=leetcode id=997 lang=rust
 *
 * [997] Find the Town Judge
 *
 * https://leetcode.com/problems/find-the-town-judge/description/
 *
 * algorithms
 * Easy (49.20%)
 * Likes:    4427
 * Dislikes: 336
 * Total Accepted:    337.2K
 * Total Submissions: 682.3K
 * Testcase Example:  '2\n[[1,2]]'
 *
 * In a town, there are n people labeled from 1 to n. There is a rumor that one
 * of these people is secretly the town judge.
 *
 * If the town judge exists, then:
 *
 *
 * The town judge trusts nobody.
 * Everybody (except for the town judge) trusts the town judge.
 * There is exactly one person that satisfies properties 1 and 2.
 *
 *
 * You are given an array trust where trust[i] = [ai, bi] representing that the
 * person labeled ai trusts the person labeled bi.
 *
 * Return the label of the town judge if the town judge exists and can be
 * identified, or return -1 otherwise.
 *
 *
 * Example 1:
 *
 *
 * Input: n = 2, trust = [[1,2]]
 * Output: 2
 *
 *
 * Example 2:
 *
 *
 * Input: n = 3, trust = [[1,3],[2,3]]
 * Output: 3
 *
 *
 * Example 3:
 *
 *
 * Input: n = 3, trust = [[1,3],[2,3],[3,1]]
 * Output: -1
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= n <= 1000
 * 0 <= trust.length <= 10^4
 * trust[i].length == 2
 * All the pairs of trust are unique.
 * ai != bi
 * 1 <= ai, bi <= n
 *
 *
 */

struct Solution;
// @lc code=start
use std::vec;
impl Solution {
    pub fn find_judge(n: i32, trusts: Vec<Vec<i32>>) -> i32 {
        let mut trusting = vec![0; n as usize];
        let mut trusted = vec![0; n as usize];

        for trust in trusts {
            let (a, b) = (trust[0] as usize - 1, trust[1] as usize - 1);
            trusting[a] += 1;
            trusted[b] += 1;
        }

        for (i, trust_info) in trusting.into_iter().zip(trusted).enumerate() {
            if trust_info == (0, n - 1) {
                return (i + 1) as i32;
            }
        }
        return -1;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(2, vec![vec![1,2]], 2)]
#[case(3, vec![vec![1,3], vec![2,3]], 3)]
#[case(3, vec![vec![1,3], vec![2,3], vec![3,1]], -1)]
fn test_find_judge(#[case] n: i32, #[case] trusts: Vec<Vec<i32>>, #[case] expected: i32) {
    assert_eq!(Solution::find_judge(n, trusts), expected);
}
fn main() {}
