'''
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

Example 1:

Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:

Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.

Constraints:

1 <= n <= 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
'''

from typing import List
from collections import defaultdict


class Solution:
  def countPairs(self, n: int, edges: List[List[int]]) -> int:
    g = {i:i for i in range(n)}
    
    def find(x: int) -> int:
      while g[x] != x:
        x = g[x]
        
      return x
    
    def union(x: int, y: int) -> int:
      xr, yr = find(x), find(y)
      if xr <= yr:
        g[yr] = xr
      else:
        g[xr] = yr
        
    for u, v in sorted(edges):
      union(u, v)
      
    groups = defaultdict(int)
    for i in range(n):
      r = find(i)
      groups[r] += 1
      
    # print(groups)
    cnt = 0
    
    for c in groups.values():
      cnt += c * (n-c)
      
    return cnt // 2
    
    
  def countPairs(self, n: int, edges: List[List[int]]) -> int:
    seen = set()
    e = defaultdict(list)
    total = 0
    prev = 0
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
    
    def bfs(u: int) -> int:
      cnt = 1
      stack = [u]
      seen.add(u)
      
      while stack:
        v = stack.pop()
        for w in e[v]:
          if w in seen:
            continue
            
          stack.append(w)
          seen.add(w)
          cnt += 1
        
      return cnt
      
    for i in range(n):
      if i in seen:
        continue
        
      cnt = bfs(i)
      total += cnt * prev
      prev += cnt
      
    return total
    