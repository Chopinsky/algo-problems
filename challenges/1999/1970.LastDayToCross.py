'''
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

Example 1:

Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

Example 2:

Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

Example 3:

Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.

Constraints:

2 <= row, col <= 2 * 10^4
4 <= row * col <= 2 * 10^4
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
'''

from typing import List
from collections import defaultdict


class Solution:
  def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
    g = [[0]*col for _ in range(row)]
    for x, y in cells:
      g[x-1][y-1] = 1
      
    gdx = 1
    gc = {}
    gr = {}
    
    def bfs(x, y):
      stack = [(x, y)]
      gc[x, y] = gdx
      rows = set()
      
      while stack:
        x0, y0 = stack.pop()
        rows.add(x0)
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          x1, y1 = x+dx, y+dy
          if x1 < 0 or x1 >= row or y1 < 0 or y1 >= col:
            continue
            
          if g[x1][y1] == 1 or (x1, y1) in gc:
            continue
            
          gc[x1][y1] = gdx
          stack.append((x1, y1))
          
      return rows
    
    for x in range(row):
      for y in range(col):
        if (x, y) in gc or g[x][y] == 1:
          continue
          
        gr[gdx] = bfs(x, y)
        if len(gr[gdx]) == row:
          return len(cells)
        
        gdx += 1
          
    # print('init:', gc, gr)
    groups = [i for i in range(gdx)]
    
    def find(x: int) -> int:
      while groups[x] != x:
        x = groups[x]
        
      return x
    
    def union(x: int, y: int):
      rx, ry = find(x), find(y)
      if rx <= ry:
        groups[ry] = rx
      else:
        groups[rx] = ry
        
    cand = set()
    while cells:
      cand.clear()
      x, y = cells.pop()
      x -= 1
      y -= 1
      g[x][y] = 0
      group_root = gdx
      
      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= row or y0 < 0 or y0 >= col:
          continue
          
        if g[x0][y0] == 1:
          continue
        
        root = find(gc[x0, y0])
        group_root = min(group_root, root)
        cand.add(root)

      base = set([x])
      
      if not cand:
        # print('add:', x+1, y+1, gdx)
        gc[x, y] = gdx
        gr[group_root] = base
        groups.append(gdx)
        gdx += 1
        continue
        
      for r0 in cand:
        union(r0, group_root)
        base |= gr[r0]
      
      if len(base) == row:
        # print('fin:', x, y, cells)
        return len(cells)
      
      # print('union:', x+1, y+1, group_root, base)
      gc[x, y] = group_root
      gr[group_root] = base
        
    return 0
        

  def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
    arr = [i for i in range(row*col)]
    mat = [[0 for _ in range(col)] for _ in range(row)]
    walls = defaultdict(set)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    def key(x: int, y: int, c: int) -> int:
      return x*c + y
    
    def find(i: int) -> int:
      while i != arr[i]:
        i = arr[i]
        
      return i
    
    def union(i: int, j: int) -> int:
      ii, ji = find(i), find(j)
      k = ii
      
      if ii < ji:
        arr[ji] = ii
        walls[ii] |= walls.pop(ji, set())
      else:
        arr[ii] = ji
        walls[ji] |= walls.pop(ii, set())
        k = ji
      
      # print('post add', walls[k])
      return k
      
    for day, [x, y] in enumerate(cells):
      # print(x, y)
      x -= 1
      y -= 1
      mat[x][y] = 1
      
      k = key(x, y, col)
      walls[k].add(y)
      
      for dx, dy in dirs:
        x0, y0 = x+dx, y+dy
        if x0 < 0 or x0 >= row or y0 < 0 or y0 >= col:
          continue
          
        # print(x, y, x0, y0, mat[x0][y0])
        if not mat[x0][y0]:
          continue
          
        # print('union:', x, y, x0, y0)
        k0 = key(x0, y0, col)
        k = union(k, k0)
        
      # print(day, k, walls[k], walls)
      if len(walls[k]) == col:
        return day
      
    return len(cells)
    
