'''
3419-minimize-the-maximum-edge-weight-of-graph
'''

from typing import List
from heapq import heappush, heappop
from collections import defaultdict


class Solution:
  def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
    res = 0
    graph = [[] for i in range(n)]

    for i, e in enumerate(edges):
      graph[e[1]].append((e[0], e[2]))

    q = [(0, 0)]
    seen = [False]*n

    while q and n:
      # pulling the lowest weight to 
      # reach node-u from 0
      w, u = heappop(q)

      # better weight edge is already 
      # added, continue
      if seen[u]:
        continue

      seen[u] = True
      res = max(res, w)
      n -= 1

      for v, w in graph[u]:
        if seen[v]:
          continue

        # push the lowest weight of
        # u <- v edge into the stack
        heappush(q, (w, v))

    return res if all(seen) else -1

  def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
    src = defaultdict(list)
    edges.sort()
    l, h = 0, 0
    debug = False

    for u, v, w in edges:
      if src[u] and src[u][-1][0] == v:
        continue

      src[u].append((v, w))
      h = max(h, w)

    if debug:
      print('init:', src, (l, h))

    def build(wt: int):
      g = defaultdict(list)
      if not wt:
        return g

      for u, lst in src.items():
        for v, w in lst:
          if w > wt:
            continue

          # reverse graph
          g[v].append(u)

      return g

    def check(g) -> bool:
      if not g:
        return False

      curr = [0]
      nxt = []
      seen = set(curr)
      cnt = [0]*n

      while curr:
        for u in curr:
          for v in g[u]:
            if v in seen:
              continue

            cnt[v] += 1
            if cnt[v] > threshold:
              # return False
              continue

            nxt.append(v)
            seen.add(v)

        curr, nxt = nxt, curr
        nxt.clear()

      if debug:
        print('iter-done:', seen)
        
      return len(seen) == n
        
    last = -1

    while l <= h:
      mid = (l+h) // 2
      graph = build(mid)
      if debug:
        print('iter:', mid, graph)

      if check(graph):
        h = mid-1
        last = mid
      else:
        l = mid+1

    return last
