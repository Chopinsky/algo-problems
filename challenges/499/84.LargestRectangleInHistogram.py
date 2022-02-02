'''
Given an array of integers heights representing the histogram's bar 
height where the width of each bar is 1, return the area of the largest 
rectangle in the histogram.

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 10^5
0 <= heights[i] <= 10^4
'''


from typing import List


class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    # make sure the last entry will pop all heights in the stack
    heights.append(0)
    # the init x-coordinate
    stack = [-1]
    area = 0
    n = len(heights)
    
    for i in range(n):
      while heights[stack[-1]] > heights[i]:
        j = stack.pop()
        # calc the rectangle area to the back, i.e. from 
        # [stack[-1], i), with heights[j] be the height 
        # of the rectangle
        area = max(area, heights[j] * (i-stack[-1]-1))
          
      stack.append(i)
        
    return area

  
  def largestRectangleArea0(self, heights: List[int]) -> int:
    stack = []
    area = 0
    n = len(heights)
    
    for i, h in enumerate(heights):
      if not stack:
        area = max(area, h)
        stack.append((h, i))
        continue
        
      j = i
      while stack and stack[-1][0] >= h:
        h0, j = stack.pop()
        area = max(area, h0 * (i-j))

      stack.append((h, j))
    
    for h, j in stack:
      area = max(area, h * (n-j))
      
    return area
  