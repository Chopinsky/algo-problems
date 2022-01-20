'''
Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

Return true if all the rectangles together form an exact cover of a rectangular region.

Example 1:

Input: rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Output: true
Explanation: All 5 rectangles together form an exact cover of a rectangular region.
Example 2:


Input: rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
Output: false
Explanation: Because there is a gap between the two rectangular regions.
Example 3:


Input: rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
Output: false
Explanation: Because two of the rectangles overlap with each other.
 

Constraints:

1 <= rectangles.length <= 2 * 10^4
rectangles[i].length == 4
-10^5 <= xi, yi, ai, bi <= 10^5
'''


from typing import List
from collections import deque


class Solution:
  def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
    total_area = 0
    corners = set()
    
    for l, b, r, u in rectangles:
      # the total areas of all rectangles
      total_area += (r - l) * (u - b)
      
      # for a perfect rectangle, corners will appear 2 or 4 times,
      # except the global corners, which appear only once; toggle
      # the corners from this rectangle in/out of the all-corners-set
      corners ^= {(l, b), (l, u), (r, b), (r, u)} 
    
    # we should only have global corners left
    if len(corners) != 4:
      return False
    
    # all the corners should form into 2 groups: a pair of xs, and 
    # a pair of ys
    set_x, set_y = set(), set()
    for x, y in list(corners):
      set_x.add(x)
      set_y.add(y)
      
    # if there are values other than the pair of xs and pair of ys, 
    # this is not valid
    if len(set_x) != 2 or len(set_y) != 2:
      return False
    
    # check if the total area of the final rectangle matches that of
    # all rectangles combined -- meaning we should not have gaps or 
    # overlapps
    x1, x2 = list(set_x)
    y1, y2 = list(set_y)
    return abs(x1-x2) * abs(y1-y2) == total_area
      
      
  def isRectangleCover0(self, rectangles: List[List[int]]) -> bool:
    b = []
    for x0, y0, x1, y1 in rectangles:
      b.append((x0, 1, y0, y1))
      b.append((x1, -1, y0, y1))
      
    b.sort()
    # print(b)
    
    curr_line = deque([])
    idx, n = 0, len(b)
    low, high = None, None
    
    # if the front blocks match
    while idx < n and b[idx][1] > 0:
      if low is None:
        low, high = b[idx][2:]
      else:
        if b[idx][2] != high:
          # print('fail 0')
          return False
        
        high = b[idx][3]
        
      idx += 1
      
    # print('front done', idx, low, high)

    # loop over all start/end lines, and make sure they
    # all match
    while idx < n:
      pos = b[idx][0]
      
      while idx < n and b[idx][1] < 0:
        # a misplaced line, false
        if b[idx][0] != pos:
          print('fail 1')
          return False
        
        if not curr_line or b[idx][2] != curr_line[-1][1]:
          curr_line.append(list(b[idx][2:]))
        else:
          curr_line[-1][1] = b[idx][3]
        
        # print(pos, 'build exit lines:', curr_line, b[idx])
        idx += 1
        
      # print(pos, 'exit lines:', curr_line, idx)
        
      # now match the entered lines with the exited lines
      while idx < n and b[idx][1] > 0:
        # a misplaced line, false
        if b[idx][0] != pos:
          # print('fail-2')
          return False
        
        y0, y1 = b[idx][2:]
        while curr_line and y0 < y1:
          # this new block will not match with the missing
          # ones
          if y0 != curr_line[0][0] or y1 > curr_line[-1][1]:
            # print('fail-3', y0, y1, b[idx])
            return False
          
          if curr_line[0][1] <= y1:
            y0 = curr_line[0][1]
            curr_line.popleft()
          else:
            y0 = y1
            curr_line[0][0] = y1
            
        # this new block will have unsolved hight
        if y0 < y1:
          # print('fail 4')
          return False
        
        # print(pos, 'match end', y0, y1, curr_line)
        idx += 1
      
      # print(pos, 'enter lines fin:', curr_line)
      
      # if we have unsolved remainders
      if curr_line and idx < n:
        # print('fail 5')
        return False
      
    # print('fin exit', curr_line, low, high)
    return len(curr_line) == 1 and curr_line[0][0] == low and curr_line[0][1] == high
    