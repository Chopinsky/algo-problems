'''
3370-smallest-number-with-all-set-bits
'''


class Solution:
  def smallestNumber(self, n: int) -> int:
    val = 1
    while val < n:
      val <<= 1
      val |= 1

    return val
        