'''
3309-maximum-possible-number-by-binary-concatenation
'''

from typing import List


class Solution:
  def maxGoodNumber(self, nums: List[int]) -> int:
    cand = [bin(val)[2:] for val in nums]
    n = len(nums)
    # print('init:', cand)

    for i in range(1, n):
      for j in range(i, 0, -1):
        if cand[j-1]+cand[j] >= cand[j]+cand[j-1]:
          break

        cand[j-1], cand[j] = cand[j], cand[j-1]
    
    base = "".join(cand)
    # print('sorted:', base, cand)

    val = 0
    mask = 1
    idx = len(base)-1

    while idx >= 0:
      if base[idx] == '1':
        val |= mask

      mask <<= 1
      idx -= 1

    return val