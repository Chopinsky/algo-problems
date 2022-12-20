'''
2508. Add Edges to Make Degrees of All Nodes Even

There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.

You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return true if it is possible to make the degree of each node in the graph even, otherwise return false.

The degree of a node is the number of edges connected to it.

Example 1:

Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
Output: true
Explanation: The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.
Example 2:

Input: n = 4, edges = [[1,2],[3,4]]
Output: true
Explanation: The above diagram shows a valid way of adding two edges.
Example 3:

Input: n = 4, edges = [[1,2],[1,3],[1,4]]
Output: false
Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.

Constraints:

3 <= n <= 10^5
2 <= edges.length <= 10^5
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There are no repeated edges.
'''

from typing import List
from collections import defaultdict

class Solution:
  def isPossible(self, n: int, edges: List[List[int]]) -> bool:
    seen = set()
    count = defaultdict(int)
    
    for u, v in edges:
      seen.add((min(u, v), max(u, v)))
      count[u] += 1
      count[v] += 1
      
    cand = []
    for u, c in count.items():
      if c % 2 == 0:
        continue
        
      cand.append(u)
      
    n = len(cand)
    # print(cand, count)
    
    # no odd degrees
    if n == 0:
      return True
    
    # can't do it with at most 2 edges
    if n > 4 or n == 1 or n == 3:
      return False
    
    # just connect the 2 if possible, or create a triangle
    if n == 2:
      u, v = cand[0], cand[1]
      u, v = min(u, v), max(u, v)
      if (u, v) not in seen:
        return True
      
      for k in range(1, n+1):
        if k == u or k == v:
          continue
          
        e1 = (min(u, k), max(u, k))
        e2 = (min(v, k), max(v, k))
        
        if e1 not in seen and e2 not in seen:
          # print('use:', (u, v, k))
          return True
      
      return False
      
    # n == 4
    sol = [
      [(cand[0], cand[1]), (cand[2], cand[3])],
      [(cand[0], cand[2]), (cand[1], cand[3])],
      [(cand[0], cand[3]), (cand[1], cand[2])],
    ]
    
    for e1, e2 in sol:
      # print(e1, e2)
      a = (min(e1), max(e1))
      if a in seen:
        continue
        
      b = (min(e2), max(e2))
      if b in seen:
        continue
        
      return True
    
    return False
    