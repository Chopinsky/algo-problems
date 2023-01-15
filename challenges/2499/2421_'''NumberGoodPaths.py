'''
2421. Number of Good Paths

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

Example 1:

Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
Example 2:

Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.
Example 3:

Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.

Constraints:

n == vals.length
1 <= n <= 3 * 10^4
0 <= vals[i] <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.

Test cases:

[1,3,2,1,3]
[[0,1],[0,2],[2,3],[2,4]]

[1,1,2,2,3]
[[0,1],[1,2],[2,3],[2,4]]

[1]
[]

[2,5,5,1,5,2,3,5,1,5]
[[0,1],[2,1],[3,2],[3,4],[3,5],[5,6],[1,7],[8,4],[9,7]]

[2,1,1]
[[0,1],[2,0]]
'''

from typing import List
from collections import defaultdict


class Solution:
  def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
    e = defaultdict(set)
    for u, v in edges:
      e[u].add(v)
      e[v].add(u)
      
    n = len(vals)
    count = n
    g = [i for i in range(n)]
    groups = {i: (vals[i], 1) for i in range(n)}
    
    def find(u: int) -> int:
      while g[u] != u:
        u = g[u]
      
      return u
    
    cand = sorted((val, i) for i, val in enumerate(vals))
    seen = set()
    
    for val, u in cand:
      # print('visit:', u, val)
      
      for v in (e[u] & seen):
        ru, rv = find(u), find(v)
        r0, r1 = min(ru, rv), max(ru, rv)
        g[r1] = r0
        
        # print('adding:', v)
        # print('check:', (r0, groups[r0]), (r1, groups[r1]))
        
        if groups[r0][0] != groups[r1][0]:
          if groups[r1][0] > groups[r0][0]:
            groups[r0] = groups[r1]
            
          continue
          
        count += groups[r0][1] * groups[r1][1]
        groups[r0] = (groups[r0][0], groups[r0][1] + groups[r1][1])
        
      seen.add(u)
    
    return count
    

  '''
  this is not a tree problem, but a graph problem first and for most; if the
  goal is clear, the rest is more palpable -- we're implementing a derived version
  of the Prim's algorithm

  the idea is to build the graph from lowest values up -- since nodes can only
  reach other nodes via all smaller value nodes, each group of the nodes built
  prior must all be accessible from the current node to add, hence we only care
  about the nodes in the groups that has the same value (i.e. the max value in the
  group), because those are the other terminal nodes in the good path.
  '''
  def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
    n = len(vals)
    count = n
    e = defaultdict(list)
    group = [i for i in range(n)]
    
    def find(x):
      while group[x] != x:
        x = group[x]
        
      return x
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
      
    cand = sorted((val, i) for i, val in enumerate(vals))
    store = [(val, i) for i, val in enumerate(vals)]
    seen = set()
    # print(cand)
    
    # adding vertices one by one
    for val, u in cand:
      seen.add(u)
      ru = find(u)
      total = 1
      
      # checking if there are existing groups that
      # we should merge with -- we only care the top value
      # of each existing group, as the `cand` is sorted by
      # value, so we only care about the top nodes that
      # equals the current node's value
      for v in e[u]:
        if v not in seen:
          continue
          
        # get data for this group
        rv = find(v)
        v1, c1 = store[rv]
        # print('checking', u, v, ru, rv)
        
        # merge the groups
        ru, rv = min(ru, rv), max(ru, rv)
        group[rv] = ru
        
        # only care about the groups whose top
        # value equals the current node's value
        if v1 == val:
          count += c1 * total
          total += c1
          
      # update the group's root values, which will be
      # used as the source of truth for all future merges
      store[ru] = (val, total)
        
    # print(store)
    return count
    

  ''' TLE
  def numberOfGoodPaths1(self, vals: List[int], edges: List[List[int]]) -> int:
    n = len(vals)
    count = n
    e = defaultdict(list)
    seen = set()
    
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
  
    stack, nxt = [0], []
    children = [0]*n
    parent = {}
    
    while stack:
      for u in stack:
        seen.add(u)
        
        for v in e[u]:
          if v in seen:
            continue
            
          parent[v] = u
          nxt.append(v)
          children[u] += 1
          
      stack, nxt = nxt, stack
      nxt.clear()
      
    stack = [i for i in range(n) if children[i] == 0]
    store = [defaultdict(int) for _ in range(n)]
    # print(children, stack, parent)
    
    def gather(u):
      # base = store[u]
      val = vals[u]
      add = 0
      
      for v in e[u]:
        if u in parent and parent[u] == v:
          continue
          
        # res = gather(v)
        for k, c in store[v].items():
          if k < val:
            continue
            
          if k == val:
            add += c
          
          if k >= val:
            add += c * store[u][k]
            
          store[u][k] += c

      store[u][val] += 1
      # print(u, store[u])
      
      return add
      
    idx = 0
    while idx < len(stack):
      u = stack[idx]
      idx += 1
      count += gather(u)

      if u in parent:
        p = parent[u]
        children[p] -= 1
        if children[p] == 0:
          stack.append(p)

    # print(store)
    return count
  '''
  