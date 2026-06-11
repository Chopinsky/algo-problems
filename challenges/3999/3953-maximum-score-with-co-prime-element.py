'''
3953-maximum-score-with-co-prime-element
'''

from typing import List
from functools import cache


upper = 10**5
siev = list(range(upper+1))

for v0 in range(2, upper+1):
  if siev[v0] < v0:
    continue

  for v1 in range(v0*v0, upper+1, v0):
    siev[v1] = min(siev[v1], v0)


def get_primes(val: int):
  if val <= 3:
    return [val]

  p = set()
  while val > 1:
    p.add(siev[val])
    val //= siev[val]

  return sorted(p)


@cache
def get_subsets(val: int):
  p = get_primes(val)
  m = len(p)
  subs = [0] * (1<<m)

  for i in range(1<<m):
    v0 = 1
    for j in range(m):
      if i & (1<<j):
        v0 *= p[j]

    subs[i] = v0

  return subs


class Solution:
  def maxScore(self, nums: List[int], maxVal: int) -> int:
    mx = max(max(nums), maxVal) + 1

    freq = [0] * mx
    for x in nums:
      freq[x] += 1

    mults = freq.copy()
    for i in range(2, mx):
      for j in range(2*i, mx, i):
        mults[i] += freq[j]

    ans = 1 if freq[1] > 0 else 0
    for i in range(mx-1, 1, -1):
      if ans >= i:
        break

      subs = get_subsets(i)
      rem = -freq[i]

      for j in range(1, len(subs)):
        if j.bit_count() & 1:
          rem += mults[subs[j]]
        else:
          rem -= mults[subs[j]]

      if freq[i] > 0:
        cost = rem + freq[i] - 1
        ans = max(ans, i-cost)
      elif i <= maxVal:
        cost = rem if rem > 0 else 1
        ans = max(ans, i-cost)

    return ans
        