'''
3658-gcd-of-odd-even-sums
'''

from math import gcd


o = []
e = []
so = 0
se = 0

for val in range(1, 2010):
  if val%2 == 0:
    se += val
    e.append(se)
  else:
    so += val
    o.append(so)


class Solution:
  def gcdOfOddEvenSums(self, n: int) -> int:
    # print('init:', o[n-1], e[n-1])
    return gcd(o[n-1], e[n-1])
        