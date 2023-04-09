'''
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

Example 1:

Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).

Example 2:

Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.

Constraints:

n == colors.length
m == edges.length
1 <= n <= 10^5
0 <= m <= 10^5
colors consists of lowercase English letters.
0 <= aj, bj < n
'''

from collections import defaultdict
from typing import List


class Solution:
  def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    cnt = defaultdict(int)
    e = defaultdict(list)
    n = len(colors)
    store = {}
    
    for u, v in edges:
      e[u].append(v)
      cnt[v] += 1
      
    cand = []
    for u in range(n):
      if u not in cnt or cnt[u] == 0:
        cand.append(u)
        cnt.pop(u, None)
        store[u] = {colors[u]:1}
        
    if not cand:
      return -1

    most = 1
    # print(cand, store)
    #todo: iter
    
    while cand:
      u = cand.pop()
      
      for v in e[u]:
        cv = colors[v]
        
        if v not in store:
          store[v] = defaultdict(int)
          store[v][cv] = 1
          
        cnt[v] -= 1
        if cnt[v] == 0:
          cand.append(v)
          cnt.pop(v, None)
          
        for color, color_cnt in store[u].items():
          if color == cv:
            store[v][color] = max(store[v][color], 1+color_cnt)
          else:
            store[v][color] = max(store[v][color], color_cnt)
            
          most = max(most, store[v][color])
      
    if cnt:
      return -1
    
    return most
    

  def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
    e = defaultdict(list)
    n = len(colors)
    degrees = [0] * n
    heads = set([i for i in range(n)])
    edge_store = set()
    
    for u, v in edges:
      if v == u or (v, u) in edge_store:
        return -1
      
      e[u].append(v)
      heads.discard(v)
      degrees[v] += 1
      edge_store.add((u, v))
      
    stack = []
    counter = defaultdict(dict)
    
    for u in heads:
      stack.append(u)
      counter[u][colors[u]] = 1
      
    # print(e, stack, counter)
    top = 1
    
    while stack:
      u = stack.pop()
      
      for v in e[u]:
        edge_store.discard((u, v))
        degrees[v] -= 1
        
        if colors[v] not in counter[v]:
          counter[v][colors[v]] = 1
        
        if not degrees[v]:
          stack.append(v)
        
        for col, cnt in counter[u].items():
          src = counter[v].get(col, 0)
          counter[v][col] = max(src, cnt + (1 if col == colors[v] else 0))
          top = max(top, counter[v][col])
          
    # print('final', top, edge_store, counter)
    if edge_store:
      return -1
    
    return top
  
