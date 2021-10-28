from typing import List, Set
from collections import defaultdict
from itertools import combinations
from functools import lru_cache


class Solution:
  def count_subtrees_dist(self, n: int, edges: List[List[int]]) -> List[int]:
    e = defaultdict(set)
    c = defaultdict(int)

    for u, v in edges:
      e[u].add(v)
      e[v].add(u)

      c[u] |= 1 << v
      c[v] |= 1 << u

    # print(e)
    dist = {}
    ans = [0] * (n-1)

    for i in range(1, n+1):
      stack, nxt = [i], []
      seen = set([i])
      d = 0

      while stack:
        d += 1

        for u in stack:
          for v in e[u]:
            if v in seen:
              continue

            seen.add(v)
            nxt.append(v)

            dist[i, v] = d
            dist[v, i] = d

        stack, nxt = nxt, stack
        nxt.clear()

    # print(dist)
    for l in range(2, n+1):
      for subset in combinations([i+1 for i in range(n)], l):
        base = 0
        for u in subset:
          base |= 1 << u

        complete = True
        for u in subset:
          if c[u] & base == 0:
            complete = False
            break

        # not a real subtree
        if not complete:
          continue

        l0 = len(subset)
        d = 0

        for i in range(l0-1):
          for j in range(i+1, l0):
            d = max(d, dist[subset[i], subset[j]])

        ans[d-1] += 1

    return ans


s = Solution()
t = [
  [4, [[1, 2], [2, 3], [2, 4]], [3, 4, 0]],
  [2, [[1, 2]], [1]],
  [3, [[1, 2], [2, 3]], [2, 1]]
]

for n, e, ans in t:
  print('\n========\nTest csae:', n, e)
  print('Expected:', ans)
  print('Gotten  :', s.count_subtrees_dist(n, e))
