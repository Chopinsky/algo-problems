'''
There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).

We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.

Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: Because there are no blocked cells, it is possible to reach the target square.
 

Constraints:

0 <= blocked.length <= 200
blocked[i].length == 2
0 <= xi, yi < 106
source.length == target.length == 2
0 <= sx, sy, tx, ty < 106
source != target
It is guaranteed that source and target are not blocked.
'''


class Solution:
  '''
  has to fast forward if possible, key is to find if either source or target is encircled. 
  '''
  def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
    if not blocked:
      return True
    
    blocks = set(tuple(b) for b in blocked)
    m, n = 1_000_000, 1_000_000
    s_seen = set([tuple(source)])
    t_seen = set([tuple(target)])
    
    rows, cols = defaultdict(list), defaultdict(list)
    for x, y in blocked:
      rows[x].append(y)
      cols[y].append(x)
      
    for k in rows:
      rows[k].sort()
      
    for k in cols:
      cols[k].sort()
    
    def expand(src: List[int], last: Set[int], curr: Set[int]) -> int:
      stack = [tuple(src)]
      exit_found = False
      
      while stack:
        x, y = stack.pop()
        
        # an exit exists
        if (x not in rows) or (y not in cols):
          return 0
        
        # we can reach a point that's not possible to encircle
        if (y < rows[x][0] and (y+1) + min(x, m-1-x) >= 200) or (y > rows[x][-1] and (n-1-y) + min(x, m-1-x) >= 200):
          return 0
        
        # we can reach a point that's not possible to encircle
        if (x < cols[y][0] and (x+1) + min(y, n-1-y) >= 200) or (x > cols[y][-1] and (m-1-x) + min(y, n-1-y) >= 200):
          return 0
        
        if x-src[0] >= 200 or y-src[1] >= 200:
          exit_found = True
          return 0
        
        # find next interesting points in rows
        j = bisect_left(rows[x], y)
        if j < len(rows[x]):
          y0 = rows[x][j] - 1
          if (x, y0) in last:
            return 1
          
          if (x, y0) not in curr:
            curr.add((x, y0))
            stack.append((x, y0))
            
        else:
          for y0 in range(y+1, n):
            if (x, y0) in last:
              return 1

            if (x, y0) not in curr:
              curr.add((x, y0))
              stack.append((x, y0))
            
        if j > 0:
          y0 = rows[x][j-1] + 1
          if (x, y0) in last:
            return 1
          
          if (x, y0) not in curr:
            curr.add((x, y0))
            stack.append((x, y0))
            
        else:
          for y0 in range(y):
            if (x, y0) in last:
              return 1

            if (x, y0) not in curr:
              curr.add((x, y0))
              stack.append((x, y0))

        # find next interesting points in cols
        i = bisect_left(cols[y], x)
        if i < len(cols[y]):
          x0 = cols[y][i] - 1
          if (x0, y) in last:
            return 1
          
          if (x0, y) not in curr:
            curr.add((x0, y))
            stack.append((x0, y))
        
        else:
          for x0 in range(x+1, m):
            if (x0, y) in last:
              return 1

            if (x0, y) not in curr:
              curr.add((x0, y))
              stack.append((x0, y))
            
        if i > 0:
          x0 = cols[y][i-1] + 1
          if (x0, y) in last:
            return 1
          
          if (x0, y) not in curr:
            curr.add((x0, y))
            stack.append((x0, y))
        
        else:
          for x0 in range(x):
            if (x0, y) in last:
              return 1

            if (x0, y) not in curr:
              curr.add((x0, y))
              stack.append((x0, y))
        
      return 0 if exit_found else -1
        
    res = expand(source, t_seen, s_seen)
    # print('from source:', res, s_seen)
    
    if res > 0:
      return True
    
    if res < 0:
      return False
    
    res = expand(target, s_seen, t_seen)
    # print('from target:', res, t_seen)
    
    if res >= 0:
      return True
    
    return False
  
