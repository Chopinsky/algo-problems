'''
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:

1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1
'''

from typing import List

class Solution:
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort(key=lambda x: (x[1], x[0]))
    last = points[0][1]
    count = 1
    # print(points)
    
    for x, y in points[1:]:
      if x <= last:
        continue
        
      count += 1
      last = y
      # print('shoot:', last)
    
    return count
        
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort()
    count, idx = 0, 0
    n = len(points)
    
    while idx < n:
      right = points[idx][1]
      # print('start:', idx, points[idx])
      
      while idx+1 < n and points[idx+1][0] <= right:
        idx += 1
        right = min(right, points[idx][1])
      
      # print('end:', idx, points[idx])
      count += 1
      idx += 1
    
    return count

    
  def findMinArrowShots(self, points: List[List[int]]) -> int:
    points.sort()
    lb, rb = points[0][0], points[0][1]
    count = 0
    
    for l, r in points[1:]:
      if l > rb:
        count += 1
        rb = r
      
      lb = l
      if r < rb:
        rb = r
        
      # print(l, r, rng)  
      
    if lb >= 0:
      count += 1
      
    return count
    