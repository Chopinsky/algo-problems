'''
3395. Subsequences with a Unique Middle Mode I

Test cases:

[1,1,1,1,1,1]
[1,2,2,3,3,4]
[0,1,2,3,4,5,6,7,8]
[0,1,-1,-1,-1]
'''

from typing import List, Dict
from collections import Counter
from math import comb


class Solution:
  def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
    mod = 10**9+7
    n = len(nums)
    cnt = 0
    lc = Counter(nums[:2])
    rc = Counter(nums[2:])
    
    def count_triplets(v0: int, d1: Dict, d2: Dict) -> int:
      pairs = 0
      slots = 0
      total = 0
      
      for v1, c1 in d2.items():
        if v1 == v0:
          continue
          
        slots += c1
        if c1 >= 2:
          pairs += comb(c1, 2)
        
      # pick any 2 from the right side, minus the same-number-pairs
      rc0 = comb(slots, 2) - pairs

      # picking v1 from one side, check how many unique (v2, v3) pairs 
      # we can pick up from the other side
      for v1, lc1 in d1.items():
        if v1 == v0:
          continue
        
        # minus the case where we picked 1 v1 and 1 other number 
        # from the right side
        rc_base = d2.get(v1, 0)
        rc1 = rc0 - max(0, rc_base*(slots-rc_base))
        total = (total + lc1*rc1) % mod
      
      return total
    
    def count_1s(i: int) -> int:
      val = nums[i]
      lc_val = lc.get(val, 0)
      rc_val = rc.get(val, 0)
      cnt = 0
      
      # distribute val with (left:1, right:0)
      if lc_val > 0:
        cnt = (cnt + lc_val*count_triplets(val, lc, rc)) % mod
      
      # distribute val with (left:0, right:1)
      if rc_val > 0:
        cnt = (cnt + rc_val*count_triplets(val, rc, lc)) % mod
      
      return cnt
    
    def count_2_and_3s(i: int) -> int:
      val = nums[i]
      cnt = 0
      
      for total in [2, 3]:
        for lc0 in [0, 1, 2]:
          rc0 = total - lc0
          if rc0 > 2:
            continue
          
          lc_val = lc.get(val, 0)
          rc_val = rc.get(val, 0)
          if lc0 > lc_val or rc0 > rc_val:
            continue

          lc1 = 2 - lc0
          lc2 = i - lc_val
          if lc1 > lc2:
            continue

          rc1 = 2 - rc0
          rc2 = (n-i-1) - rc_val
          if rc1 > rc2:
            continue

          lcnt = (comb(lc_val, lc0) * comb(lc2, lc1)) % mod
          rcnt = (comb(rc_val, rc0) * comb(rc2, rc1)) % mod
          cnt = (cnt + lcnt*rcnt) % mod
      
      return cnt % mod
    
    def count_4s(i: int) -> int:
      if lc.get(val, 0) < 2 or rc.get(val, 0) < 2:
        return 0
      
      return (comb(lc[val], 2) * comb(rc[val], 2)) % mod
    
    for i in range(2, n-2):
      # pop from the right counter
      val = nums[i]
      rc[val] -= 1
      
      # count with total number of val
      cnt = (cnt + count_1s(i) + count_2_and_3s(i) + count_4s(i)) % mod
      # print('iter:', val, count_1s(i), count_2_and_3s(i), count_4s(i))
      
      # add to the left counter
      lc[val] = lc.get(val, 0) + 1
      
    # print('end:', lc, rc)
    return cnt
    