'''
3985-palindromic-subarray-sum
'''

from typing import List
from itertools import accumulate


class Solution:
  def getSum(self, nums: List[int]) -> int:
    prefix = list(accumulate(nums, initial=0))
    
    def manacher(seq: list, sentinel = 0) -> list:
      s = [sentinel] * (2*len(seq) + 1)
      for i, val in enumerate(seq):
        s[2*i+1] = val

      n = len(s)
      p = [0]*n
      c = 0
      r = 0

      for i in range(n):
        if i < r:
          p[i] = min(r-i, p[2*c-i])

        while i-1-p[i] >= 0 and i+1+p[i] < n and s[i-1-p[i]] == s[i+1+p[i]]:
          p[i] += 1

        if i+p[i] > r:
          c, r = i, i+p[i]

      return p

    radius = manacher(nums)
    return max(prefix[(i+d)//2] - prefix[(i-d)//2] for i, d in enumerate(radius))
