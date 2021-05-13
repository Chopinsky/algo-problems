package challenges

import "sort"

/**
Implement a MyCalendarTwo class to store your events. A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection (ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true

Explanation:
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
*/

// MyCalendarTwo ...
type MyCalendarTwo struct {
	start []int
	end   []int
}

// MC2Constructor ...
func MC2Constructor() MyCalendarTwo {
	return MyCalendarTwo{
		start: make([]int, 0, 64),
		end:   make([]int, 0, 64),
	}
}

// Book ...
func (t *MyCalendarTwo) Book(start int, end int) bool {
	if len(t.start) == 0 {
		t.start = append(t.start, start)
		t.end = append(t.end, end)
		return true
	}

	var i, j, seg int

	for i < len(t.start) && end > t.start[i] {
		if t.start[i] < t.end[j] {
			seg++

			if seg == 2 && !(t.end[j] <= start || t.start[i] >= end) {
				return false
			}

			i++
		} else {
			seg--
			j++
		}
	}

	i = sort.SearchInts(t.start, start)
	j = sort.SearchInts(t.end, end)

	t.start = append(t.start, 0)
	t.end = append(t.end, 0)

	if i < len(t.start)-1 {
		copy(t.start[i+1:], t.start[i:])
	}

	if j < len(t.end)-1 {
		copy(t.end[j+1:], t.end[j:])
	}

	t.start[i] = start
	t.end[j] = end

	return true
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */
