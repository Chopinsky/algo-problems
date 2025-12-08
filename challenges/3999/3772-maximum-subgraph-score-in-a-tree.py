'''
3772-maximum-subgraph-score-in-a-tree
'''

from collections import defaultdict
from typing import List


class Solution:
  def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
    e = defaultdict(list)
    for u, v in edges:
      e[u].append(v)
      e[v].append(u)

    q = [0]
    p = [-1]*n

    # build the tree
    for u in q:
      for v in e[u]:
        if v == p[u]:
          continue

        q.append(v)
        p[v] = u

    dp = [1 if val > 0 else -1 for val in good]
    
    # traverse from bottom to top
    for u in q[::-1]:
      v = p[u]
      if v < 0:
        continue

      # scores from subtree
      dp[v] += max(dp[u], 0)

    ans = dp.copy()

    # traverse from top to bottom
    for u in q:
      v = p[u]
      if v < 0:
        continue

      # scores from the "parent+cousin" part of the tree
      high = ans[v] - max(dp[u], 0)
      ans[u] += max(high, 0)

    return ans

    
        