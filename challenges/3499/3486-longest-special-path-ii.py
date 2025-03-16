'''
3486-longest-special-path-ii
'''

from collections import defaultdict
from sortedcontainers import SortedList
from typing import List


class Solution:
  def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
    n = len(nums)
    path = [[] for _ in range(n)]
    for u, v, w in edges:
      path[u].append((v, w))
      path[v].append((u, w))
    
    inf = 10 ** 5
    depth = [0] * n
    dis = [0] * n
    p1 = [-1] * n
    vis = defaultdict(lambda: -1)
    
    def dfs(u, p=-1):
      if nums[u] in vis:
        p1[u] = vis[nums[u]]
      
      saved = vis[nums[u]]
      vis[nums[u]] = u
      
      for v, w in path[u]:
        if v != p:
          depth[v] = depth[u] + 1
          dis[v] = dis[u] + w
          dfs(v, u)
      
      vis[nums[u]] = saved
    
    depth.append(-1)
    dfs(0)

    tmp = []
    v1 = SortedList()
    ans = []

    def dfs1(u, p=-1):
      tmp.append(u)
      if p1[u] != -1:
        v1.add(depth[p1[u]] * n + p1[u])
      
      chosen = v1[-2] % n if len(v1) >= 2 else -1
      chosen = tmp[depth[chosen] + 1]
      ans.append((u, chosen))
      
      for v, w in path[u]:
        if v != p:
          dfs1(v, u)
      
      if p1[u] != -1:
        v1.remove(depth[p1[u]] * n + p1[u])

      tmp.pop()
    
    dfs1(0)
    res = -1
    v = 0

    for x, y in ans:
      if dis[x] - dis[y] > res:
        res = dis[x] - dis[y]
        v = depth[x] - depth[y]

      elif dis[x] - dis[y] == res and depth[x] - depth[y] < v:
        res = dis[x] - dis[y]
        v = depth[x] - depth[y]
    
    return [res, v+1]
