'''
66-plus-one
'''

from typing import List


class Solution:
  def plusOne(self, d: List[int]) -> List[int]:
    n = len(d)
    carry = 1

    for i in range(n-1, -1, -1):
      d[i] += carry
      carry = 0

      if d[i] >= 10:
        d[i] %= 10
        carry = 1

    if carry > 0:
      d = [1] + d

    return d
        