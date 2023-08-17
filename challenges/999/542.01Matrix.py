'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 10 ** 4
1 <= m * n <= 10 ** 4
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
'''

import math
from typing import List


class Solution:
  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    d = [[math.inf]*n for _ in range(m)]
    
    def is_edge(x: int, y: int) -> bool:
      if mat[x][y] == 0:
        return False
      
      if x-1 >= 0 and mat[x-1][y] == 0:
        return True
      
      if x+1 < m and mat[x+1][y] == 0:
        return True
      
      if y-1 >= 0 and mat[x][y-1] == 0:
        return True
      
      if y+1 < n and mat[x][y+1] == 0:
        return True
      
      return False
    
    curr, nxt = set(), set()
    seen = set()
    
    for x in range(m):
      for y in range(n):
        val = mat[x][y]
        if val == 0:
          d[x][y] = 0
          continue
          
        if is_edge(x, y):
          d[x][y] = 1
          curr.add((x, y))
          
    # print(curr)
    while curr:
      seen |= curr
      # print("iter:", curr)
      
      for x, y in curr:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          if mat[x0][y0] != 1 or ((x0, y0) in seen):
            continue
            
          d[x0][y0] = min(d[x0][y0], d[x][y] + 1)
          nxt.add((x0, y0))
      
      curr, nxt = nxt, curr
      nxt.clear()
          
    return d
  

  def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    h, w = len(mat), len(mat[0])
    dist = [[0 if mat[i][j] == 0 else -1 for j in range(w)] for i in range(h)]
    # print(dist)
    
    stack = []
    dirs = [-1, 0, 1, 0, -1]
    
    for x in range(h):
      for y in range(w):
        if mat[x][y] == 0:
          continue
        
        zero_neighbor = False
        for k in range(4):
          x0, y0 = x+dirs[k], y+dirs[k+1]
          if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w or mat[x0][y0] == 1:
            continue
            
          zero_neighbor = True
          break
          
        if zero_neighbor:
          stack.append((x, y))
          dist[x][y] = 1
          
    step = 2
    # print(stack)
    
    while len(stack) > 0:
      next_round = []
      
      for (x, y) in stack:
        for k in range(4):
          x0, y0 = x+dirs[k], y+dirs[k+1]
          if x0 < 0 or x0 >= h or y0 < 0 or y0 >= w or dist[x0][y0] >= 0:
            continue
            
          dist[x0][y0] = step
          next_round.append((x0, y0))
      
      stack = next_round
      step += 1
    
    return dist
    