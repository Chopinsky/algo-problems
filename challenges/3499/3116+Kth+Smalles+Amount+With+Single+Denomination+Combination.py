from typing import List
from math import lcm
from itertools import combinations

class Solution:
  '''
  use the inclusion-exclusion principal to count the number of numbers that can be created with the
  combinations of the coins, then use the binary search to determine the number that will have exactly
  k-1 values smaller than it;

  the inclusion-exclusion principal uses the LCM or each combination to count the numbers that's the
  product of this LCM, aka the "double" counts, and remove/add it based on the combination level;
  '''
  def findKthSmallest(self, coins: List[int], k: int) -> int:
    coins.sort()
    cand = []
    
    def can_add(val):
      for v0 in cand:
        if val % v0 == 0:
          return False
        
      return True
    
    for v1 in coins:
      if can_add(v1):
        cand.append(v1)
          
    n = len(cand)
    combs = []
    
    # get the LCM of all the combinations at different combination level
    for cnt in range(n):
      mult = []
      for arr in combinations(cand, cnt+1):
        mult.append(lcm(*arr))
        
      combs.append(list(mult))
    
    def count(top: int):
      total = 0

      for i in range(n):
        sign = 1 if i % 2 == 0 else -1

        # update the counter of the numbers produced from the LCM of the sequence of the coins,
        # and add/substract the count from the total count based on the inclusion-exclusion principal
        for prod in combs[i]:
          total += sign * (top // prod)
          # print('update:', (i, sign), prod, top//prod)
        
      # print('count:', top, total)
      return total
    
    # print(cand, comb)
    l, r = cand[0], cand[-1]*k
    while l <= r:
      mid = (l+r) // 2
      if count(mid) >= k:
        r = mid - 1
      else:
        l = mid + 1
    
    return l
        