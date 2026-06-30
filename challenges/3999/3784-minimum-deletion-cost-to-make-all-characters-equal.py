'''
3784-minimum-deletion-cost-to-make-all-characters-equal
'''

from typing import List
from collections import defaultdict
from math import inf


class Solution:
  def minCost(self, s: str, cost: List[int]) -> int:
    total = 0
    cnt = defaultdict(int)
    n = len(s)

    for i in range(n):
      ch = s[i]
      c = cost[i]
      
      total += c
      cnt[ch] += c

    # print('init:', total, cnt)
    if len(cnt) == 1:
      # nothing to delete
      return 0
    
    min_cost = inf
    for c in cnt.values():
      min_cost = min(min_cost, total-c)

    return min_cost
        