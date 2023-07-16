'''
1319. Number of Operations to Make Network Connected

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.

Example 1:

Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.

Constraints:

1 <= n <= 10^5
1 <= connections.length <= min(n * (n - 1) / 2, 10^5)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
'''

from typing import List


class Solution:
  def makeConnected(self, n: int, connections: List[List[int]]) -> int:
    # not enough cabels
    if len(connections)+1 < n:
      return -1
      
    g = {i:i for i in range(n)}
    connections.sort()
    
    def find(u: int) -> int:
      while g[u] != u:
        u = g[u]
        
      return u

    def union(u: int, v: int):
      u0, v0 = find(u), find(v)
      if u0 < v0:
        g[v0] = u0
      else:
        g[u0] = v0
    
    for u, v in connections:
      union(u, v)

    groups = set()
    # print(g)
    
    for i in range(n):
      root = find(i)
      groups.add(root)
      # print(i, root)
      
    return len(groups) - 1
      