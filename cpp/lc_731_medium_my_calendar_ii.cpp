/*
 * @lc app=leetcode id=731 lang=cpp
 *
 * [731] My Calendar II
 *
 * https://leetcode.com/problems/my-calendar-ii/description/
 *
 * algorithms
 * Medium (55.79%)
 * Likes:    1850
 * Dislikes: 154
 * Total Accepted:    116.4K
 * Total Submissions: 204.4K
 * Testcase Example:  '["MyCalendarTwo","book","book","book","book","book","book"]\n' +
  '[[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]'
 *
 * You are implementing a program to use as your calendar. We can add a new
 * event if adding the event will not cause a triple booking.
 * 
 * A triple booking happens when three events have some non-empty intersection
 * (i.e., some moment is common to all the three events.).
 * 
 * The event can be represented as a pair of integers start and end that
 * represents a booking on the half-open interval [start, end), the range of
 * real numbers x such that start <= x < end.
 * 
 * Implement the MyCalendarTwo class:
 * 
 * 
 * MyCalendarTwo() Initializes the calendar object.
 * boolean book(int start, int end) Returns true if the event can be added to
 * the calendar successfully without causing a triple booking. Otherwise,
 * return false and do not add the event to the calendar.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input
 * ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
 * [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
 * Output
 * [null, true, true, true, false, true, true]
 * 
 * Explanation
 * MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
 * myCalendarTwo.book(10, 20); // return True, The event can be booked. 
 * myCalendarTwo.book(50, 60); // return True, The event can be booked. 
 * myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
 * myCalendarTwo.book(5, 15);  // return False, The event cannot be booked,
 * because it would result in a triple booking.
 * myCalendarTwo.book(5, 10); // return True, The event can be booked, as it
 * does not use time 10 which is already double booked.
 * myCalendarTwo.book(25, 55); // return True, The event can be booked, as the
 * time in [25, 40) will be double booked with the third event, the time [40,
 * 50) will be single booked, and the time [50, 55) will be double booked with
 * the second event.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 0 <= start < end <= 10^9
 * At most 1000 calls will be made to book.
 * 
 * 
 */

#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <optional>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

// @lc code=start
class MyCalendarTwo {
  private:
    // Store the regular bookings and overlapping bookings
    vector<pair<int, int>> bookings;
    vector<pair<int, int>> overlapping_bookings;

  public:
    MyCalendarTwo() {}

    inline bool is_overlap(int s1, int e1, int s2, int e2) {
        return max(s1, s2) < min(e1, e2); // overlap exists if max(s1, s2) < min(e1, e2)
    }

    inline pair<int, int> get_overlap(int s1, int e1, int s2, int e2) {
        return {max(s1, s2), min(e1, e2)};
    }

    bool book(int start, int end) {
        // First, check if the new event overlaps with any double bookings (triple booking prevention)
        for (const auto &[overlap_start, overlap_end] : overlapping_bookings)
            if (is_overlap(start, end, overlap_start, overlap_end))
                return false; // Triple booking would occur

        // Then, check for overlaps with all existing regular bookings and record overlaps
        for (const auto &[booked_start, booked_end] : bookings)
            if (is_overlap(start, end, booked_start, booked_end))
                overlapping_bookings.push_back(get_overlap(start, end, booked_start, booked_end));

        bookings.push_back({start, end});
        return true;
    }
};

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo* obj = new MyCalendarTwo();
 * bool param_1 = obj->book(start,end);
 */
// @lc code=end
