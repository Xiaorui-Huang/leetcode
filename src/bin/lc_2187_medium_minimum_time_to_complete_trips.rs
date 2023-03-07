/*
 * @lc app=leetcode id=2187 lang=rust
 *
 * [2187] Minimum Time to Complete Trips
 *
 * https://leetcode.com/problems/minimum-time-to-complete-trips/description/
 *
 * algorithms
 * Medium (32.16%)
 * Likes:    965
 * Dislikes: 60
 * Total Accepted:    35.3K
 * Total Submissions: 105.3K
 * Testcase Example:  '[1,2,3]\n5'
 *
 * You are given an array time where time[i] denotes the time taken by the i^th
 * bus to complete one trip.
 *
 * Each bus can make multiple trips successively; that is, the next trip can
 * start immediately after completing the current trip. Also, each bus operates
 * independently; that is, the trips of one bus do not influence the trips of
 * any other bus.
 *
 * You are also given an integer totalTrips, which denotes the number of trips
 * all buses should make in total. Return the minimum time required for all
 * buses to complete at least totalTrips trips.
 *
 *
 * Example 1:
 *
 *
 * Input: time = [1,2,3], totalTrips = 5
 * Output: 3
 * Explanation:
 * - At time t = 1, the number of trips completed by each bus are [1,0,0].
 * ⁠ The total number of trips completed is 1 + 0 + 0 = 1.
 * - At time t = 2, the number of trips completed by each bus are [2,1,0].
 * ⁠ The total number of trips completed is 2 + 1 + 0 = 3.
 * - At time t = 3, the number of trips completed by each bus are [3,1,1].
 * ⁠ The total number of trips completed is 3 + 1 + 1 = 5.
 * So the minimum time needed for all buses to complete at least 5 trips is
 * 3.
 *
 *
 * Example 2:
 *
 *
 * Input: time = [2], totalTrips = 1
 * Output: 2
 * Explanation:
 * There is only one bus, and it will complete its first trip at t = 2.
 * So the minimum time needed to complete 1 trip is 2.
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= time.length <= 10^5
 * 1 <= time[i], totalTrips <= 10^7
 *
 *
 */

struct Solution;
// @lc code=start
impl Solution {
    pub fn minimum_time(bus_trip_times: Vec<i32>, total_trips: i32) -> i64 {
        let can_complete_in_time = |time: i64| {
            let mut trips = 0;
            for &t in bus_trip_times.iter() {
                trips += time / t as i64;
                if trips >= total_trips as i64 {
                    return true;
                }
            }
            return false;
        };

        let mut low = 1;
        let mut high = *bus_trip_times.iter().min().unwrap() as i64 * total_trips as i64;
        while low < high {
            let mid = (low + high) / 2;
            if can_complete_in_time(mid) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }

        return high;
    }
}
// @lc code=end

use rstest::rstest;

#[rstest]
#[case(vec![10000], 10000000, 100000000000)]
fn test_min_time(
    #[case] bus_trip_times: Vec<i32>,
    #[case] total_trips: i32,
    #[case] expected: i64,
) {
    assert_eq!(
        Solution::minimum_time(bus_trip_times, total_trips),
        expected
    );
}
fn main() {}
