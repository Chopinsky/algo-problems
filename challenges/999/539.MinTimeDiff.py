'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".
'''

from typing import List
from collections import defaultdict
import math

class Solution:
  def findMinDifference(self, time: List[str]) -> int:
    def parse(t: str):
      arr = t.split(':')
      hr = int(arr[0]) * 60
      mm = int(arr[1])
      
      return hr + mm
    
    cand = sorted(parse(t) for t in time)
    day = parse('24:00')
    diff = cand[0] + (day - cand[-1])
    
    for i in range(1, len(cand)):
      d0 = cand[i] - cand[i-1]
      diff = min(diff, d0)
      
    return diff
        
  def findMinDifference(self, timePoints: List[str]) -> int:
    cnt = defaultdict(int)
    for t in timePoints:
      t_arr = t.split(':')
      ts = 60 * int(t_arr[0]) + int(t_arr[1])
      cnt[ts] += 1
      if cnt[ts] > 1:
        return 0
      
    times = sorted(cnt)
    diff = math.inf
    
    for i in range(1, len(times)):
      diff = min(diff, times[i]-times[i-1])
    
    if len(times) > 1:
      diff = min(diff, times[0]+1440-times[-1])
      
    return diff
    