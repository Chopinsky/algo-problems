'''
3440-reschedule-meetings-for-maximum-free-time-ii
'''

from typing import List


class Solution:
  def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
    meetings = list(zip(startTime, endTime))
    n = len(meetings)
    gaps = []

    for i in range(n):
      s, e = meetings[i]
      if i == 0:
        if s > 0:
          gaps.append((s, -1, 0))

      if i == n-1:
        if e < eventTime:
          gaps.append((eventTime-e, i, i+1)) 

      if i > 0:
        ps, pe = meetings[i-1]
        if pe < s:
          gaps.append((s-pe, i-1, i))

    gaps.sort()
    time = 0
    # print('init:', meetings, gaps)

    def can_reschedule(i: int) -> bool:
      s, e = meetings[i]
      ln = e-s
      j = len(gaps)-1
      count = 0

      while j >= 0 and count < 3:
        if gaps[j][0] < ln:
          return False

        if i != gaps[j][1] and i != gaps[j][2]:
          return True

        count += 1
        j -= 1 
      
      return False

    def free_time(i: int) -> int:
      if i == 0:
        s = 0
      else:
        s = meetings[i-1][1]

      if i == n-1:
        e = eventTime
      else:
        e = meetings[i+1][0]

      return e-s

    for i in range(len(meetings)):
      free = free_time(i)
      ln = meetings[i][1]-meetings[i][0]

      if can_reschedule(i):
        time = max(time, free)
      else:
        time = max(time, free-ln)

    return time
