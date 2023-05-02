'''
2662. Minimum Cost of a Path With Special Roads

You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

Example 1:

Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
- (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
- (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
- (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
So the total cost is 1 + 2 + 1 + 1 = 5.
It can be shown that we cannot achieve a smaller total cost than 5.
Example 2:

Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.

Constraints:

start.length == target.length == 2
1 <= startX <= targetX <= 10^5
1 <= startY <= targetY <= 10^5
1 <= specialRoads.length <= 200
specialRoads[i].length == 5
startX <= x1i, x2i <= targetX
startY <= y1i, y2i <= targetY
1 <= costi <= 10^5
'''

from typing import List
from heapq import heappop, heappush


class Solution:
  def minimumCost(self, start: List[int], target: List[int], roads: List[List[int]]) -> int:
    def calc(x0, y0, x1, y1):
      return abs(y1-y0) + abs(x1-x0)
    
    roads = [(x0, y0, x1, y1, d) for x0, y0, x1, y1, d in roads if d < calc(x0, y0, x1, y1)]
    sx, sy = start
    tx, ty = target
    cost = calc(sx, sy, tx, ty)
    costs = {(sx, sy): 0}
    stack = [(0, sx, sy)]
    # print('init:', cost)
    
    while stack:
      d, x, y = heappop(stack)
      for x0, y0, x1, y1, d0 in roads:
        d1 = d + d0 + calc(x, y, x0, y0)
        if d1 >= cost:
          continue
        
        if (x1, y1) not in costs or costs[x1, y1] > d1:
          costs[x1, y1] = d1
          heappush(stack, (d1, x1, y1))
          
    for x0, y0, x1, y1, d0 in roads:
      if (x1, y1) not in costs:
        continue
        
      cost = min(cost, costs[x1, y1] + calc(x1, y1, tx, ty))
          
    return cost
    