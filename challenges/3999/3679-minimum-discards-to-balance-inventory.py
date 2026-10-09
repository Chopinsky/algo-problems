'''
3679-minimum-discards-to-balance-inventory
'''

from typing import List
from collections import defaultdict


class Solution:
  def minArrivalsToDiscard(self, a: List[int], w: int, m: int) -> int:
    cnt = defaultdict(int)
    n = len(a)
    dc = set()

    for i in range(n):
      j = i-w
      if j >= 0 and j not in dc:
        cnt[a[j]] -= 1

      if a[i] not in cnt or cnt[a[i]]+1 <= m:
        cnt[a[i]] += 1
      else:
        dc.add(i)
        
    return len(dc)
