'''
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:

Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
'''


import math
from typing import List
from collections import deque
from heapq import heappush, heappop


class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    n = len(graph)
    if n == 0 or not graph[0]:
      return 0
    
    cnt = math.inf
    m0 = (1<<n) - 1
    
    def bfs(root: int):
      curr, nxt = [(root, 1<<root)], []
      seen = set(curr)
      steps = 0
      
      while curr:
        steps += 1
        for i, m in curr:
          for j in graph[i]:
            nm = m | (1 << j)
            if nm == m0:
              return steps
            
            if (j, nm) in seen:
              continue
              
            nxt.append((j, nm))
            seen.add((j, nm))
        
        curr, nxt = nxt, curr
        nxt.clear()
        
      return math.inf
    
    for i in range(n):
      cnt = min(cnt, bfs(i))
    
    return cnt
        
        
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    n = len(graph)
    q = deque([(i, 1<<i) for i in range(n)])
    states = [set([1<<i]) for i in range(n)]
    steps = 0
    target = (1<<n) - 1
    # print(states, q)
    
    # just bfs, no optimization
    while q:
      count = len(q)
      
      while count:
        u, state = q.popleft()
        
        # all vertices have been visited
        if state == target:
          return steps
        
        for v in graph[u]:
          nxt_state = state | 1<<v
          if nxt_state == target:
            return steps+1
          
          if nxt_state in states[v]:
            continue
            
          states[v].add(nxt_state)
          q.append((v, nxt_state))
        
        count -= 1
      
      steps += 1
    
    return math.inf
    
  
  def shortestPathLength0(self, graph: List[List[int]]) -> int:
    roots = {}
    chain_nodes = set()
    n = len(graph)
    max_len = 0
    target = (1 << n) - 1
    
    def get_chain(i: int):
      count = 0
      head = i
      
      while (i == head) or (len(graph[i]) == 2 and (graph[i][0] in chain_nodes or graph[i][1] in chain_nodes)):
        chain_nodes.add(i)
        i = graph[i][1] if (len(graph[i]) == 2 and graph[i][0] in chain_nodes) else graph[i][0]
        count += 1
      
      if len(graph[i]) == 1 and i != head:
        chain_nodes.add(i)
      
      if count:
        if i not in roots:
          roots[i] = [count, count, -1]
          
        else:
          roots[i][0] += count
          if count >= roots[i][1]:
            roots[i][2] = roots[i][1]
            roots[i][1] = count
          
          elif count > roots[i][2]:
            roots[i][2] = count
    
    # build the single chains
    for i, chain in enumerate(graph):
      # add to the total amount of
      max_len += len(chain)
      if (len(chain) != 1) or (i in chain_nodes):
        continue
        
      get_chain(i)
        
    # chains.sort(reverse=True)
    
    for i, chain in enumerate(graph):
      if len(chain) <= 1:
        graph[i] = []
        continue
        
      pruned = []
      for j in chain:
        if j not in chain_nodes:
          pruned.append(j)
          
      graph[i] = pruned
      
    for i in chain_nodes:
      target ^= 1 << i
    
    # print(graph, roots, chain_nodes, '{:012b}'.format(target))
    
    # all nodes are in 1 long chain
    if not target:
      return n-1
      
    short = max_len
    
    def bfs(i: int) -> int:
      steps = 0
      stack = []
      states = set()
      
      if i in roots:
        steps += 2*roots[i][0] - roots[i][1]
        if roots[i][2] > 0:
          ss = steps-roots[i][2]
          stack.append((ss, i, 1<<i, 1))
          states.add((i, 1<<i, 1))
          
      heappush(stack, (steps, i, 1<<i, 0))
      states.add((i, 1<<i, 0))
      # print('init:', i, stack)
        
      while stack:
        steps, u, seen, back = heappop(stack)
        # print(u, '{:012b}'.format(seen), steps, back)
        
        # if (u, seen, back) in states:
        #   continue
        
        # if all remainder nodes have been visited, and we either
        # done, or we have routed back to the start (with reduced chain),
        # we have reached the min-steps to visit all nodes
        if seen == target and (not back or u == i):
          # print('done:', u, '{:012b}'.format(seen), steps, back)
          return steps
        
        for v in graph[u]:
          # print('find next:', u, v)
          seen_v = seen | 1<<v
          steps_v = steps + 1
          
          # idled for too long, not going to be the ideal solution
          if steps_v > max_len or (v, seen_v, back) in states:
            continue
          
          # add steps to visit chains linked to this node if not the start,
          # since we've already added all needed chain steps
          if v in roots and not (seen & 1<<v):
            steps_v += 2 * roots[v][0]
            
            # if this is the last node to visit without needing to go back 
            # to start, don't need to come back from the longest chain
            if seen_v == target and not back:
              steps_v -= roots[v][1]
              
          heappush(stack, (steps_v, v, seen_v, back))
          states.add((v, seen_v, back))
      
      return math.inf
    
    for i in range(n):
      if i in chain_nodes:
        continue
        
      short = min(short, bfs(i))
    
    return short
