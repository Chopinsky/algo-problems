'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
'''

from typing import List


class Solution:
  def maxArea(self, h: List[int]) -> int:
    area = 0
    l = 0
    r = len(h)-1

    while l < r:
      container_height = min(h[l], h[r])
      area = max(area, (r-l)*container_height)
      if h[l] <= h[r]:
        l += 1
      else:
        r -= 1

    return area

  def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height)-1
    area = 0
    
    while l < r:
      h = min(height[l], height[r])
      area = max(area, (r-l)*h)

      # find the next (l, r) such that the
      # water level is higher than the current
      # level, as the container is narrower
      while height[l] <= h and l < r:
        l += 1

      while height[r] <= h and l < r:
        r -= 1
        
    return area
      
    
  def maxArea0(self, height: List[int]) -> int:
    n = len(height)
    l, r = 0, n-1
    area = 0
    
    while l < r:
      # print(l, r, height[l], height[r])
      area = max(area, (r-l) * min(height[l], height[r]))
      
      if height[l] < height[r]:
        l += 1
      elif height[r] < height[l]:
        r -= 1
      else:
        if height[l+1] <= height[r-1]:
          l += 1
        else:
          r -= 1
      
    return area
  

  def maxArea00(self, height: List[int]) -> int:
    n = len(height) 
    l, r = 0, n-1
    area = 0
    
    while l < r:
      area = max(area, (r-l) * min(height[l], height[r]))
      if l == r-1:
        break
      
      if height[l] < height[r]:
        l += 1
      elif height[l] > height[r]:
        r -= 1
      elif height[l+1] <= height[r-1]:
        l += 1
      else:
        r -= 1
    
    return area
  