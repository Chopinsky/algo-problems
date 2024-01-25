from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:
  def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)
      
    score, n = 0, len(values)
    p, subtree = [0]*n, [val for val in values]
    ch = defaultdict(list)
    
    def dfs(u):
      for v in e[u]:
        if p[u] == v:
          continue

        ch[u].append(v)
        p[v] = u
        dfs(v)
        subtree[u] += subtree[v]

    dfs(0)
    # print(ch, p, subtree)
    
    @lru_cache(None)
    def score(u: int):
      if u >= n or not ch[u]:
        return 0
      
      # keep value at this node, can take out all values from children
      s0 = subtree[u] - values[u] 
      
      # take out values at this node, add children scores 
      s1 = values[u]
      for v in ch[u]:
        s1 += score(v)
      
      return max(s0, s1)
    
    return score(0)
        