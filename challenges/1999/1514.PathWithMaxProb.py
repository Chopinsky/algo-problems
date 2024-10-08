'''
You are given an undirected weighted graph of n nodes (0-indexed), 
represented by an edge list where edges[i] = [a, b] is an undirected 
edge connecting the nodes a and b with a probability of success of 
traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum 
probability of success to go from start to end and return its success 
probability.

If there is no path from start to end, return 0. Your answer will be 
accepted if it differs from the correct answer by at most 1e-5.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.

Example 2:

Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000

Example 3:

Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.

Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
'''

from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    if start_node == end_node:
      return 1.0
    
    e = defaultdict(list)
    for (u, v), p in zip(edges, succProb):
      e[u].append((v, p))
      e[v].append((u, p))
      
    # print(e)
    stack = [(-1.0, start_node)]
    seen = {start_node: 1.0}
    
    while stack:
      p0, u = heappop(stack)
      p0 = -p0

      if u == end_node:
        return p0
      
      if p0 == 0:
        continue
      
      # print('run:', u, p0)
      
      for v, p1 in e[u]:
        p2 = p0*p1
        if v in seen and p2 <= seen[v]:
          continue
          
        seen[v] = p2
        heappush(stack, (-p2, v))
    
    return 0
        
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    p = [-1] * n
    s = {}
    nb = defaultdict(list)
    
    for [u, v], prob in zip(edges, succProb):
      nb[u].append(v)
      nb[v].append(u)
      
      if u > v:
        u, v = v, u
        
      s[u, v] = prob
      
    # print(s, nb)
    p[start] = 1
    stack = [(-p[start], start)]
    
    while stack:
      p0, u = heappop(stack)
      p0 = -p0
      
      if u == end:
        return p0
      
      for v in nb[u]:
        p1 = p0 * s[min(u, v), max(u, v)]
        if p1 <= p[v]:
          continue
          
        p[v] = p1
        heappush(stack, (-p[v], v))
      
    return 0
        
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    g = defaultdict(list)
    for i, e in enumerate(edges):
      g[e[0]].append((e[1], succProb[i]))
      g[e[1]].append((e[0], succProb[i]))
      
    rates = [0 if i != start else 1 for i in range(n)]
    stack = [(-1, start)]
    
    while stack:
      r, u = heappop(stack)
      r *= -1
      
      # less optimal option, skip
      if r < rates[u]:
        continue
      
      for v, prob in g[u]:
        if r*prob > rates[v]:
          heappush(stack, (-r*prob, v))
          rates[v] = r * prob
          
        # print(u, v, r, prob, rates)

    # print(rates)
    return rates[end]
  