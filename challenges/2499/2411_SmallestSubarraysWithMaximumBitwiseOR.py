from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
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
    