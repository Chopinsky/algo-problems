'''
2699. Modify Graph Edge Weights

You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.

Example 1:

Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.

Example 2:

Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.

Example 3:

Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.

Constraints:

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 10^7
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 10^9
The graph is connected, and there are no self-loops or repeated edges
'''

from typing import List
from collections import defaultdict
from functools import lru_cache
from heapq import heappush, heappop
import math


class Solution:
  '''
  the idea is to find out the `dist` for the modifiable edges: use BFS as the main loop branch, and
  we move from `source` to node `u`, if the edge to its children `v` is modifiable, then the `dist`
  assigned to this edge should be: `target - source_to_u - v_to_destination`; v_to_destination is
  determined herustically, where modifiable edges are given distance of 1.
  '''
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    max_val = 2*10**9
    weight = {}
    e = defaultdict(list)
    
    def get_pair(u, v):
      return (min(u, v), max(u, v))
      
    for u, v, w in edges:
      e[u].append((v, w))
      e[v].append((u, w))
      weight[get_pair(u, v)] = w
      
    # print(e, weight)
    stack = [(0, destination)]
    to_dest = {destination:0}
    
    while stack:
      s0, u = heappop(stack)
      if to_dest[u] < s0:
        continue
      
      for v, w in e[u]:
        w = weight[get_pair(u, v)]
        s1 = s0 + (1 if w < 0 else w)
        
        if v not in to_dest or s1 < to_dest[v]:
          to_dest[v] = s1
          heappush(stack, (s1, v))
      
    stack = [(0, source)]
    score = {source:0}
    reached = False
    
    while stack and not reached:
      s0, u = heappop(stack)
      # print('check:', u, s0)
      
      if score[u] < s0:
        continue
        
      if u == destination:
        if s0 < target:
          return []
        
        reached = s0 == target
        continue
      
      for v, w in e[u]:
        pair = get_pair(u, v)
        w = weight[pair]
        
        if w < 0:
          s2 = to_dest[v]
          w = target - s0 - s2
          if w > max_val:
            return []
          
          if w == 0:
            w = max_val
            
          weight[pair] = w
          # print('assign:', (u, v), s0, s2, w)
        
        s1 = s0 + w
        if v not in score or s1 < score[v]:
          score[v] = s1
          heappush(stack, (s1, v))
    
    # print('fin:', weight)
    ans = []
    if not reached:
      return ans
    
    for p, w in weight.items():
      if w < 0:
        ans.append([p[0], p[1], max_val])
      else:
        ans.append([p[0], p[1], w])
    
    return ans
    

  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    max_val = 2*10**9
    weight = {}
    e = defaultdict(list)
    
    def get_pair(u, v):
      return (min(u, v), max(u, v))
      
    for u, v, w in edges:
      e[u].append((v, w))
      e[v].append((u, w))
      weight[get_pair(u, v)] = w
      
    # print(e, weight)
    
    @lru_cache(None)
    def from_target(t: int):
      stack = [(0, destination)]
      score = {destination:0}
      
      while stack:
        s0, u = heappop(stack)
        if score[u] < s0:
          continue
        
        if u == t:
          return s0
        
        for v, w in e[u]:
          w = weight[get_pair(u, v)]
          s1 = s0 + (1 if w < 0 else w)
          
          if v not in score or s1 < score[v]:
            score[v] = s1
            heappush(stack, (s1, v))
        
      return math.inf
      
    stack = [(0, source)]
    score = {source:0}
    reached = False
    
    while stack and not reached:
      s0, u = heappop(stack)
      # print('check:', u, s0)
      
      if score[u] < s0:
        continue
        
      if u == destination:
        if s0 < target:
          return []
        
        reached = s0 == target
        continue
      
      for v, w in e[u]:
        pair = get_pair(u, v)
        w = weight[pair]
        
        if w < 0:
          s2 = from_target(v)
          w = target - s0 - s2
          if w > max_val:
            return []
          
          if w == 0:
            w = max_val
            
          weight[pair] = w
          # print('assign:', (u, v), s0, s2, w)
        
        s1 = s0 + w
        if v not in score or s1 < score[v]:
          score[v] = s1
          heappush(stack, (s1, v))
    
    # print('fin:', weight)
    ans = []
    if not reached:
      return ans
    
    for p, w in weight.items():
      if w < 0:
        ans.append([p[0], p[1], max_val])
      else:
        ans.append([p[0], p[1], w])
    
    return ans
    