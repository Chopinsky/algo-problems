'''
3733-minimum-time-to-complete-all-deliveries
'''

from typing import List
from math import gcd


class Solution:
  def minimumTime(self, d: List[int], r: List[int]) -> int:
    low = d[0] + d[1]
    high = 10 * low

    # Pre-calculate the LCM of the recharge intervals.
    # lcm(a, b) = (a * b) / gcd(a, b)
    lcm = (r[0]*r[1]) // gcd(r[0], r[1])

    def can_complete(time):
      # 1. Drone 1 capacity -- time minus down time
      slots1 = time - (time//r[0])
      
      # 2. Drone 2 capacity -- time minus down time
      slots2 = time - (time//r[1])
      
      # 3. Check total system capacity (accounting for shared recharge times)
      total_slots = time - (time//lcm)
      
      return (slots1 >= d[0]) and (slots2 >= d[1]) and (total_slots >= d[0]+d[1])

    # Binary search for the minimum time
    while low <= high:
      mid = (low + high) // 2
      if can_complete(mid):
        high = mid - 1
      else:
        low = mid + 1   # This time doesn't work, need more time
    
    return low
