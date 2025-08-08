'''
3529-count-cells-in-overlapping-horizontal-and-vertical-substrings
'''

from typing import List


class Solution:
  def countCells(self, grid: List[List[str]], pattern: str) -> int:
    m, n = len(grid), len(grid[0])
    h = ""
    for arr in grid:
      h += "".join(arr)

    res1 = []
    pr = 0
    x = len(pattern)
    
    for i in range(len(h)-len(pattern)+1):
      if h[i:i+x] == pattern:
        res1.append((max(i, pr), i+x))
        pr = i+x

    if len(res1) == 0:
      return 0
      
    res = set()
    for a, b in res1:
      for i in range(a, b):
        res.add((i//n, (i%n)))
            
    var = ""
    for i in range(len(grid[0])):
      for j in range(len(grid)):
        var += grid[j][i]

    res2 = set()
    prev = 0 

    for i in range(len(var)-x+1):
      if var[i:i+x] != pattern:
        continue

      for j in range(max(prev,i),i+x):
        res2.add((j%m,j//m))
        
      prev = i+x
                
    res = res.intersection(res2)
        
    return len(res)
        
    
        