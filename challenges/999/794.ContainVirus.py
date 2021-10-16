'''
A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as an m x n binary grid isInfected, where isInfected[i][j] == 0 represents uninfected cells, and isInfected[i][j] == 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region (i.e., the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night). There will never be a tie.

Return the number of walls used to quarantine all the infected regions. If the world will become fully infected, return the number of walls used.

Example 1:

Input: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
Output: 10
Explanation: There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:

Input: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

Example 3:

Input: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
Output: 13
Explanation: The region on the left only builds two new walls.

Constraints:

m == isInfected.length
n == isInfected[i].length
1 <= m, n <= 50
isInfected[i][j] is either 0 or 1.
There is always a contiguous viral region throughout the described process that will infect strictly more uncontaminated squares in the next round.
'''


from typing import List
from collections import defaultdict


class Solution:
  def containVirus(self, areas: List[List[int]]) -> int:
    regions = []
    infected = set()
    walled = set()
    walls = 0
    m, n = len(areas), len(areas[0])
    dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    dots = [i for i in range(m*n)]
    
    def find(x: int, y: int) -> int:
      key = x*n + y
      while dots[key] != key:
        key = dots[key]
        
      return key
    
    def find_key(k: int) -> int:
      while dots[k] != k:
        k = dots[k]
        
      return k
    
    def union(x0: int, y0: int, x1: int, y1: int):
      k0, k1 = find(x0, y0), find(x1, y1)
      
      if k0 <= k1:
        dots[k1] = k0
      else:
        dots[k0] = k1
    
    def init_regions(x: int, y: int):
      nxt_areas = set()
      borders = set()
      border_len = 0
      stack = [(x, y)]
      
      while stack:
        x, y = stack.pop()
        if (x, y) in infected:
          continue
        
        infected.add((x, y))
        
        for dx, dy in dirs:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n or (x0, y0) in infected:
            continue
          
          # bordering an uninfected area
          if not areas[x0][y0]:
            nxt_areas.add((x0, y0))
            borders.add((x, y))
            border_len += 1
            # print('adding wall', x, y, x0, y0)
          
          else:
            stack.append((x0, y0))
            union(x, y, x0, y0)
          
      regions.append((len(nxt_areas), border_len, nxt_areas, borders))
        
    def spread(day: int):
      nonlocal walls, walled
      
      longest_wall = max(regions)
      # print(day, walls, longest_wall[0])
      walls += longest_wall[1]
      pts = set()
      
      for reg in regions:
        # build the wall along the most infection-possible 
        # region and call it the day
        if reg[0] == longest_wall[0]:
          wall_len = -1
          walled |= reg[3]
          continue
          
        # add border areas for processing
        for x, y in reg[2]:
          areas[x][y] = day
          pts.add((x, y))
          
      # for r in areas:
      #   print(r)
        
      # print(pts, border_pts)
      curr_borders = defaultdict(set)
      borders = defaultdict(set)
      border_ln = defaultdict(int)
        
      # mark the map, union regions
      for x, y in pts:
        key = find(x, y)
        
        for dx, dy in dirs:
          x0, y0 = x+dx, y+dy
          if x0 < 0 or x0 >= m or y0 < 0 or y0 >= n:
            continue
            
          # print('check para:', x, y, x0, y0, areas[x0][y0])
          if not areas[x0][y0]:
            # increase the outer-border and the wall length
            curr_borders[key].add((x, y))
            borders[key].add((x0, y0))
            border_ln[key] += 1
            
          elif (x0, y0) not in walled:
            # don't union the region with a previously
            # walled region
            union(x, y, x0, y0)
            
      remove = set()
      keys = list(border_ln.keys())
      # print(border_ln, find_key(21))
      
      for k in keys:
        real_key = find_key(k)
        if real_key != k:
          curr_borders[real_key] |= curr_borders[k]
          borders[real_key] |= borders[k]
          border_ln[real_key] += border_ln[k]
          remove.add(k)
          
      # union and expand
      regions.clear()
      for k in border_ln:
        if k in remove:
          continue
          
        regions.append((len(borders[k]), border_ln[k], borders[k], curr_borders[k]))
        # print('region:', k, border_ln[k])
      
    # build init regions
    for i in range(m):
      for j in range(n):
        if (i, j) in infected or not areas[i][j]:
          continue
          
        init_regions(i, j)
    
    # print(regions)
    if len(regions) == 0:
      return 0
    
    if len(regions) == 1:
      return regions[0][1]

    # each day, as long as there are uncontained infection
    # regions, continue the spread
    day = 2
    while regions:
      spread(day)
      day += 1
      
    return walls
    