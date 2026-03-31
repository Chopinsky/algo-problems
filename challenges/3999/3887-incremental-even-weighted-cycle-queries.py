'''
3887-incremental-even-weighted-cycle-queries
'''

from typing import List


class Solution:
  def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
    p = [i for i in range(n)]
    size = [1]*n
    parity = [0]*n

    def find(x: int):
      # is root
      if p[x] == x:
        return x, 0

      # find the real root
      root, par = find(p[x])

      # lazy updates
      p[x] = root
      parity[x] ^= par

      return p[x], parity[x]

    def union(u: int, v: int, w: int) -> bool:
      pu, xu = find(u)
      pv, xv = find(v)

      # same root, check parity
      if pu == pv:
        return (xu^xv == w)

      # union
      if size[pu] < size[pv]:
        pu, pv = pv, pu
        xu, xv = xv, xu

      p[pv] = pu
      size[pu] += size[pv]

      # update parity, must stay consistent from u-> pu, v-> pv
      parity[pv] = xu^xv^w

      return True

    count = 0
    for u, v, w in edges:
      if union(u, v, w):
        count += 1

    return count

