'''
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]

Constraints:

1 <= n <= 10^4
0 <= paths.length <= 2 * 10^4
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
Every garden has at most 3 paths coming into or leaving it.
'''

from typing import List
from collections import defaultdict


class Solution:
  def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
    ans = [0] * n
    e = defaultdict(list)
    
    for u, v in paths:
      e[u-1].append(v-1)
      e[v-1].append(u-1)
    
    # print(e)
    for i in range(n):
      if ans[i] > 0:
        continue
        
      stack = [(i, 0)]
      ans[i] = 1
      
      while stack:
        u, i = stack.pop()
        if i >= len(e[u]):
          continue

        v = e[u][i]  
        while v >= 0 and ans[v] > 0:
          i += 1
          v = e[u][i] if i < len(e[u]) else -1

        # all u's neighbors have been visited
        if v < 0:
          continue

        if i+1 < len(e[u]):
          stack.append((u, i+1))
          
        colors = set([1, 2, 3, 4])
        # print(u, i, v)

        for w in e[v]:
          if ans[w] > 0:
            colors.discard(ans[w])

        # print(u, i, v, colors)
        ans[v] = colors.pop()
        stack.append((v, 0))
    
    return ans
  