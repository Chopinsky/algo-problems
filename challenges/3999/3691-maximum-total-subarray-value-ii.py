'''
3691-maximum-total-subarray-value-ii
'''

from typing import List
import math
from heapq import heappush, heappop


class SegTree:
  def __init__(self, arr: List, is_min: bool):
    self.n = len(arr)
    self.arr = arr
    self.is_min = is_min
    self.tree = [0] * (4*self.n + 1)
    self.build(1, 0, self.n-1)

  def choose(self, l: int, r: int):
    return min(l, r) if self.is_min else max(l, r)

  def build(self, idx: int, l: int, r: int):
    if l == r:
      self.tree[idx] = self.arr[l]
      return 

    mid = (l+r) // 2
    ldx = 2*idx
    rdx = 2*idx+1
    self.build(ldx, l, mid)
    self.build(rdx, mid+1, r)
    self.tree[idx] = self.choose(self.tree[ldx], self.tree[rdx])

  def query(self, idx: int, l:int, r: int, ql: int, qr: int):
    if ql > r or qr < l:
      return math.inf if self.is_min else -math.inf

    if ql <= l and r <= qr:
      return self.tree[idx]

    mid = (l+r) // 2
    lval = self.query(2*idx, l, mid, ql, qr)
    rval = self.query(2*idx+1, mid+1, r, ql, qr)

    return self.choose(lval, rval)

  def range_query(self, left: int, right: int):
    return self.query(1, 0, self.n-1, left, right)


class Solution:
  def maxTotalValue(self, nums: List[int], k: int) -> int:
    n = len(nums)
    max_tree = SegTree(nums, False)
    min_tree = SegTree(nums, True)
    h = []
    seen = set()

    max_val = max_tree.range_query(0, n-1)
    min_val = min_tree.range_query(0, n-1)
    heappush(h, (-(max_val-min_val), (0, n-1)))
    seen.add((0, n-1))
    ans = 0

    def update(l: int, r: int):
      if l > r or (l, r) in seen:
        return

      max_val = max_tree.range_query(l, r)
      min_val = min_tree.range_query(l, r)
      heappush(h, (-(max_val-min_val), (l, r)))
      seen.add((l, r))

    while h and k > 0:
      diff, (l, r) = heappop(h)
      diff = -diff
      ans += diff
      k -= 1

      update(l+1, r)
      update(l, r-1)

    return ans
