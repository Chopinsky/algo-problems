'''
2492. Minimum Score of a Path Between Two Cities

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.

Example 1:

Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:

Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.

Constraints:

2 <= n <= 10^5
1 <= roads.length <= 10^5
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 10^4
There are no repeated edges.
There is at least one path between 1 and n.
'''

from typing import List
from collections import defaultdict
import math


class Solution:
  def minScore(self, n: int, roads: List[List[int]]) -> int:
    md = {1:math.inf, n:math.inf}
    curr, nxt = set([1]), set()
    conn = defaultdict(list)
    
    for u, v, d in roads:
      u, v = min(u, v), max(u, v)
      conn[u].append((v, d))
      conn[v].append((u, d))
    
    # print(conn)
    while curr:
      for u in curr:
        d0 = md[u]
        for v, d1 in conn[u]:
          dd = min(d0, d1)
          if (v not in md) or (dd < md[v]):
            md[v] = dd
            nxt.add(v)
        
      # print(curr, nxt, md)
      curr, nxt = nxt, curr
      nxt.clear()
      
    return md[n]
    

  def minScore(self, n: int, roads: List[List[int]]) -> int:
    group = [i for i in range(n+1)]
    dist = [math.inf] * (n+1)
    
    def find(x: int):
      while group[x] != x:
        x = group[x]
        
      return x
    
    def union(x: int, y: int):
      rx, ry = find(x), find(y)
      if rx <= ry:
        group[ry] = rx
        return rx
      
      group[rx] = ry
      return ry
        
    for u, v, d in roads:
      root = union(u, v)
      dist[root] = min(dist[root], d)
      
    d = dist[1]
    for u in range(1, n+1):
      if find(u) == 1:
        d = min(d, dist[u])
    
    return d
    
    