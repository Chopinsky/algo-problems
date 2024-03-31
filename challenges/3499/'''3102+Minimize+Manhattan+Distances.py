'''
3102. Minimize Manhattan Distances

You are given a 0-indexed array points representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

The distance between two points is defined as their Manhattan distance.

Return the minimum possible value for maximum distance between any two points by removing exactly one point.

Example 1:

Input: points = [[3,10],[5,15],[10,2],[4,4]]
Output: 12
Explanation: The maximum distance after removing each point is the following:
- After removing the 0th point the maximum distance is between points (5, 15) and (10, 2), which is |5 - 10| + |15 - 2| = 18.
- After removing the 1st point the maximum distance is between points (3, 10) and (10, 2), which is |3 - 10| + |10 - 2| = 15.
- After removing the 2nd point the maximum distance is between points (5, 15) and (4, 4), which is |5 - 4| + |15 - 4| = 12.
- After removing the 3rd point the maximum distance is between points (5, 15) and (10, 2), which is |5 - 10| + |15 - 2| = 18.
It can be seen that 12 is the minimum possible maximum distance between any two points after removing exactly one point.
Example 2:

Input: points = [[1,1],[1,1],[1,1]]
Output: 0
Explanation: It can be seen that removing any of the points results in the maximum distance between any two points of 0.

Constraints:

3 <= points.length <= 10^5
points[i].length == 2
1 <= points[i][0], points[i][1] <= 10^8
'''

from typing import List
from collections import defaultdict
import math

testCases = [
  [[4,1],[10,7],[5,6],[3,2],[10,9],[2,9],[2,8]],
  [[3,10],[5,15],[10,2],[4,4]],
  [[1,1],[1,1],[1,1]],
]

class Solution:
  '''
  the core idea is that for any 2 points, the manhattan distance is 
    d[0,1] = max(
       x0-x1+y0-y1,
       x0-x1-y0+y1,
      -x0+x1+y0-y1,
      -x0+x1-y0+y1,
    )

  this is equivalent to this formula:
    d[0,1] = max(
      (x0+y0) - (x1+y1),
      (x1+y1) - (x0+y0),
      (x0-y0) - (x1-y1),
      (x1-y1) - (x0-y0),
    )

  and it can be furth simplified:
    d[0, 1] = max(
      max((x0+y0), (x1+y1)) - min((x0+y0), (x1+y1)),
      max((x0-y0), (x1-y1)) - min((x0-y0), (x1-y1)),
    )
  
  so the max manhanttan dist among all point-pairs are:
    d_max = max(
      max(point_x_plus_y) - min(point_x_plus_y),
      max(point_x_minus_y) - min(point_x_minus_y),
    )

  and we can test if removing any point in the array would change
  the value of <d_max>, and take the minimum possible <d_max>
  after all possible point-removals.
  '''
  def minimumDistance(self, points: List[List[int]]) -> int:
    plus = defaultdict(set)
    minus = defaultdict(set)
    
    for i, (x, y) in enumerate(points):
      plus[x+y].add(i)
      minus[x-y].add(i)
    
    cp = sorted(plus)
    cm = sorted(minus)
    # print('init-0:', plus, cp)
    # print('init-1:', minus, cm)
    
    def calc_dist(dic, cand):
      high, low = cand[-1], cand[0]
      val0 = cand[-2] if i in dic[high] and len(dic[high]) == 1 else high
      val1 = cand[1] if i in dic[low] and len(dic[low]) == 1 else low
      return val0 - val1
    
    def max_dist_except(i: int):
      d0 = 0
      if len(cp) > 1:
        d0 = max(d0, calc_dist(plus, cp))
      
      if len(cm) > 1:
        d0 = max(d0, calc_dist(minus, cm))
        
      return d0
      
    dist = math.inf
    for i in range(len(points)):
      dist = min(dist, max_dist_except(i))
      
    return dist
        