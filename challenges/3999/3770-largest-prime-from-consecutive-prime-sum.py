'''
3770-largest-prime-from-consecutive-prime-sum
'''

from bisect import bisect_right


mx = 500001
s = [val for val in range(mx)]
p = []

for v0 in range(2, mx):
  if s[v0] < v0:
    continue

  p.append(v0)
  for v1 in range(v0*v0, mx, v0):
    s[v1] = v0

curr = 0
pset = set(p)
cand = []

for val in p:
  curr += val
  if curr in pset:
    cand.append(curr)


class Solution:
  def largestPrime(self, n: int) -> int:
    idx = bisect_right(cand, n) - 1
    return cand[idx] if idx >= 0 else 0
        