'''
3264. Final Array State After K Multiplication Operations I
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def getFinalState(self, nums: List[int], k: int, mult: int) -> List[int]:
    cand = sorted([(val, i) for i, val in enumerate(nums)])
    # print('init:', cand)
    
    while k > 0:
      _, idx = heappop(cand)
      # print('pop:', idx, nums[idx])
      nums[idx] *= mult
      heappush(cand, (nums[idx], idx))
      k -= 1
    
    return nums
        