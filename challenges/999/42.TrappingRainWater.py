'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:

n == height.length
0 <= n <= 3 * 10 ** 4
0 <= height[i] <= 10 ** 5
'''


from typing import List


class Solution:
  def trap(self, height: List[int]) -> int:
    stack = []
    ln = len(height)
    start = 0
    count = 0
    
    while start < ln and height[start] == 0:
      start += 1
      
    for i in range(start, ln):
      h = height[i]
      if len(stack) > 0 and h == stack[-1][0]:
        stack[-1][1] = i
        continue
        
      while len(stack) > 0 and h > stack[-1][0]:
        curr = stack.pop()
        
        if len(stack) > 0:
          top = min(stack[-1][0], h)
          # print("popped:", i, h, curr, top, stack[-1], (top - curr[0]) * (i - stack[-1][1] - 1))
          count += (top - curr[0]) * (i - stack[-1][1] - 1)
          
      # print(i, h, count)
      
      if len(stack) == 0 or h < stack[-1][0]:
        stack.append([h, i])
      elif len(stack) > 0 and h == stack[-1][0]:
        stack[-1][1] = i
    
    return count
  