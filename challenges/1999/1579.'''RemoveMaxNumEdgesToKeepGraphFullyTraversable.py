'''
Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

 

Example 1:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:

Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:

Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.

Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.
'''

from typing import List

class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    parents = [-1 for _ in range(n + 1)]

    res = 0
    res += self.update(edges, parents, 3)

    alice = parents.copy()
    res += self.update(edges, alice, 1)
        
    bob = parents.copy()
    res += self.update(edges, bob, 2)

    if not self.verify(alice[1:]) or not self.verify(bob[1:]):
      return -1

    return res
    
  def update(self, edges, p, num):
    count = 0
    
    for t, s, e in edges:
      if t != num:
        continue
        
      if self.find(s, p) == self.find(e, p):
        count += 1
        continue

      self.union(s, e, p)
      
    return count
    
  def verify(self, parents):
    count = 0
    for val in parents:
      if val < 0:
        count += 1
        
      if count > 1:
        return False
    
    return True

  def find(self, node, parents):
    while parents[node] >= 0:
      node = parents[node]
      
    return node

  def union(self, s, e, parents):
    fP = self.find(s, parents)
    if fP != s:
      parents[s] = fP

    sP = self.find(e, parents)
    if sP != e:
      parents[e] = sP

    if fP == sP:
      return

    if sP < fP:
      fP, sP = sP, fP

    parents[fP] += parents[sP]
    parents[sP] = fP

  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    a, b, c = set(), set(), set()
    an = [i for i in range(n+1)]
    bn = [i for i in range(n+1)]
    
    for e in edges:
      edge = tuple(e[1:])
      if e[0] == 3:
        c.add(edge)
      elif e[0] == 2 and edge not in c:
        b.add(edge)
      elif edge not in c:
        a.add(edge)

    def find(nodes: List[int], i: int) -> int:
      while nodes[i] != i:
        i = nodes[i]
        
      return i
    
    shared = 0
    a_cnt = 0
    b_cnt = 0
    groups = {i:set([i]) for i in range(1, n+1)}
    # print(len(c), len(a), len(b), len(edges))
    
    for u, v in c:
      ui, vi = find(an, u), find(an, v)
      if ui != vi:
        if ui <= vi:
          an[vi] = ui
          bn[vi] = ui
          groups[ui] |= groups[vi]
        else:
          an[ui] = vi
          bn[ui] = vi
          groups[vi] |= groups[ui]
          
        shared += 1

    ga = groups
    gb = groups.copy()
    
    for u, v in a:
      if u in ga[1] and v in ga[1]:
        continue
        
      if (u in ga[1] and v not in ga[1]) or (u not in ga[1] and v in ga[1]):
        a_cnt += 1
        if v not in ga[1]:
          ga[1] |= ga[find(an, v)]
        else:
          ga[1] |= ga[find(an, u)]
          
        continue
      
      ui, vi = find(an, u), find(an, v)
      if ui != vi:
        if ui <= vi:
          an[vi] = an[ui]
          ga[ui] |= ga[vi]
          ga.pop(vi, None)
        else:
          an[ui] = an[vi]
          ga[vi] |= ga[ui]
          ga.pop(ui, None)
          
        a_cnt += 1
    
    for u, v in b:
      if u in gb[1] and v in gb[1]:
        continue
        
      if (u in gb[1] and v not in gb[1]) or (u not in gb[1] and v in gb[1]):
        b_cnt += 1
        if v not in gb[1]:
          gb[1] |= gb[find(bn, v)]
        else:
          gb[1] |= gb[find(bn, u)]
          
        continue
      
      ui, vi = find(bn, u), find(bn, v)
      if ui != vi:
        # union(bn, u, v)
        if ui <= vi:
          bn[vi] = bn[ui]
          gb[ui] |= gb[vi]
        else:
          bn[ui] = bn[vi]
          gb[vi] |= gb[ui]
          
        b_cnt += 1
    
    # print(ga[1], gb[1])
    # print(len(edges), shared, a_cnt, b_cnt)
    # print(len(ga[1]|gb[1]))
    
    if len(ga[1]) != n or len(gb[1]) != n:
      return -1
    
    return len(edges) - shared - a_cnt - b_cnt
    