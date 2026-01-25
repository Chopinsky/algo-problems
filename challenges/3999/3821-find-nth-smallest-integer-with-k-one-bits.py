'''
3821-find-nth-smallest-integer-with-k-one-bits
'''

from math import comb


class Solution:
  def nthSmallest(self, n: int, k: int) -> int:
    res = 0

    for i in range(49, -1, -1):
      # found
      if k == 0:
        break

      # find total comb of digits: put remaining
      # k ones into i available slots, if keep
      # MSB to 1 (aka start from 50th to 1st bit)
      c = comb(i, k)

      # must set 1 at the (i+1) position, as it 
      # contains both 1/0 cases
      if n > c:
        res |= 1 << i
        n -= c
        k -= 1

    return res
        