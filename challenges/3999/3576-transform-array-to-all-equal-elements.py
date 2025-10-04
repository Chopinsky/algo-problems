'''
3576-transform-array-to-all-equal-elements
'''

import math
from typing import List


class Solution:
  def canMakeEqual(self, nums: List[int], k: int) -> bool:
    n = len(nums)
    pos = [i for i in range(n) if nums[i] > 0]
    neg = [i for i in range(n) if nums[i] < 0]
    if not pos or not neg:
      return True

    if len(pos)%2 == 1 and len(neg)%2 == 1:
      return False

    # print('iter:', pos, neg)

    def count(arr: List) -> int:
      c = 0
      ln = len(arr)

      if ln%2 == 1:
        return math.inf

      for i in range(0, ln, 2):
        c += arr[i+1]-arr[i]

      return c
        
    if len(pos)%2 == 0 and count(pos) <= k:
      return True

    if len(neg)%2 == 0 and count(neg) <= k:
      return True

    return False
