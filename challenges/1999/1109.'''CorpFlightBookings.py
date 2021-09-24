'''
There are n flights that are labeled from 1 to n.

You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.

Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

Example 2:

Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

Constraints:

1 <= n <= 2 * 10 ^ 4
1 <= bookings.length <= 2 * 10 ^ 4
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 10 ^ 4
'''


from typing import List
from itertools import accumulate


class Solution:
  def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
    ans = [0] * (n+1)
    for s, e, c in bookings:
      ans[s-1] += c
      ans[e] -= c
      
    ans.pop()
    
    return list(accumulate(ans))
  
    
  def corpFlightBookings0(self, bookings: List[List[int]], n: int) -> List[int]:
    ans = [0] * n
    events = []
    
    for s, e, c in bookings:
      events.append((s, c))
      events.append((e+1, -c))
      
    events.sort(key=lambda x: x[0])
    curr, j = 0, 0
    # print(events)
    
    for i in range(1, n+1):
      while j < len(events) and events[j][0] == i:
        curr += events[j][1]
        j += 1
        
      ans[i-1] = curr
    
    return ans
  