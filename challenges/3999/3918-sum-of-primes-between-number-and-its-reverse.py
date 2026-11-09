'''
3918-sum-of-primes-between-number-and-its-reverse
'''

from bisect import bisect_left, bisect_right


top = 1001
sv = list(range(top))
p = []
pf = []

for v0 in range(2, top):
  if sv[v0] < v0:
    continue

  p.append(v0)
  pf.append(v0 + (0 if not pf else pf[-1]))

  for v1 in range(v0*v0, top, v0):
    sv[v1] = v0


class Solution:
  def sumOfPrimesInRange(self, n: int) -> int:
    rev = int(str(n)[::-1])
    l = min(rev, n)
    r = max(rev, n)
    # print('init', l, r)

    ldx = bisect_left(p, l)
    rdx = bisect_right(p, r)-1
    # print('idx:', ldx, rdx, p[ldx:rdx+1] if ldx <= rdx else [])

    if ldx > rdx:
      return 0

    return pf[rdx] - (0 if ldx == 0 else pf[ldx-1])
        