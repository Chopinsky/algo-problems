from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet
# Write any import statements here

'''
Mathematical Art

the idea is to use a swiping line to count the number of intersections of the vertical swiping
line and the horizontal lines that are in the range:
1. build and merge all horizontal lines and vertical lines, and sort them;
2. build 2 stacks for the horizontal lines with its start and end, specifically; we will use 
   these 2 stacks to add/pop lines that's are possibly intersetable with the vertical swiping
   line;
3. sort the vertical lines, and go from left-to-right (primary) and top-to-bottom (secondary),
   a) add all horizontal lines that starts right at position x; 
   b) pop all horizontal lines that ends right at position x; 
   c) count all remaining lines that are between (y0, y1);
4. return the total count;
'''
def getPlusSignCount(N: int, L: List[int], D: str) -> int:
  draw = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
  }
  
  h_lines = defaultdict(list)
  v_lines = defaultdict(list)
  x, y = 0, 0
  
  # build lines
  for dist, dr in zip(L, D):
    delta = draw[dr]
    x0, y0 = x+dist*delta[0], y+dist*delta[1]
    
    # vertical stroke
    if x == x0:
      v_lines[x].append((min(y, y0), max(y, y0)))
      
    # horizontal stroke
    else:
      h_lines[y].append((min(x, x0), max(x, x0)))
      
    x, y = x0, y0
    
  # merge lines
  def merge(seg):
    if not seg:
      return set
    
    seg.sort()
    res = []
    start, end = seg[0]
    
    for x0, x1 in seg[1:]:
      if x0 > end:
        res.append((start, end))
        start, end = x0, x1
      else:
        end = max(end, x1)
    
    res.append((start, end))
    
    return res
    
  def rebuild(lines):
    res = []
    for key, seg in lines.items():
      res += [(key, start, end) for start, end in merge(seg)]
      
    return sorted(res)
  
  h_lines = rebuild(h_lines)
  v_lines = rebuild(v_lines)
  count = 0
    
  if not h_lines or not v_lines:
    return count
  
  #print(h_lines)
  #print(v_lines)
  
  def build_stacks(lines):
    start = []
    end = []
    n = len(lines)
    for y0, x0, x1 in lines:
      start.append((x0, y0))
      end.append((x1, y0))
      
    return sorted(start), sorted(end)
  
  h_start, h_end = build_stacks(h_lines)
  add, remove = 0, 0
  n = len(h_lines)
  points = SortedSet()
  #print('init:', h_start, h_end)
    
  for x0, y0, y1 in v_lines:
    while add < n and h_start[add][0] < x0:
      points.add(h_start[add][1])
      add += 1
      
    while remove < n and h_end[remove][0] <= x0:
      points.remove(h_end[remove][1])
      remove += 1
      
    i = points.bisect_right(y0)
    j = points.bisect_left(y1)
    #print('intersect:', (x0, y0, y1), (i, j), points, (add, remove))
    count += j-i
    
  return count
