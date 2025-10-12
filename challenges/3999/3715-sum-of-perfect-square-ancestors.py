'''
3715-sum-of-perfect-square-ancestors
'''

from typing import List
from collections import defaultdict


class Solution:
  def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
    g = defaultdict(list)
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    def kernel(x: int) -> int:
      res, f = 1, 2
      while f*f <= x:
        odd = 0
        while x%f == 0:
          x //= f
          odd ^= 1

        if odd:
          res *= f

        f += 1

      if x > 1:
        res *= x

      return res
        
    k = [kernel(x) for x in nums]
    freq = defaultdict(int)
    ans = 0

    def dfs(u: int, p: int):
      nonlocal ans
      ans += freq[k[u]]
      freq[k[u]] += 1
      
      for v in g[u]:
        if v != p:
          dfs(v, u)

      freq[k[u]] -= 1
      if freq[k[u]] == 0:
        del freq[k[u]]

    dfs(0, -1)

    return ans
