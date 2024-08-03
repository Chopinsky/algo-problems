'''
There exists an undirected tree with n nodes numbered 0 to n - 1. You are given a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.

Initially, all nodes are unmarked. For each node i:

If i is odd, the node will get marked at time x if there is at least one node adjacent to it which was marked at time x - 1.
If i is even, the node will get marked at time x if there is at least one node adjacent to it which was marked at time x - 2.
Return an array times where times[i] is the time when all nodes get marked in the tree, if you mark node i at time t = 0.

Note that the answer for each times[i] is independent, i.e. when you mark node i all other nodes are unmarked.

Example 1:

Input: edges = [[0,1],[0,2]]

Output: [2,4,3]

For i = 0:
Node 1 is marked at t = 1, and Node 2 at t = 2.
For i = 1:
Node 0 is marked at t = 2, and Node 2 at t = 4.
For i = 2:
Node 0 is marked at t = 2, and Node 1 at t = 3.
Example 2:

Input: edges = [[0,1]]

Output: [1,2]

For i = 0:
Node 1 is marked at t = 1.
For i = 1:
Node 0 is marked at t = 2.
Example 3:

Input: edges = [[2,4],[0,1],[2,3],[0,2]]

Output: [4,6,3,5,5]

Constraints:

2 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
The input is generated such that edges represents a valid tree.

Test cases:

[[0,1],[0,2]]
[[0,1]]
[[2,4],[0,1],[2,3],[0,2]]
[[5,1],[8,4],[4,2],[6,3],[7,5],[9,7],[3,0],[1,0],[2,0]]
[[1,0],[2,1],[3,1],[7,2],[6,4],[4,2],[5,2]]
'''

from typing import List
from collections import defaultdict

class Solution:
  '''
  simplified version of the problem: the furthest node to i-th node, given:
    d(u, v) = 1 if u%2 == 1 else 2
  
  first iteration: bottom up to get the top-2 children distance from below the subtree;
  second iteration: top down and update the top-2 children distance from siblings;

  note that in the second iteration, can't count the self-subtree, so much use the alt-distant-children
  from siblings;
  '''
  def timeTaken(self, edges: List[List[int]]) -> List[int]:
    e = defaultdict(set)
    n = len(edges)+1
    c = [0]*n
    p = [-1]*n
    tops = [list() for _ in range(n)]
    
    for u, v in edges:
      e[u].add(v)
      c[u] += 1
      e[v].add(u)
      c[v] += 1

    # bottom up iteration
    cand, nxt = [i for i in range(n) if c[i] == 1], []
    dist = [0]*n
    seen = set()

    def add_top(u, v, dv):
      top = (dv, u)
      if len(tops[v]) < 2:
        tops[v].append(top)
      elif dv > tops[v][0][0]:
        tops[v][1] = tops[v][0]
        tops[v][0] = top
      elif dv > tops[v][1][0]:
        tops[v][1] = top
        
      # maintain order
      if len(tops[v]) >= 2 and tops[v][0][0] < tops[v][1][0]:
        tops[v][0], tops[v][1] = tops[v][1], tops[v][0]
    
    while True:
      if len(cand) == 1 and len(seen) == n-1:
        break    
        
      if len(cand) == 2 and cand[0] in e[cand[1]]:
        break
        
      # print(cand)
      for u in cand:
        for v in e[u]:
          if (u, v) in seen:
            continue
            
          dv = dist[u] + (1 if u%2 == 1 else 2)
          dist[v] = max(dist[v], dv)
          add_top(u, v, dv)
          # print('bottom-up:', v, dv)
          
          seen.add((v, u))
          p[u] = v
          
          c[v] -= 1
          if c[v] == 1:
            nxt.append(v)
          
      cand, nxt = nxt, cand
      nxt.clear()
          
    # update dual-roots
    if len(cand) == 2:
      u, v = cand
      du = dist[u]
      dv = dist[v]
      
      duv = dv + (1 if v%2 == 1 else 2)
      dist[u] = max(du, duv)
      p[u] = v
      add_top(v, u, duv)
      
      dvu = du + (1 if u%2 == 1 else 2)
      dist[v] = max(dv, dvu)
      p[v] = u
      add_top(u, v, dvu)

    # print('bu:', dist, p, tops)
    
    # top down
    while cand:
      # print(cand)
      for u in cand:
        du = 1 if u%2 == 1 else 2
        top = tops[u]
        dist[u] = max(dist[u], top[0][0])
        # print('td:', u, top)
        
        if len(top) == 1:
          top.append((0, -1))
        
        for v in e[u]:
          if v == p[u]:
            continue
            
          nxt.append(v)
          
          if v == top[0][1]:
            dv = top[1][0] + du
          else:
            dv = top[0][0] + du
          
          add_top(u, v, dv)
        
      cand, nxt = nxt, cand
      nxt.clear()
    
    return dist 
  
