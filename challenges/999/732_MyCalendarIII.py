'''
732. My Calendar III

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)

You are given some events [start, end), after each given event, return an integer k representing the maximum k-booking between all the previous events.

Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int start, int end) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.
 
Example 1:

Input
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1, The first event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(50, 60); // return 1, The second event can be booked and is disjoint, so the maximum k-booking is a 1-booking.
myCalendarThree.book(10, 40); // return 2, The third event [10, 40) intersects the first event, and the maximum k-booking is a 2-booking.
myCalendarThree.book(5, 15); // return 3, The remaining events cause the maximum K-booking to be only a 3-booking.
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3

Constraints:

0 <= start < end <= 10^9
At most 400 calls will be made to book.
'''

from collections import defaultdict


class MyCalendarThree(object):
  def __init__(self):
    self.seg = defaultdict(int)
    self.covered = defaultdict(int)


  def book(self, start, end):
    # idx -> current node; 2*idx -> left node; 2*idx+1 -> right node
    def update(s, e, l=0, r=10**9, idx=1):
      if r <= s or e <= l: 
        return 

      if s <= l < r <= e:
        self.seg[idx] += 1
        self.covered[idx] += 1
        
      else:
        m = (l + r) // 2
        ldx = 2*idx
        rdx = 2*idx + 1
        
        # update child segments
        update(s, e, l, m, ldx)
        update(s, e, m, r, rdx)
        
        # get the max intersections from the [l, r) segment represented by `idx`,
        # it equals the fully covered segments plus partial ones from the left tree
        # as well as the right tree
        self.seg[idx] = self.covered[idx] + max(self.seg[ldx], self.seg[rdx])

    update(start, end)
    return self.seg[1]


class MyCalendarThree:
  def __init__(self):
    self.store = defaultdict(int)
    

  def book(self, start: int, end: int) -> int:
    self.store[start] += 1
    self.store[end] -= 1
    booking = 1
    curr = 0
    
    for s in sorted(self.store):
      curr += self.store[s]
      booking = max(booking, curr)
    
    return booking


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)