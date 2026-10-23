'''
3984-divisible-game
'''

from collections import defaultdict


top = 10**6 + 1
sv = list(range(top))
p = []
fac = defaultdict(set)

for v0 in range(2, top):
  if sv[v0] < v0:
    continue

  p.append(v0)
  for v1 in range(v0, top, v0):
    sv[v1] = v0
    fac[v1].add(v0)


class Solution:
  def divisibleGame(self, nums: list[int]) -> int:
    cand = []
    n = len(nums)
    mod = 10**9 + 7

    if all(val == 1 for val in nums):
      return -2 % mod

    cand = set()
    for val in nums:
      cand |= fac[val]

    # print('pre:', cand)

    def calc(k: int) -> int:
      low = 0
      curr = 0
      best = -float('inf')

      for val in nums:
        if val%k == 0:
          curr += val
        else:
          curr -= val

        best = max(best, curr - low)
        low = min(low, curr)
        
      return best

    best = -float('inf')
    best_k = 2

    for k in sorted(cand):
      diff = calc(k)
      # print('iter:', k, diff)
      if diff > best:
        best = diff
        best_k = k

    return (best * best_k) % mod
        