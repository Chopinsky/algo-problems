'''
3590-kth-smallest-path-xor-sum
'''

from collections import Counter, defaultdict
from sortedcontainers import SortedList
from typing import List


class Solution:
  def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
    children = defaultdict(list)
    for i in range(len(par)):
      p = par[i]
      if p != -1:
        children[p].append(i)

    res = {}
    q = defaultdict(list)
    for i, k in queries:
      q[i].append(k)

    def merge(bsl, bc, ssl, sc):
      for val in ssl:
        freq = sc[val]
        if val not in bc:
          bsl.add(val)

        bc[val] += freq

    def dfs(i: int, above: int):
      curr = vals[i] ^ above
      bsl = SortedList()
      bc = Counter()

      for ch in children[i]:
        csl, cc = dfs(ch, curr)

        if len(csl) > len(bsl):
          bsl, csl = csl, bsl
          bc, cc = cc, bc

        merge(bsl, bc, csl, cc)

      bc[curr] += 1
      if bc[curr] == 1:
        bsl.add(curr)

      for k in q[i]:
        res[i, k] = bsl[k-1] if k-1 < len(bsl) else -1

      return bsl, bc

    dfs(0, 0)
    ans = []

    for i, k in queries:
      ans.append(res[i, k])

    return ans

        