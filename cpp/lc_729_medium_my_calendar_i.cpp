/*
 * @lc app=leetcode id=729 lang=cpp
 *
 * [729] My Calendar I
 *
 * https://leetcode.com/problems/my-calendar-i/description/
 *
 * algorithms
 * Medium (56.59%)
 * Likes:    4580
 * Dislikes: 127
 * Total Accepted:    383K
 * Total Submissions: 657.7K
 * Testcase Example:  '["MyCalendar","book","book","book"]\n[[],[10,20],[15,25],[20,30]]'
 *
 * You are implementing a program to use as your calendar. We can add a new
 * event if adding the event will not cause a double booking.
 * 
 * A double booking happens when two events have some non-empty intersection
 * (i.e., some moment is common to both events.).
 * 
 * The event can be represented as a pair of integers start and end that
 * represents a booking on the half-open interval [start, end), the range of
 * real numbers x such that start <= x < end.
 * 
 * Implement the MyCalendar class:
 * 
 * 
 * MyCalendar() Initializes the calendar object.
 * boolean book(int start, int end) Returns true if the event can be added to
 * the calendar successfully without causing a double booking. Otherwise,
 * return false and do not add the event to the calendar.
 * 
 * 
 * 
 * Example 1:
 * 
 * 
 * Input
 * ["MyCalendar", "book", "book", "book"]
 * [[], [10, 20], [15, 25], [20, 30]]
 * Output
 * [null, true, false, true]
 * 
 * Explanation
 * MyCalendar myCalendar = new MyCalendar();
 * myCalendar.book(10, 20); // return True
 * myCalendar.book(15, 25); // return False, It can not be booked because time
 * 15 is already booked by another event.
 * myCalendar.book(20, 30); // return True, The event can be booked, as the
 * first event takes every time less than 20, but not including 20.
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

// @lc code=start

#include <set>
#include <utility>
using namespace std;

class MyCalendar {
  private:
    std::set<std::pair<int, int>> bookings;

  public:
    MyCalendar() {}

    bool book(int start, int end) {
        const pair<int, int> event{start, end};
        const auto next_event = bookings.lower_bound(event);
        if (next_event != bookings.end() && next_event->first < end) 
            return false;

        // check for out of bound when doing prev - this is the case when
        if (next_event != bookings.begin() && start < prev(next_event)->second)
            return false;

        bookings.insert(event);
        return true;
    };

    /**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
};
// @lc code=end
