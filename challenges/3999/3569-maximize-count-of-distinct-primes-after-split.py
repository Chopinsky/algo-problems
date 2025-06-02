'''
3569-maximize-count-of-distinct-primes-after-split
'''

from heapq import heappush, heappop
from typing import List


MAXV = 10**5
is_prime = [False, False] + [True] * (MAXV - 1)

for i in range(2, int(MAXV**0.5) + 1):
  if is_prime[i]:
    for j in range(i*i, MAXV+1, i):
      is_prime[j] = False


class Solution:
  def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    # print('init:', len(prims))
    n = len(nums)
    heaps = {}

    def add(p: int, idx: int):
      if p not in heaps:
        heaps[p] = ([], [], set())

      minh, maxh, s = heaps[p]
      heappush(minh, idx)
      heappush(maxh, -idx)
      s.add(idx)

    def remove(p: int, idx: int):
      minh, maxh, s = heaps[p]
      s.discard(idx)

      while minh and minh[0] not in s:
        heappop(minh)

      while maxh and -maxh[0] not in s:
        heappop(maxh)

      if not s:
        del heaps[p]

    def bounds(p: int):
      minh, maxh, s = heaps[p]
      while minh and minh[0] not in s:
        heappop(minh)
      
      while maxh and -maxh[0] not in s:
        heappop(maxh)

      return minh[0], -maxh[0]

    size = 1
    while size < n+2:
      size <<= 1

    S = [0]*(2*size)
    M = [0]*(2*size)

    def point_add(pos: int, delta: int):
      i = pos + size
      S[i] += delta
      M[i] = max(S[i], 0)
      i //= 2

      while i:
        S[i] = S[2*i] + S[2*i+1]
        M[i] = max(M[2*i], S[2*i]+M[2*i+1])
        i //= 2

    def apply(f, l, delta):
      if f+1 <= l:
        point_add(f+1, delta)
        point_add(l+1, -delta)

    distinct = 0
    for i, v in enumerate(nums):
      if is_prime[v]:
        add(v, i)

    for p in list(heaps):
      f, l = bounds(p)
      apply(f, l, 1)
      distinct += 1

    ans = []
    for idx, val in queries:
      old = nums[idx]
      if is_prime[old]:
        f0, l0 = bounds(old)
        apply(f0, l0, -1)
        remove(old, idx)
        if old in heaps:
          f1, l1 = bounds(old)
          apply(f1, l1, 1)
        else:
          distinct -= 1

      if is_prime[val]:
        if val in heaps:
          f0, l0 = bounds(val)
          apply(f0, l0, -1)
          add(val, idx)
          f1, l1 = bounds(val)
          apply(f1, l1, 1)
        else:
          add(val, idx)
          distinct += 1

      nums[idx] = val
      ans.append(distinct + M[1])

    return ans
    