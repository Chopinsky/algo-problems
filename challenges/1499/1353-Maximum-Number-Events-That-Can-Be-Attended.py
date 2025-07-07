'''
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
 

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= startDayi <= endDayi <= 10^5
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def maxEvents(self, events: List[List[int]]) -> int:
    d = 0
    cnt = 0
    cand = []
    events.sort()
    i = 0

    while i < len(events) or cand:
      while cand and cand[0] < d:
        heappop(cand)

      if not cand:
        if i >= len(events):
          break

        d = events[i][0]

      while i < len(events) and events[i][0] <= d:
        if events[i][1] >= d:
          heappush(cand, events[i][1])

        i += 1

      if cand:
        heappop(cand)
        cnt += 1

      d += 1
        
    return cnt


  '''
  the trick is to use each hour-based time-slot and try to match it with
  the event with the earliest ending time that's already happening
  '''
  def maxEvents(self, events: List[List[int]]) -> int:
    events.sort(reverse=True)
    stack = []
    count = 0
    top = 0
    # print(events)
    
    while events or stack:
      # no more prior events left to attend,
      # start fresh
      if not stack:
        top = events[-1][0]
        
      # add all events that happens before the current
      # top hour
      while events and events[-1][0] <= top:
        s, e = events.pop()
        heappush(stack, e)
      
      # attend the event with the earliest end hour
      if stack:
        heappop(stack)
        count += 1

      # now move to the next time-slot to attend an event
      top += 1
      
      # and remove all events that are no longer attendable
      # by the moving of the top hour
      while stack and stack[0] < top:
        heappop(stack)
          
    return count
    