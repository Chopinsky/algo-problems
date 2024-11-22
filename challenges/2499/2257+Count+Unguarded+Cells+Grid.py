'''
2257. Count Unguarded Cells in the Grid

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

Example 1:

Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:

Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.

Constraints:

1 <= m, n <= 10^5
2 <= m * n <= 10^5
1 <= guards.length, walls.length <= 5 * 10^4
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.
'''

from typing import List
from bisect import bisect_right
from collections import defaultdict


class Solution:
  def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    rows = defaultdict(list)
    cols = defaultdict(list)
    skip = set()
    
    for x, y in guards:
      rows[x].append((y, 0))
      cols[y].append((x, 0))
      skip.add((x, y))
      
    for x, y in walls:
      rows[x].append((y, 1))
      cols[y].append((x, 1))
      skip.add((x, y))
      
    for row in rows.values():
      row.sort()
    
    for col in cols.values():
      col.sort()
      
    # print('init:', rows, cols, skip)
    count = 0
    
    for x in range(m):
      for y in range(n):
        if (x, y) in skip:
          continue
          
        free = 0
        
        if x not in rows:
          free += 1
        else:
          row = rows[x]
          idx = bisect_right(row, (y, -1))
          rg = idx < len(row) and row[idx][1] == 0
          lg = idx-1 >= 0 and row[idx-1][1] == 0
          free += 1 if not rg and not lg else 0
        
        if y not in cols:
          free += 1
        else:
          col = cols[y]
          idx = bisect_right(col, (x, -1))
          bg = idx < len(col) and col[idx][1] == 0
          tg = idx-1 >= 0 and col[idx-1][1] == 0
          free += 1 if not bg and not tg else 0
          
        if free == 2:
          # print('free:', (x, y))
          count += 1
          
    return count
        
  def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    rows, rl = [[] for _ in range(m)], [[] for _ in range(m)]
    cols, cl = [[] for _ in range(n)], [[] for _ in range(n)]
    src = sorted([(x, y, 'g') for x, y in guards] + [(x, y, 'w') for x, y in walls])
    taken = set((x, y) for x, y, _ in src)
    
    for x, y, label in src:
      rows[x].append(y)
      rl[x].append(label)
      
      cols[y].append(x)
      cl[y].append(label)
      
    # print(rows, rl)
    # print(cols, cl)
        
    def check_row(x: int, y: int) -> bool:
      row = rows[x]
      if not row:
        return True
      
      label = rl[x]
      if y <= row[0]:
        return y != row[0] and label[0] == 'w'
      
      if y >= row[-1]:
        return y != row[-1] and label[-1] == 'w'
      
      idx = bisect_right(row, y) - 1
      l = row[idx]
      r = row[idx+1]
      if l == y or r == y:
        return False
      
      return label[idx] != 'g' and label[idx+1] != 'g'
    
    def check_col(x: int, y: int) -> bool:
      col = cols[y]
      if not col:
        return True
      
      label = cl[y]
      if x <= col[0]:
        return x != col[0] and label[0] == 'w'
      
      if x >= col[-1]:
        return x != col[-1] and label[-1] == 'w'
      
      idx = bisect_right(col, x)-1
      t = col[idx]
      b = col[idx+1]
      if t == x or b == x:
        return False
      
      return label[idx] != 'g' and label[idx+1] != 'g'
    
    count = 0
    for x in range(m):
      for y in range(n):
        if (x, y) in taken:
          continue
        
        if check_row(x, y) and check_col(x, y):
          count += 1
          
    return count
      