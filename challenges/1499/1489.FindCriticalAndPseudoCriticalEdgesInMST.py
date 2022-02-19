'''
Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.

Example 1:

Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
Output: [[0,1],[2,3,4,5]]
Explanation: The figure above describes the graph.
The following figure shows all the possible MSTs:

Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.
Example 2:

Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
Output: [[],[0,1,2,3]]
Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

Constraints:

2 <= n <= 100
1 <= edges.length <= min(200, n * (n - 1) / 2)
edges[i].length == 3
0 <= ai < bi < n
1 <= weighti <= 1000
All pairs (ai, bi) are distinct.
'''


from typing import List, Tuple
import math


class Solution:
  '''
  the trick is to check what's a critical edge, and what's a pseudo one:
    * critical edge: if *excluded* from the MST, the total score will rise, or the graph
                     will no longer be connected;
    * pseudo edge:   if *included* in the MST, we will get a valid MST;

  then we build a baseline score for the valid MST, and compare trees generated without an
  edge first, if the score becomes larger, we know it's a critical one; otherwise, make it
  part of the final tree, then re-generate the MST, if the score is still the valid MST score, 
  we know it is part of this valid MST, and hence a pseudo one.
  '''
  def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    ans = [[], []]
    e = {k: (i, j) for k, [i, j, w] in enumerate(edges)}
    edges = [(w, k) for k, [i, j, w] in enumerate(edges)]
    edges.sort()
    # print(edges, e)
    
    def find(arr: List[int], idx: int) -> int:
      while arr[idx] != idx:
        idx = arr[idx]
        
      return idx
    
    def union(arr: List[int], a: int, b: int):
      ai, bi = find(arr, a), find(arr, b)
      if ai <= bi:
        arr[bi] = ai
      else:
        arr[ai] = bi
    
    def calc_mst(exclude: int, start: Tuple[int]) -> int:
      p = [i for i in range(n)]
      score = 0
      count = 0
      
      if start:
        union(p, start[0], start[1])
        score += start[2]
        count += 1
        
      for w, idx in edges:
        if count == n-1:
          break
          
        if idx == exclude:
          continue
          
        i, j = e[idx]
        ri, rj = find(p, i), find(p, j)
        if ri == rj:
          continue
          
        score += w
        union(p, ri, rj)
        count += 1
          
      # if exclude == 3:
        # print(score, count, p)
          
      return score if count == n-1 else math.inf
    
    baseline = calc_mst(-1, None)
    # print('base line:', baseline)
    
    for w, idx in edges:
      # if don't use i-th edge
      score = calc_mst(idx, None)
      # print('c edge:', idx, w, e[idx], score)
      
      # ... and cause the score to rise, thus a critical-edge
      if score > baseline:
        ans[0].append(idx)
        continue
        
      # if idx is in the list
      score = calc_mst(-1, (e[idx][0], e[idx][1], w))
      # print('p edge:', score)
      
      # ... and if this will lead to the same baseline score,
      # thus a psudo-critical-edge
      if score == baseline:
        ans[1].append(idx)
    
    return ans
