'''
3765-complete-prime-number
'''

from math import isqrt


top = isqrt(10**9) + 1
p = set()
siev = [i for i in range(top)]

for v0 in range(2, top):
  if siev[v0] < v0:
    continue

  p.add(v0)
  for v1 in range(v0*v0, top, v0):
    siev[v1] = v0


class Solution:
  def completePrime(self, num: int) -> bool:
    # print('init:', len(p))
    base = str(num)
    n = len(base)

    def check(s: int) -> bool:
      # already a known prime
      if s in p:
        return True

      # all primes in [2, top) is known
      if s < top:
        return False

      for pval in p:
        if s%pval == 0:
          return False

      return True

    # check prefix
    for i in range(n):
      sub = int(base[:i+1])
      if not check(sub):
        return False

    # check suffix
    for i in range(n):
      sub = int(base[-i-1:])
      if not check(sub):
        return False

    return True
        
