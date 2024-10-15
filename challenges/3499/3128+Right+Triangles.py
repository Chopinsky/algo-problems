'''
3128. Right Triangles

Test cases:

[[0,1,0],[0,1,1],[0,1,0]]
[[1,0,0,0],[0,1,0,1],[1,0,0,0]]
[[1,0,1],[1,0,0],[1,0,0]]
[[0,0],[0,1],[1,1]]
'''

from typing import List
from collections import defaultdict

class Solution:
  def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
    rows = defaultdict(list)
    cols = defaultdict(list)
    m, n = len(grid), len(grid[0])
    
    for x in range(m):
      for y in range(n):
        if grid[x][y] == 0:
          continue
          
        rows[x].append(y)
        cols[y].append(x)
    
    # print('init:', rows, cols)
    count = 0
    
    for x in sorted(rows.keys()):
      r = rows[x]
      hor_cnt = len(r) - 1
      
      for cdx in range(len(r)):
        y = r[cdx]
        c = cols[y]
        ver_cnt = len(c)-1
        count += ver_cnt * hor_cnt
        # print('iter:', (x, y), ver_cnt, hor_cnt)
        
    return count
        