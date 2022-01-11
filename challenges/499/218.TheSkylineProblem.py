'''
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

lefti is the x coordinate of the left edge of the ith building.
righti is the x coordinate of the right edge of the ith building.
heighti is the height of the ith building.
You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

Example 1:


Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:

1 <= buildings.length <= 10^4
0 <= lefti < righti <= 2^31 - 1
1 <= heighti <= 2^31 - 1
buildings is sorted by lefti in non-decreasing order.
'''


from typing import List
from heapq import heappop, heappush


class Solution:
  def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    # add start-building events, also add end-building events(acts as 
    # buildings with 0 height) and sort the events in left -> right order
    heights = [(l, -h, r) for l, r, h in buildings] + list({(r, 0, -1) for _, r, _ in buildings})
    heights.sort()
    
    # res: result, [x, height]
    # live: heap, [-height, endingPosition]
    res = []
    heap = [(0, float('inf'))]
    
    for start, height, end in heights:
      # pop any buildings that's already ended
      while start >= heap[0][1]:
        heappop(heap)
      
      # add the start of a building
      if height > 0:
        heappush(heap, (height, end))
      
      # if a building is appearing but not the last recorded
      # height, add it to the result
      if not res or res[-1][1] != -heap[0][0]:
        res.append([start, -heap[0][0]])

      return res


  def getSkyline0(self, buildings: List[List[int]]) -> List[List[int]]:
    b = []
    for i, [s, e, h] in enumerate(buildings):
      b.append((s, 0, -h, i))
      b.append((e, 1, h, i))
      
    b.sort()
    ans = []
    stack = []
    ended = set()
    curr_h = 0
    # print(b)
    
    for pt, typ, h, idx in b:
      h = -h if typ == 0 else h
      
      if typ == 1:
        ended.add(idx)
        # print('end:', idx, pt, stack)
        
      while stack and stack[0][1] in ended:
        heappop(stack)
      
      if typ == 1 and not stack:
        ans.append([pt, 0])
        curr_h = 0
      
      if typ == 0:
        heappush(stack, (-h, idx))
        
      if stack and curr_h != -stack[0][0]:
        curr_h = -stack[0][0]
        ans.append([pt, curr_h])
      
    return ans
