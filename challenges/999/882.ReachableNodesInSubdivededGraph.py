'''
You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.

Example 1:

Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.

Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23

Example 3:

Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.

Constraints:

0 <= edges.length <= min(n * (n - 1) / 2, 10 ** 4)
edges[i].length == 3
0 <= ui < vi < n
There are no multiple edges in the graph.
0 <= cnti <= 104
0 <= maxMoves <= 109
1 <= n <= 3000
'''


from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
  def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
    d = [-1 for _ in range(n)]
    e = defaultdict(list)
    l = {}
    unfinished = {}
    finished = set()
    
    for i, j, d0 in edges:
      e[i].append((j, d0+1))
      e[j].append((i, d0+1))
      l[i, j] = d0
      
    count = 1
    stack = [(-maxMoves, 0)]
    
    while stack:
      moves, curr = heappop(stack)
      moves = -moves
      
      # a better solution has already been explored, skip
      if moves < d[curr]:
        continue
      
      # print('next:', curr, moves, e[curr])
      for nxt, dist in e[curr]:
        # don't go back to 0, and don't redo the edge again
        if (curr, nxt) in finished:
          continue
          
        # we can reach the main node from the current node
        if moves >= dist:
          # less optimal solutions will be discarded
          unfinished.pop((curr, nxt), None)
          unfinished.pop((nxt, curr), None)
          
          # we can reach the node for the first time ever, add
          # all subnodes + main node
          if nxt > 0 and (curr, nxt) not in finished:
            count += dist if d[nxt] < 0 else dist-1
            
          finished.add((curr, nxt))
          finished.add((nxt, curr))
          left = moves - dist
          
          # updating the point we reached, and don't go back to 0
          if d[nxt] < left and nxt > 0:
            d[nxt] = left
            
            # only add if we have more moves to go from there
            if left > 0:
              heappush(stack, (-left, nxt))
        
        # we can't reach the next node from the current node,
        # and no other route to the next node is discovered yet,
        # add the edge to the unfinished list
        else:
          if (curr, nxt) in unfinished:
            unfinished[curr, nxt] = max(unfinished[curr, nxt], moves)
          else:
            unfinished[curr, nxt] = moves
        
      # print("after:", curr, count)
        
    done = set()
    # print(d, count)
    # print(unfinished)
    # print(finished)
    
    for edge in unfinished:
      i, j = min(edge), max(edge)
      if (i, j) in done:
        continue
        
      d0 = unfinished[i, j] if (i, j) in unfinished else 0
      d1 = unfinished[j, i] if (j, i) in unfinished else 0
      total = l[i, j]
      done.add((i, j))
      # print(d0, d1, total)
      
      if d0+d1 > total:
        count += total
      else:
        count += d0 + d1
    
    return count
    