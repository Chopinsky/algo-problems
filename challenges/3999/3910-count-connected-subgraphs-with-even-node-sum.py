'''
3910-count-connected-subgraphs-with-even-node-sum
'''


class DSU:
  def __init__(self, n: int):
    self.g = list(range(n))
    self.rank = [0]*n

  def find(self, x: int) -> int:
    if self.g[x] != x:
      self.g[x] = self.find(self.g[x])

    return self.g[x]

  def union(self, x: int, y: int):
    rx = self.find(x)
    ry = self.find(y)

    if rx == ry:
      return

    if self.rank[rx] < self.rank[ry]:
      self.g[rx] = ry
    elif self.rank[rx] > self.rank[ry]:
      self.g[ry] = rx
    else:
      self.g[ry] = rx
      self.rank[rx] += 1

class Solution:
  def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
    cand: list[int] = []  # contains all subgraph candidates
    n = len(nums)

    # build all subgraph candidates
    def dfs(i: int, curr: list[int]):
      cand.append(curr[:])
      for idx in range(i, n):
        curr.append(idx)
        dfs(idx+1, curr)
        curr.pop()

    dfs(0, [])
    count = 0
    # print('init:', cand)

    for sub in cand:
      if not sub:
        continue

      s = sum(nums[node] for node in sub)
      if s%2 == 1:
        # subgraph has odd sum, continue
        continue

      nodes = set[int](sub)
      d = DSU(n)

      for u, v in edges:
        # adding the edge+nodes
        if (u in nodes) and (v in nodes):
          d.union(u, v)

      roots = set[int]()
      for x in sub:
        roots.add(d.find(x))

      # a single connected group
      if len(roots) == 1:
        count += 1

    return count

        