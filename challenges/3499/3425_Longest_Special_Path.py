'''
3425. Longest Special Path
'''

from typing import List
from collections import defaultdict


class Solution:
  def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
    n = len(nums)
    max_val = max(nums)
    lastOccur = [-1] * (max_val + 1)
    res = [0, 1]
    pathStack = []
    adj = defaultdict(list)
    dist = [-1] * n

    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))

    def build_dist(u: int, parent: int, currDist: int):
      dist[u] = currDist
      for v, w in adj[u]:
        if v == parent:
          continue

        build_dist(v, u, currDist + w)

    def dfs(u: int, parent: int, nums: List[int], minIndex: int):
      stackPos = len(pathStack)
      pathStack.append(u)
      val = nums[u]
      oldPos = lastOccur[val]
      lastOccur[val] = stackPos
      if oldPos >= minIndex:
        minIndex = oldPos + 1
      
      if minIndex <= stackPos:
        ancestor = pathStack[minIndex]
        pathLength = dist[u] - dist[ancestor]
        pathNodes = stackPos - minIndex + 1
        
        if pathLength > res[0]:
          res[0] = pathLength
          res[1] = pathNodes
        elif pathLength == res[0]:
          res[1] = min(res[1], pathNodes)
      
      for v, _ in adj[u]:
        if v == parent:
          continue

        dfs(v, u, nums, minIndex)
      
      pathStack.pop()
      lastOccur[val] = oldPos

    build_dist(0, -1, 0)

    dfs(0, -1, nums, 0)
    
    return res
        