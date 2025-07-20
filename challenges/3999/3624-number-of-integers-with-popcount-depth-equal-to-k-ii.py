'''
3624-number-of-integers-with-popcount-depth-equal-to-k-ii
'''

from functools import cache
from typing import List


class Bit:
  def __init__(self, n: int):
    self.n = n
    self.bit = [0]*(n+1)

  def add(self, i: int, delta: int):
    i += 1
    while i <= self.n:
      self.bit[i] += delta
      i += i & -i

  def query(self, i: int) -> int:
    i += 1
    cnt = 0
    while i > 0:
      cnt += self.bit[i]
      i -= i & -i

    return cnt

  def range(self, l: int, r: int) -> int:
    if l > r:
      return 0

    return self.query(r) - (self.query(l-1) if l > 0 else 0)


@cache
def popcnt(val: int) -> int:
  return bin(val)[2:].count('1')


@cache
def depth(val: int) -> int:
  dep = 0
  while val > 1:
    val = popcnt(val)
    dep += 1

  return dep


class Solution:
  def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    max_depth = 5
    bits = [Bit(n) for _ in range(max_depth+1)]
    curr = [depth(val) for val in nums]

    for i, d in enumerate(curr):
      bits[d].add(i, 1)

    ans = []
    for q in queries:
      if q[0] == 1:
        _, l, r, k = q
        if k > max_depth:
          ans.append(0)
        else:
          ans.append(bits[k].range(l, r))

        continue

      _, idx, val = q
      old = curr[idx]
      bits[old].add(idx, -1)

      nums[idx] = val
      nxt = depth(val)
      curr[idx] = nxt
      bits[nxt].add(idx, 1)

    return ans
        