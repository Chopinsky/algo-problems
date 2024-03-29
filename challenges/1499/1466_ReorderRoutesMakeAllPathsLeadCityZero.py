'''
1466. Reorder Routes to Make All Paths Lead to the City Zero

There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

Example 1:

Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
Output: 3
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 2:

Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
Output: 2
Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
Example 3:

Input: n = 3, connections = [[1,0],[2,0]]
Output: 0

Constraints:

2 <= n <= 5 * 10^4
connections.length == n - 1
connections[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
'''

from typing import List
from collections import defaultdict


class Solution:
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    curr, nxt = [0], []
    cnt = 0
    seen, conn = set(curr), set()
    e = defaultdict(set)
    
    for u, v in connections:
      e[u].add(v)
      e[v].add(u)
      conn.add((u, v))
    
    while curr:
      # print(curr)
      
      for u in curr:
        for v in e[u]:
          if v in seen:
            continue
            
          seen.add(v)
          nxt.append(v)
          # print('move:', v, u)
          
          if (v, u) not in conn:
            cnt += 1
      
      curr, nxt = nxt, curr
      nxt.clear()
      
    return cnt
    
    
  def minReorder(self, n: int, connections: List[List[int]]) -> int:
    conn = defaultdict(list)
    routes = defaultdict(set)
    
    for a, b in connections:
      routes[a].add(b)
      conn[a].append(b)
      conn[b].append(a)
      
    # print(routes, conn)
    changes = 0
    curr, nxt = [0], []
    visited = set(curr)

    while curr:
      # print(curr)
      for u in curr:
        for v in conn[u]:
          if v in visited:
            continue
            
          if u not in routes[v]:
            # print('reverse:', u, v)
            changes += 1
            
          nxt.append(v)
          visited.add(v)
      
      curr, nxt = nxt, curr
      nxt.clear()
      
    return changes
    