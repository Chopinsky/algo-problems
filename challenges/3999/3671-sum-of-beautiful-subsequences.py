'''
3671-sum-of-beautiful-subsequences
'''

from typing import List
from collections import defaultdict


class Fenwick:
  def __init__(self, n: int):
    self.a = [0] * (n+1)

  def query(self, i: int) -> int:
    s = 0 if i > 0 else self.a[i]
    
    while i > 0:
      s += self.a[i]
      i -= i & -i

    return s

  def add(self, i: int, val: int):
    if i == 0:
      self.a[i] += val
      return

    while i < len(self.a):
      self.a[i] += val
      i += i & -i


class Solution:
  def totalBeauty(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    m = max(nums) + 1
    locs = defaultdict(list)

    for i, val in enumerate(nums):
      locs[val].append(i)

    f = [0]*m
    for d in range(1, m):
      indices = sorted(i for v in range(d, m, d) for i in locs[v])
      if len(indices) <= 1:
        f[d] = len(indices)
        continue

      rank = {pos: r for r, pos in enumerate(indices, 1)}
      fen = Fenwick(len(indices))
      
      for v in range(d, m, d):
        for pos in reversed(locs[v]):
          r = rank[pos]
          addend = 1 + fen.query(r-1)
          f[d] += addend
          fen.add(r, addend)

    for d in range(m-1, 0, -1):
      for e in range(2*d, m, d):
        f[d] -= f[e]

      f[d] %= mod

    return sum(d * f[d] for d in range(1, m)) % mod
