'''
2411-smallest-subarrays-with-maximum-bitwise-or
'''

from typing import List, Dict
from functools import lru_cache
from collections import defaultdict


class Solution:
  def smallestSubarrays(self, nums: List[int]) -> List[int]:
    n = len(nums)
    t = [0]*n
    curr = 0

    for i in range(n-1, -1, -1):
      curr |= nums[i]
      t[i] = curr

    def bits_to_val(b: Dict) -> int:
      val = 0
      for os, cnt in b.items():
        if cnt > 0:
          val |= 1 << os

      return val

    def update(b: Dict, val: int, delta: int) -> Dict:
      os = 0

      while val > 0:
        if val & 1:
          b[os] += delta

        val >>= 1
        os += 1

      return b

    # print('init:', t)
    bits = defaultdict(int)
    l, r = 0, 0
    res = []

    for l in range(n):
      if r < l:
        r = l
        bits.clear()

      if t[l] == 0:
        res.append(1)
        continue

      while r < n and bits_to_val(bits) != t[l]:
        bits = update(bits, nums[r], 1)
        r += 1

      res.append(r-l)
      # print('iter:', l, bits_to_val(bits), t[l], bits)
      update(bits, nums[l], -1)

    return res

  def smallestSubarrays(self, nums: List[int]) -> List[int]:
    n = len(nums)
    suffix = [0]*n
    
    @lru_cache(None)
    def get_bits(val):
      res = []
      idx = 0
      
      while val > 0:
        if val & 1 > 0:
          res.append(idx)
          
        val >>= 1
        idx += 1
        
      return res
    
    @lru_cache(None)
    def bits_to_val(bits):
      res = 0
      for idx in bits:
        res |= 1 << idx
        
      return res
    
    for i in range(n-1, -1, -1):
      if i == n-1:
        suffix[i] = nums[i]
      else:
        suffix[i] = nums[i] | suffix[i+1]
        
    ans = []
    l, r, curr = 0, 0, 0
    counter = defaultdict(int)
    # print(suffix)
    
    while l < n-1:
      while r < n and (r < l or curr < suffix[l]):
        for d in get_bits(nums[r]):
          counter[d] += 1
          
        curr |= nums[r]
        r += 1
        
      # print(l, r, curr, suffix[l])
      ans.append(max(1, r-l))
      
      for d in get_bits(nums[l]):
        counter[d] -= 1
        if counter[d] == 0:
          del counter[d]
          
      curr = bits_to_val(tuple(counter))
      l += 1
    
    ans.append(1)
    return ans
    