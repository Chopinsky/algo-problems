'''
3525-find-x-value-of-array-ii
'''

from typing import List, Tuple


class Tree:
  def __init__(self, nums: List[int], k: int):
    self.k = k
    self.n = len(nums)
    s = 1
    while s < self.n:
      s <<= 1

    self.s = s
    self.tree = [([0 for _ in range(k)], 1) for _ in range(2*s)]
    
    for i in range(self.n):
      vmod = nums[i] % k
      cnt = [0 for _ in range(k)]
      cnt[vmod] = 1
      prod = vmod
      self.tree[s+i] = (cnt, prod)

    for p in range(s-1, 0, -1):
      self.tree[p] = self.merge(self.tree[2*p], self.tree[2*p+1])

  def merge(self, lnode: Tuple, rnode: Tuple):
    c0, p0 = lnode
    c1, p1 = rnode
    k = self.k
    cnt = c0.copy()

    for val, c in enumerate(c1):
      if not c:
        continue

      vmod = (p0 * val) % k
      cnt[vmod] += c

    return cnt, (p0 * p1) % k

  def update(self, idx: int, val: int):
    pos = self.s + idx
    vmod = val % self.k
    cnt = [0]*self.k
    cnt[vmod] = 1
    prod = vmod
    self.tree[pos] = (cnt, prod)
    pos >>= 1

    while pos:
      self.tree[pos] = self.merge(self.tree[2*pos], self.tree[2*pos+1])
      pos >>= 1

  def query(self, l: int, r: int):
    l += self.s
    r += self.s
    c0, p0 = [0]*self.k, 1
    c1, p1 = [0]*self.k, 1

    while l < r:
      if l & 1:
        c0, p0 = self.merge((c0, p0), self.tree[l])
        l += 1

      if r & 1:
        r -= 1
        c1, p1 = self.merge(self.tree[r], (c1, p1))

      l >>= 1
      r >>= 1

    return self.merge((c0, p0), (c1, p1))


class Solution:
  def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
    tree = Tree(nums, k)
    res = []

    for idx, val, start, x in queries:
      tree.update(idx, val)
      cnt, _ = tree.query(start, len(nums))
      res.append(cnt[x])

    return res
        