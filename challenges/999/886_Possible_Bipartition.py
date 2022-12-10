'''
886. Possible Bipartition

We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.

Example 1:

Input: n = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4] and group2 [2,3].
Example 2:

Input: n = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false

Constraints:

1 <= n <= 2000
0 <= dislikes.length <= 10^4
dislikes[i].length == 2
1 <= dislikes[i][j] <= n
ai < bi
All the pairs of dislikes are unique.
'''

from collections import defaultdict
from typing import List


class Solution:
  def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
    color = [-1] * n
    graph = [[] for _ in range(n)]

    for a, b in dislikes:
      graph[a-1].append(b-1)
      graph[b-1].append(a-1)
    
    def dfs(u: int, curr: int) -> bool:
      color[u] = curr
      for v in graph[u]:
        if color[v] == curr:
          return False
    
        elif color[v] == -1 and not dfs(v, 1-curr):
          return False

      return True

    for u in range(n):
      if color[u] == -1 and not dfs(u, 0):
        return False

    return True


  def possibleBipartition0(self, n: int, dislikes: List[List[int]]) -> bool:
    d = defaultdict(set)
    side = [0]*(n+1)

    for a, b in dislikes:
      d[a].add(b)
      d[b].add(a)

    def bfs(root: int) -> bool:
      # print('root:', root)
      level = 1
      curr, nxt = [root], []
      side[root] = level

      while curr:
        # print('level:', level, curr)
        level = 3 - level

        for i in curr:
          for j in d[i]:
            if side[i] == side[j]:
              # print('fail:', i, j, side)
              return False

            if side[j] == 0:
              nxt.append(j)
              side[j] = level

        curr, nxt = nxt, curr
        nxt.clear()

      return True
    
    for i in range(1, n+1):
      if side[i] != 0:
        continue

      if not bfs(i):
        return False

    return True
