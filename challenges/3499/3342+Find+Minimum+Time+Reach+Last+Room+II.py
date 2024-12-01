'''
3342. Find Minimum Time to Reach Last Room II

[[38,87,68,34,32,8],[3,29,39,73,86,10]]
[[0,4],[4,4]]
[[0,0,0,0],[0,0,0,0]]
[[0,1],[1,2]]
'''

from typing import List
from heapq import heappush, heappop
import math


class Solution:
  def minTimeToReach(self, mat: List[List[int]]) -> int:
    m, n = len(mat), len(mat[0])
    dp = {(0, 0, 1): 0}
    stack = []
    
    if m > 1:
      t = mat[1][0]
      heappush(stack, (t+1, 1, 0, 2))
      
    if n > 1:
      t = mat[0][1]
      heappush(stack, (t+1, 0, 1, 2))
      
    while stack:
      t0, x, y, s = heappop(stack)
      if (x, y, s) in dp and t0 >= dp[x, y, s]:
        continue
        
      dp[x, y, s] = t0
      if x+1 < m:
        t1 = max(mat[x+1][y], t0)
        heappush(stack, (t1+s, x+1, y, 3-s))
        
      if x-1 >= 0:
        t1 = max(mat[x-1][y], t0)
        heappush(stack, (t1+s, x-1, y, 3-s))
        
      if y+1 < n:
        t1 = max(mat[x][y+1], t0)
        heappush(stack, (t1+s, x, y+1, 3-s))
        
      if y-1 >= 0:
        t1 = max(mat[x][y-1], t0)
        heappush(stack, (t1+s, x, y-1, 3-s))
      
    # print('done:', dp)
    return min(
      dp.get((m-1, n-1, 1), math.inf), 
      dp.get((m-1, n-1, 2), math.inf),
    )
    
        