'''
3315. Construct the Minimum Bitwise Array II
'''

from typing import List


class Solution:
  def minBitwiseArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    ans = []
    
    def find(prime: int) -> int:
      if prime % 2 == 0:
        return -1
      
      mask = 1
      while mask < prime:
        mask <<= 1
        
      if mask > prime:
        mask >>= 1
        
      # print('find:', bin(prime), bin(mask))
      while mask > 0:
        a = prime^mask
        b = a+1
        if a|b == prime:
          return a
        
        mask >>= 1
        
      return -1
    
    return [find(val) for val in nums]
        