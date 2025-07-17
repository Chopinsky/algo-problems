'''
3439-reschedule-meetings-for-maximum-free-time-i
'''

from typing import List


class Solution:
  def maxFreeTime(self, event: int, k: int, s: List[int], e: List[int]) -> int:
    n = len(s)
    if k >= n:
      meetings = sum(e[i]-s[i] for i in range(n))
      return event - meetings

    i = 0
    j = 0
    ln = 0

    while j < k and j < n:
      ln += e[j] - s[j]
      j += 1
    
    time = (s[j] if j < n else event) - ln
    # print('init:', ln, time)
    
    while j < n:
      ln += e[j] - s[j]
      ln -= e[i] - s[i]
      left = e[i]
      right = (s[j+1] if j+1 < n else event)
      time = max(time, right - left - ln)
      j += 1
      i += 1

    return time