'''
4079-prime-subset-selection-i
'''

from bisect import bisect_right


top = 10**6 + 1
sv = list(range(top))
p = []
pf = []

for v0 in range(2, top):
  if sv[v0] < v0:
    continue

  p.append(v0)
  pf.append(v0 if not pf else pf[-1]+v0)

  for v1 in range(v0*v0, top, v0):
    sv[v1] = v0


class Solution:
  def maxPrimes(self, n: int, s: int) -> list[int]:
    i = bisect_right(p, n)-1
    if i < 0:
      return []

    cand = pf[:i+1]
    j = bisect_right(cand, s)-1
    # print('init:', [] if idx < 0 else p[:idx+1])
    if j < 0:
      return []

    return p[:j+1]
        