'''
You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].


You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.

Example 1:


Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
Example 2:

Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.
Example 3:


Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.
 

Constraints:

1 <= points.length <= 105
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100
'''


from typing import List
from math import atan2, pi
from heapq import heappop, heappush


class Solution:
  def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
    x0, y0 = location
    p = []
    spot_on = 0
    
    for x, y in points:
      if x == x0 and y == y0:
        spot_on += 1
        continue
        
      deg = 180 * atan2(y-y0, x-x0) / pi
      if deg < 0:
        deg += 360
        
      p.append(deg)
    
    if not p:
      return spot_on
    
    p.sort()
    stack = [p[0]]
    count = 1 + spot_on
    
    for i in range(len(p)):
      if p[i] - p[0] > angle:
        break
        
      p.append(360+p[i])
      
    n = len(p)
    i = 1
    # print(p)
    
    while i < n:
      while stack and p[i] - stack[0] > angle:
        heappop(stack)
        
      while i < n and (not stack or p[i] - stack[0] <= angle):
        # print('add', i, p[i], stack)
        heappush(stack, p[i])  
        i += 1

      # update in-view-points count
      count = max(count, len(stack) + spot_on)
      # print(i, spot_on, count, stack)
    
    return count
  