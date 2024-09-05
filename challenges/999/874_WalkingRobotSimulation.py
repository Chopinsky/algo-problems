'''
A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
Example 3:

Input: commands = [6,-1,-1,6], obstacles = []
Output: 36
Explanation: The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.

Constraints:

1 <= commands.length <= 10^4
commands[i] is either -2, -1, or an integer in the range [1, 9].
0 <= obstacles.length <= 10^4
-3 * 10^4 <= xi, yi <= 3 * 10^4
The answer is guaranteed to be less than 2^31.
'''

from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right

class Solution:
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    rows = defaultdict(list)
    cols = defaultdict(list)
    
    for x, y in obstacles:
      rows[y].append(x)
      cols[x].append(y)
      
    for r in rows:
      rows[r].sort()
      
    for c in cols:
      cols[c].sort()
      
    # print('init:', rows, cols)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr = 0
    x, y = 0, 0
    
    def vert(x0: int, y0: int, y1: int):
      if x0 not in cols or y0 == y1:
        return y1
      
      col = cols[x0]
      if y0 < y1:
        # move north
        idx = bisect_right(col, y0)
        if idx < len(col) and col[idx] <= y1:
          y1 = col[idx]-1
      
      # move south
      else:
        idx = bisect_left(col, y0) - 1
        if idx >= 0 and col[idx] >= y1:
          y1 = col[idx]+1
      
      return y1
      
    def hor(x0: int, y0: int, x1: int):
      if y0 not in rows or x0 == x1:
        return x1
      
      row = rows[y0]
      if x0 < x1:
        # move east
        idx = bisect_right(row, x0)
        if idx < len(row) and row[idx] <= x1:
          x1 = row[idx]-1
          
      else:
        # move west
        idx = bisect_left(row, x0) - 1
        if idx >= 0 and row[idx] >= x1:
          x1 = row[idx]+1
      
      return x1
    
    dist = 0
    for cmd in commands:
      if cmd == -1:
        curr = (curr + 1) % 4
        continue
        
      if cmd == -2:
        curr = (curr + 3) % 4
        continue
        
      dx, dy = dirs[curr]
      tx, ty = x+cmd*dx, y+cmd*dy
      
      if dx == 0:
        y = vert(x, y, ty)
        x = tx
        
      else:
        x = hor(x, y, tx)
        y = ty
        
      dist = max(dist, x*x+y*y)
      # print('move:', cmd, (x, y))
      
    return dist
    
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    curr = 0
    x, y = 0, 0
    dist = 0
    obs = set([(x, y) for x, y in obstacles])
    
    for c in commands:
      if c == -2:
        curr -= 1
        if curr < 0:
          curr += 4
          
        continue
        
      if c == -1:
        curr += 1
        if curr >= 4:
          curr -= 4
          
        continue
        
      dx, dy = dirs[curr]
      while c > 0:
        x0, y0 = x+dx, y+dy
        if (x0, y0) in obs:
          break
          
        x, y = x0, y0
        dist = max(dist, x*x + y*y)
        c -= 1
        
    return dist
        