'''
There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.

Example 2:

Input: n = 1, edges = []
Output: [0]

Example 3:

Input: n = 2, edges = [[1,0]]
Output: [1,1]

Constraints:

1 <= n <= 3 * 10^4
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
'''

from typing import List, Tuple
from collections import defaultdict

class Solution:
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    node = {}
    ans = [0]*n
    e = [list() for _ in range(n)]
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
    
    def dfs(u: int, p: int) -> int:
      cnt = 1
      dist = 0
      
      for v in e[u]:
        if v == p:
          continue
        
        c0, d0 = dfs(v, u)
        cnt += c0
        dist += (d0 + c0)
      
      node[u] = [p, cnt, dist]
      
      return cnt, dist
    
    def update(u: int):
      p, c0, d0 = node[u]
      
      if u == 0:
        ans[u] = d0
      else:
        ans[u] = d0 + (ans[p]-d0-c0) + (n-c0)
        # print('update:', (u, node[u]), (node[p][2]-d0-c0, n-c0))
        
      for v in e[u]:
        if v == p:
          continue
          
        update(v)
      
    dfs(0, -1)
    update(0)
    # print(node)
    
    return ans
        
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    e = defaultdict(list)
    down = {}
    ans = [0] * n
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
    
    def count(u: int, p: int):
      d0, c0 = 0, 1
      
      for v in e[u]:
        if v == p:
          continue
          
        # visit node v, parent is u
        d1, c1 = count(v, u)
        c0 += c1
        d0 += c1 + d1
      
      down[u] = c0
      # print(u, p, d0, c0)
      
      return d0, c0
      
    dist, total = count(0, -1)
    ans[0] = dist
    # print(down)
    
    def drill_down(u: int, p: int):
      ans[u] = ans[p] + (total-down[u]) - down[u]
      # print(u, p, ans[u])
      
      for v in e[u]:
        if v == p:
          continue
          
        drill_down(v, u)
    
    for v in e[0]:
      drill_down(v, 0)
    
    return ans
  
  
  def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2:
      return [0] if n == 1 else [1, 1]
    
    d = defaultdict(list)
    dist = {}
    
    for i, j in edges:
      d[i].append(j)
      d[j].append(i)
    
    def walk(s: int, r: int) -> Tuple[int]:
      if (s, r) in dist:
        return dist[s, r]
      
      cr, dr = 1, 0
      for n0 in d[r]:
        if n0 == s:
          continue
          
        c0, d0 = walk(r, n0)
        cr += c0
        dr += c0 + d0
      
      dist[s, r] = (cr, dr)
      return dist[s, r]

    ans = [0] * n
    for i in range(n):
      _, di = walk(-1, i)
      ans[i] = di
      # print(i, di)

    # print("dist:", dist)
    
    return ans
      