'''
2493. Divide Nodes Into the Maximum Number of Groups

You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

Example 1:

Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.

Constraints:

1 <= n <= 500
1 <= edges.length <= 10^4
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.
'''

from typing import List
from collections import defaultdict


class Solution:
  def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
    groups = 0
    e = defaultdict(list)
    seen = set()

    for u, v in edges:
      e[u].append(v)
      e[v].append(u)

    def dfs(u: int) -> List:
      group = []
      stack = [u]
      seen.add(u)

      while stack:
        u = stack.pop()
        group.append(u) 

        for v in e[u]:
          if v in seen:
            continue

          stack.append(v)
          seen.add(v)

      return group

    def bfs(u: int) -> int:
      curr, nxt = [u], []
      num = 1
      level = {u:num}
      # print('bfs:', u)

      while curr:
        num += 1
        # print('level:', curr, level)

        for u in curr:
          for v in e[u]:
            # print('reach:', (u, v), num, level.get(v, -1))
            if v in level:
              if abs(level[u]-level[v]) != 1:
                return -1

              continue

            level[v] = num
            nxt.append(v)

        curr, nxt = nxt, curr
        nxt.clear()

      return max(level.values())

    def find_groups(g: List) -> int:
      gc = 0
      for u in g:
        gc0 = bfs(u)
        if gc0 <= 0:
          continue

        gc = max(gc, gc0)
        # print('count:', g, gc)

      return gc

    for u in range(n):
      u += 1
      if u in seen:
        continue

      g = dfs(u)
      gc = find_groups(g)
      # print('group:', u, g, gc)

      if gc <= 0:
        return -1

      groups += gc

    return groups

  def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
    conn = defaultdict(set)
    for u, v in edges:
      conn[u].add(v)
      conn[v].add(u)
      
    def count_groups(root: int):
      if root not in conn:
        return 1, set([root])
        
      last, curr, nxt = set(), set([root]), set()
      groups = 0
      
      while curr:
        groups += 1
        
        for u in curr:
          # nodes in the same group can't be connected
          if u in nxt:
            # print('break 0:', root, groups, u)
            return -1, None
          
          addition = conn[u] - last
          if addition & curr:
            return -1, None
          
          nxt |= addition
          
        last |= curr
        curr, nxt = nxt, curr
        nxt.clear()
        
      return groups, last
      
    visited = set()
    cand = defaultdict(int)
    # print(cand)
    
    # for u in cand:
    for u in range(1, n+1):
      cnt, curr = count_groups(u)
      # print(u, cnt, len(conn[u]))
      
      if cnt > 0:
        idx = min(curr)
        cand[idx] = max(cand[idx], cnt)
        visited |= curr
    
    if len(visited) != n:
      return -1
    
    return sum(cand.values())
  