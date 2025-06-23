'''
3594-minimum-time-to-transport-all-individuals
'''

from typing import List
from heapq import heappush, heappop
from itertools import combinations
from math import floor


class Solution:
  def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
    h = [(0.0, 0, 0, 0)]
    seen = dict()
    done = (1<<n) - 1

    while h:
      t, p, mask, j = heappop(h)
      state = (p, mask, j)

      # better solution exists
      if state in seen and seen[state] <= t:
        continue

      seen[state] = t

      # all people on the other side, done
      if mask == done and p == 1:
        return round(t, 5)

      # on the camp side
      if p == 0:
        camp = [i for i in range(n) if not (mask>>i) & 1]
        for r in range(1, min(k, len(camp))+1):
          # take r people from the remaining crowd
          for g in combinations(camp, r):
            cross_time = max(time[i] for i in g) * mul[j]
            nxt_j = (j + floor(cross_time)) % m
            nxt_mask = mask
            for i in g:
              nxt_mask |= 1 << i

            heappush(h, (t+cross_time, 1, nxt_mask, nxt_j))

        continue

      dst = [i for i in range(n) if (mask>>i) & 1]
      # take 1 person from to take the boat back
      for i in dst:
        cross_time = time[i] * mul[j]
        nxt_j = (j + floor(cross_time)) % m
        nxt_mask = mask ^ (1<<i)
        heappush(h, (t+cross_time, 0, nxt_mask, nxt_j))

    # can't be done
    return -1.0
        