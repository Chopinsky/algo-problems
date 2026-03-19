'''
3296-minimum-number-of-seconds-to-make-mountain-height-zero
'''

from math import isqrt


class Solution:
  def minNumberOfSeconds(self, mountainHeight: int, workerTimes: list[int]) -> int:
    l, r = 1, 10**16

    def check(t: int) -> bool:
      h = 0
      for t0 in workerTimes:
        t1 = t // t0
        h0 = isqrt(2*t1)
        if h0*(h0+1) <= 2*t1:
          h += h0
        else:
          h += max(0, h0-1)

      # print('check:', t, h)
      return h >= mountainHeight

    while l <= r:
      mid = (l+r)//2
      if check(mid):
        r = mid-1
      else:
        l = mid+1

    return l
        