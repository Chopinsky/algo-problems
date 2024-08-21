'''
3180. Maximum Total Reward Using Operations I
'''

from typing import List

class Solution:
  def maxTotalReward(self, values: List[int]) -> int:
    values.sort()
    curr = set([0])
    
    for val in values:
      nxt = set(val+v0 if v0 < val else 0 for v0 in curr )
      curr |= nxt
      # print(curr, nxt)
    
    return max(curr)
        