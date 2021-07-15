from typing import List
from shared import print_output


class DSU:
  def __init__(self, n: int):
    # parent node's index, and count of edges
    self.p, self.e = list(range(n)), 0

  def find(self, x: int) -> int:
    # use union find to get the root parent node
    while x != self.p[x]:
      x = self.p[x]

    return x

  def union(self, x: int, y: int) -> int:
    rx, ry = self.find(x), self.find(y)
    if rx == ry:
      return 1

    if rx <= ry:
      self.p[ry] = rx
    else:
      self.p[rx] = ry

    self.e += 1
    return 0


class Solution:
  '''
  idea is to define 2 graphs: graph a is alice's graph, graph b is bob's graph,
  then we rebuild the graphs using type-3 + proper edges for each graph.

  The goal is to build a fully connected graphs a and b, then count how many
  we can discard during the building process.
  '''
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    a, b = DSU(n+1), DSU(n+1)
    ans = 0

    # add all type-3 edges to the 2 graphs
    for t, x, y in edges:
      if t != 3:
        continue

      # if the root node of x and the root node of y are identical, meaning 
      # we can ignore this type-3 edge already, add it to the final count. at
      # this point, graph a and b are identical, because both only use type-3
      # edges.
      ans += a.union(x, y)
      b.union(x, y)

    # add all non-type-3 edges to 2 graphs
    for t, x, y in edges:
      if t == 3:
        continue

      # choose the proper graph
      graph = a if t == 1 else b
      ans += graph.union(x, y)

    # the graph needs exactly n-1 edges to fully connect every nodes; otherwise,
    # we can't build the graphs in concern.
    return ans if b.e == n-1 and a.e == n-1 else -1

s = Solution()
t = [
  [
    4, 
    [
      [3,1,2],
      [3,2,3],
      [1,1,3],
      [1,2,4],
      [1,1,2],
      [2,3,4],
    ],
    2,
  ],
  [
    4,
    [
      [3,2,3],
      [1,1,2],
      [2,3,4],
    ],
    -1,
  ]
]

for [n, e, output] in t:
  ans = s.maxNumEdgesToRemove(n, e)
  print_output(output, ans)
