'''
3169. Count Days Without Meetings
'''

from typing import List


class Solution:
  def countDays(self, days: int, meetings: List[List[int]]) -> int:
    if not meetings:
      return days
    
    meetings.sort()
    count = 0
    prev = 0
    
    for i in range(len(meetings)):
      s, e = meetings[i]
      if s > prev:
        count += s-1-prev
        prev = e
      else:
        prev = max(prev, e)
        
    count += days-prev
    
    return count
  