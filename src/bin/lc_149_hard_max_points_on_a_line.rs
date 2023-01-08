/*
 * @lc app=leetcode id=149 lang=rust
 *
 * [149] Max Points on a Line
 *
 * https://leetcode.com/problems/max-points-on-a-line/description/
 *
 * algorithms
 * Hard (21.90%)
 * Likes:    1884
 * Dislikes: 272
 * Total Accepted:    268.4K
 * Total Submissions: 1.2M
 * Testcase Example:  '[[1,1],[2,2],[3,3]]'
 *
 * Given an array of points where points[i] = [xi, yi] represents a point on
 * the X-Y plane, return the maximum number of points that lie on the same
 * straight line.
 *
 *
 * Example 1:
 *
 *
 * Input: points = [[1,1],[2,2],[3,3]]
 * Output: 3
 *
 *
 * Example 2:
 *
 *
 * Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
 * Output: 4
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= points.length <= 300
 * points[i].length == 2
 * -10^4 <= xi, yi <= 10^4
 * All the points are unique.
 *
 *
 */

struct Solution;
// @lc code=start
use std::cmp::max;
use std::collections::HashMap;
impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i32 {
        let n = points.len();
        if n == 1 {
            return 1;
        }
        let mut res = 1;
        for i in 0..n {
            let (ax, ay) = (points[i][0], points[i][1]);
            let mut angle_counts: HashMap<u64, i32> = HashMap::new();
            for j in 0..n {
                let (bx, by) = (points[j][0], points[j][1]);
                if i != j {
                    let angle = ((by - ay) as f64).atan2((bx - ax) as f64);
                    angle_counts
                        // f64::to_bits as key will potentially have NaN and floats that should be the equal evaluate to not equal
                        // refer to leetcode rust solution for brain explosion (in all seriousness, probably safer floating point operations)
                        // https://stackoverflow.com/questions/39638363/how-can-i-use-a-hashmap-with-f64-as-key-in-rust
                        // https://stackoverflow.com/questions/63695874/why-does-transmuting-a-f64-into-u64-and-then-back-into-f64-result-in-a-different
                        .entry(angle.to_bits())
                        .and_modify(|count| *count += 1)
                        .or_insert(1);
                }
            }
            res = max(res, angle_counts.values().max().unwrap_or(&0) + 1);
        }
        return res;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case([[1, 1]].to_vec().iter().map(|x|x.to_vec()).collect(), 1)]
#[case([[1, 1], [4, 122]].to_vec().iter().map(|x|x.to_vec()).collect(), 2)]
#[case([[0, 0], [1, 0]].to_vec().iter().map(|x|x.to_vec()).collect(), 2)]
#[case([[0, 0], [0, 1], [0, -1]].to_vec().iter().map(|x|x.to_vec()).collect(), 3)]
#[case([[0, 0], [0, 1], [1, -1]].to_vec().iter().map(|x|x.to_vec()).collect(), 2)]
#[case([[1, 1], [2, 2], [3, 3]].to_vec().iter().map(|x|x.to_vec()).collect(), 3)]
#[case([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]].to_vec().iter().map(|x|x.to_vec()).collect(), 4)]
#[case([[1, 0], [1, 90], [1, -72], [-1, 1], [4, 0]].to_vec().iter().map(|x|x.to_vec()).collect(), 3)]
#[case([[2, 3], [3, 3], [-5, 3]].to_vec().iter().map(|x|x.to_vec()).collect(), 3)]
fn test_max_points(#[case] points: Vec<Vec<i32>>, #[case] expected: i32) {
    assert_eq!(Solution::max_points(points), expected);
}

fn main() {}
