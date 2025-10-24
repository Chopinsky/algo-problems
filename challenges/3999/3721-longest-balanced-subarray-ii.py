'''
3721-longest-balanced-subarray-ii
'''

from typing import List
from collections import defaultdict


class Tree:
  def __init__(self, n: int):
    self.n = n
    self.min_tree = [0] * (4*n)
    self.max_tree = [0] * (4*n)
    self.lazy = [0] * (4*n)

  def push(self, u: int, l: int, r: int):
    if self.lazy[u] != 0:
      self.min_tree[u] += self.lazy[u]
      self.max_tree[u] += self.lazy[u]
      if l != r:
        self.lazy[2*u] += self.lazy[u]
        self.lazy[2*u+1] += self.lazy[u]

      self.lazy[u] = 0

  def update(self, u: int, l: int, r: int, ll: int, rr: int, val: int):
    self.push(u, l, r)
    if l > r or l > rr or r < ll:
      return

    if ll <= l and r <= rr:
      self.lazy[u] += val
      self.push(u, l, r)
      return

    mid = (l+r) // 2
    self.update(2*u, l, mid, ll, rr, val)
    self.update(2*u+1, mid+1, r, ll, rr, val)
    self.min_tree[u] = min(self.min_tree[2*u], self.min_tree[2*u+1])
    self.max_tree[u] = max(self.max_tree[2*u], self.max_tree[2*u+1])

  def find_left(self, u: int, l: int, r: int):
    self.push(u, l, r)
    if self.min_tree[u] > 0 or self.max_tree[u] < 0:
      return -1

    if l == r:
      return l if self.min_tree[u] == 0 else -1

    mid = (l+r) // 2
    left = self.find_left(2*u, l, mid)
    if left != -1:
      return left

    return self.find_left(2*u+1, mid+1, r)


class Solution:
  def longestBalanced(self, nums: List[int]) -> int:
    n = len(nums)
    prev = defaultdict(lambda: -1)
    t = Tree(n)
    res = 0
    
    for r in range(n):
      v = nums[r]
      val = 1 if v%2 == 0 else -1

      if prev[v] != -1:
        t.update(1, 0, n-1, 0, prev[v], -val)

      t.update(1, 0, n-1, 0, r, val)
      prev[v] = r
      l = t.find_left(1, 0, n-1)

      if l != -1 and l <= r:
        res = max(res, r-l+1)

    return res
        