'''
We are given a list of (axis-aligned) rectangles. Each rectangle[i] = [xi1, yi1, xi2, yi2] , where (xi1, yi1) are the coordinates of the bottom-left corner, and (xi2, yi2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.

Example 2:

Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 1018 modulo (109 + 7), which is (109)2 = (-7)2 = 49.

Constraints:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10 ** 9
The total area covered by all rectangles will never exceed 263 - 1 and thus will fit in a 64-bit signed integer.
'''


from typing import List
from collections import defaultdict
from bisect import bisect_left, bisect_right


class Solution:
  def rectangleArea(self, rec: List[List[int]]) -> int:
    events = []
    for x0, y0, x1, y1 in rec:
      events.append((x0, y0, y1, 0))
      events.append((x1, y0, y1, 1))
      
    events.sort()
    heights = defaultdict(int)
    # print(events)
    
    # calculate the heights of rectangles inside the given
    # rec ranges
    def get_heights() -> int:
      total = 0
      curr = None
      
      for l, h in sorted(heights.keys()):
        if not curr:
          curr = [l, h]
          continue
          
        if l <= curr[1]:
          curr[1] = max(curr[1], h)
          continue
          
        total += curr[1] - curr[0]
        curr[0] = l
        curr[1] = h
        
      if curr:
        total += curr[1] - curr[0]
        
      return total
      
    last = -1
    ans = 0
    
    for x, y0, y1, evt in events:
      # init event, record and continue
      if last < 0:
        last = x
        heights[y0, y1] += 1
        continue
        
      # before applying the new event, calculate the rec area
      # in the current range
      ans += (x-last) * get_heights()
      last = x
      
      if evt == 0:
        # adding a new y-section
        heights[y0, y1] += 1
      else:
        # removing an old y-section that's out of the bound
        heights[y0, y1] -= 1
        if not heights[y0, y1]:
          heights.pop((y0, y1))
    
    return ans % (10 ** 9 + 7)


  def rectangleArea0(self, rec: List[List[int]]) -> int:
    xs_set = set()
    for r in rec:
      xs_set.add(r[0])
      xs_set.add(r[2])
      
    xs = sorted(xs_set)
    recs = defaultdict(set)
    # print(xs)
    
    for x0, y0, x1, y1 in rec:
      l, r = bisect_left(xs, x0), bisect_right(xs, x1)
      bounds = xs[l:r]
      # print(bounds)
      
      for i in range(len(bounds)-1):
        lb, rb = bounds[i], bounds[i+1]
        recs[lb, rb].add((y0, y1))
      
    ans = 0
    for xr, yr in recs.items():
      dx = xr[1] - xr[0]
      curr = None
      # print(xr, yr)

      for rng in sorted(yr):
        if not curr:
          curr = rng
          continue
          
        if rng[0] <= curr[1]:
          curr = (curr[0], max(curr[1], rng[1]))
          continue
          
        ans += dx * (curr[1]-curr[0])
        curr = rng
      
      if curr:
        ans += dx * (curr[1]-curr[0])
    
    return ans % (1_000_000_007)
