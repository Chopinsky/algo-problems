'''
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)

Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.

Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
'''

from bisect import bisect_left, bisect_right


class MyCalendar:
  def __init__(self):
    self.start = []
    self.end = []
    self.cal = []

  def book(self, start: int, end: int) -> bool:
    if not self.start or start > self.end[-1]:
      self.start.append(start)
      self.end.append(end)
      return True
    
    if self.start and end <= self.start[0]:
      self.start = [start] + self.start
      self.end = [end] + self.end
      return True
      
    idx = bisect_right(self.start, start)
    if idx < len(self.start) and end > self.start[idx]:
      return False
    
    if idx > 0 and start < self.end[idx-1]:
      return False
    
    self.start.insert(idx, start)
    self.end.insert(idx, end)
    
    return True

  def book(self, start: int, end: int) -> bool:
    idx = bisect_left(self.cal, (start, ))
    if idx < len(self.cal) and self.cal[idx][0] < end:
      return False

    if idx > 0 and start < self.cal[idx-1][1]:
      return False

    self.cal.insert(idx, (start, end))

    return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
