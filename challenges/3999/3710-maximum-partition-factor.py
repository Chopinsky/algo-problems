'''
3710-maximum-partition-factor
'''

from typing import List


class DSU:
  def __init__(self, n: int):
    self.rank = [0]*(n+1)
    self.parent = [i for i in range(n+1)]
    self.size = [0]*(n+1)

  def find(self, x: int) -> int:
    while self.parent[x] != x:
      x = self.parent[x]

    return x

  def union(self, x: int, y: int):
    px = self.find(x)
    py = self.find(y)

    if px == py:
      return

    if self.rank[px] < self.rank[py]:
      self.parent[px] = py
      return

    if self.rank[py] < self.rank[px]:
      self.parent[py] = px
      return

    self.parent[py] = px
    self.rank[px] += 1


class Solution:
  def maxPartitionFactor(self, points: List[List[int]]) -> int:
    n = len(points)
    if n == 2:
      return 0

    def dist(a: List, b: List) -> int:
      return abs(a[0]-b[0]) + abs(a[1]-b[1])

    dist = [(dist(points[i], points[j]), i, j) for i in range(n) for j in range(i+1, n)]
    dist.sort()

    p = [i for i in range(n)]
    wt = [1]*n
    opp = {}

    def find(x: int):
      if p[x] != x:
        p[x] = find(p[x])

      return p[x]

    def join(x: int, y: int):
      rx = find(x)
      ry = find(y)

      # swap to get into the right order
      if wt[rx] < wt[ry]:
        x, y = y, x

      wt[ry] += wt[rx]
      p[rx] = ry

    for d, i, j in dist:
      # this pair is in the same group, we're done,
      # can't get better results
      if find(i) == find(j):
        return d

      # add j to the opposite of i
      if i in opp:
        join(opp[i], j)

      # add i to the opposite of j
      if j in opp:
        join(opp[j], i)

      # init, add points in this pair
      # to the opposite side
      opp[i] = j
      opp[j] = i

    return dist[-1][0]


  def maxPartitionFactor0(self, points: List[List[int]]) -> int:
    l, r = 0, 10**9
    n = len(points)
    if n == 2:
      return 0

    def dist(a: List, b: List) -> int:
      return abs(a[0]-b[0]) + abs(a[1]-b[1])

    def is_valid(val: int) -> bool:
      d = DSU(2*n)

      for i in range(n):
        for j in range(i+1, n):
          if dist(points[i], points[j]) < val:
            d.union(i, j+n)
            d.union(i+n, j)

      for i in range(n):
        if d.find(i) == d.find(i+n):
          return False

      return True

    ans = 0
    while l <= r:
      mid = (l+r) // 2
      if is_valid(mid):
        ans = mid
        l = mid+1
      else:
        r = mid-1

    return ans

    
        