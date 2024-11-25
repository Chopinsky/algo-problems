'''
3367. Maximize Sum of Weights after Edge Removals
'''

from typing import List
from heapq import nlargest


class Solution:
  def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
    n = len(edges) + 1
    graph = [[] for _ in range(n)]
    
    for i, j, w in edges:
      graph[i].append((j, w))
      graph[j].append((i, w))

    def dfs(i: int, parent: int):
      res = 0
      diff = []
      
      for j, w in graph[i]:
        if j == parent: 
          continue

        v1, v2 = dfs(j, i)
        res += v2
      
        # diff: the delta if taking the i<->j edge with 
        # 1 less grandchild edge, floored at 0 as not taking
        # the swap (i.e., no edge -> edge)
        diff.append(max(0, v1+w-v2))
        
      return (
        # take k-1 edges from children (hence can take the 
        # parent edge)
        res + sum(nlargest(k-1, diff)), 
        # take k edges from children (hence not taking the 
        # parent edge)
        res + sum(nlargest(k, diff)),
      )

    _, ans = dfs(0, -1)
    
    return ans
    