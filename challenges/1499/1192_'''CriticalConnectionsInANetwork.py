'''
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
'''

from typing import List
from collections import defaultdict


class Solution:
  def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
    if n == 2:
      return connections
    
    e = defaultdict(list)
    for u, v in connections:
      e[u].append(v)
      e[v].append(u)
    
    ans = []
    ranks = [-1] * n
    
    def dfs(u: int, p: int, depth: int) -> int:
      ranks[u] = depth
      
      for v in e[u]:
        # don't go back
        if v == p:
          continue
          
        # not visited yet, get the rank for node-v
        if ranks[v] < 0:
          ranks[v] = dfs(v, u, depth+1)
          
        # if ranks-v is larger in depth, there's no other 
        # shorter way to circle back to the root, hence
        # u-v edge is the only path leading back to the root.
        if depth < ranks[v]:
          ans.append((u, v))
          continue
        
        # if ranks-v makes a smaller rank number, update the
        # rank to the true depth since there's a different
        # route to go back to the root
        ranks[u] = min(ranks[u], ranks[v])
      
      return ranks[u]
    
    dfs(0, -1, 0)
    # print(ranks)
    
    return ans
  
        
