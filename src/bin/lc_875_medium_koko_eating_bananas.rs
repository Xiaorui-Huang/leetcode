/*
 * @lc app=leetcode id=875 lang=rust
 *
 * [875] Koko Eating Bananas
 *
 * https://leetcode.com/problems/koko-eating-bananas/description/
 *
 * algorithms
 * Medium (51.78%)
 * Likes:    6164
 * Dislikes: 299
 * Total Accepted:    279.8K
 * Total Submissions: 544.8K
 * Testcase Example:  '[3,6,7,11]\n8'
 *
 * Koko loves to eat bananas. There are n piles of bananas, the i^th pile has
 * piles[i] bananas. The guards have gone and will come back in h hours.
 *
 * Koko can decide her bananas-per-hour eating speed of k. Each hour, she
 * chooses some pile of bananas and eats k bananas from that pile. If the pile
 * has less than k bananas, she eats all of them instead and will not eat any
 * more bananas during this hour.
 *
 * Koko likes to eat slowly but still wants to finish eating all the bananas
 * before the guards return.
 *
 * Return the minimum integer k such that she can eat all the bananas within h
 * hours.
 *
 *
 * Example 1:
 *
 *
 * Input: piles = [3,6,7,11], h = 8
 * Output: 4
 *
 *
 * Example 2:
 *
 *
 * Input: piles = [30,11,23,4,20], h = 5
 * Output: 30
 *
 *
 * Example 3:
 *
 *
 * Input: piles = [30,11,23,4,20], h = 6
 * Output: 23
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= piles.length <= 10^4
 * piles.length <= h <= 10^9
 * 1 <= piles[i] <= 10^9
 *
 *
 */
struct Solution;

// @lc code=start
impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let can_finish_at_speed = |speed: i32| {
            let mut hours: i32 = 0;
            for pile in piles.iter() {
                hours += pile / speed;
                if pile % speed != 0 {
                    hours += 1;
                }
            }
            return hours <= h;
        };

        let mut lo = 1;
        let mut hi = *piles.iter().max().unwrap();
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if can_finish_at_speed(mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }

        return lo;
    }
}
// @lc code=end

fn main() {
    print!(
        "{}",
        Solution::min_eating_speed(
            vec![
                332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673,
                679580077, 337406589, 290818316, 877337160, 901728858, 679284947, 688210097,
                692137887, 718203285, 629455728, 941802184
            ],
            823855818
        )
    );
}
