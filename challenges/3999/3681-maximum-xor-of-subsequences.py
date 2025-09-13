'''
3681-maximum-xor-of-subsequences
'''

from typing import List


class Solution:
  def maxXorSubsequences(self, nums: List[int]) -> int:
    bs = []
    for val in nums:
      for b in bs:
        val = min(val , val^b)
      
      if val > 0:
        bs.append(val)
        bs.sort(reverse=True)

    maxVal = 0
    for b in bs:
      maxVal = max(maxVal , maxVal^b)

    return maxVal                
        
  def maxXorSubsequences(self, nums: List[int]) -> int:
    cand = sorted(set(nums))
    if not cand:
      return 0

    res = 0
    top = max(cand)

    while top > 0:
      res = max(res, res^top)
      for i in range(len(cand)):
        cand[i] = min(cand[i], cand[i]^top)

      top = max(cand)

    return res 
    
