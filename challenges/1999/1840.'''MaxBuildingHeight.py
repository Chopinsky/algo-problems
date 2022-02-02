'''
You want to build n new buildings in a city. The new buildings will be built in a line and are labeled from 1 to n.

However, there are city restrictions on the heights of the new buildings:

The height of each building must be a non-negative integer.
The height of the first building must be 0.
The height difference between any two adjacent buildings cannot exceed 1.
Additionally, there are city restrictions on the maximum height of specific buildings. These restrictions are given as a 2D integer array restrictions where restrictions[i] = [idi, maxHeighti] indicates that building idi must have a height less than or equal to maxHeighti.

It is guaranteed that each building will appear at most once in restrictions, and building 1 will not be in restrictions.

Return the maximum possible height of the tallest building.

Example 1:

Input: n = 5, restrictions = [[2,1],[4,1]]
Output: 2
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,1,2], and the tallest building has a height of 2.

Example 2:

Input: n = 6, restrictions = []
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,4,5], and the tallest building has a height of 5.

Example 3:

Input: n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
Output: 5
Explanation: The green area in the image indicates the maximum allowed height for each building.
We can build the buildings with heights [0,1,2,3,3,4,4,5,4,3], and the tallest building has a height of 5.

Constraints:

2 <= n <= 10^9
0 <= restrictions.length <= min(n - 1, 10^5)
2 <= idi <= n
idi is unique.
0 <= maxHeighti <= 10^9
'''


from typing import List


class Solution:
  '''
  the key is to construct the building height limits from both end: first
  scan from left to right to establish the height limits for each restriction
  section; then scan from right to left, and reset the height limits. last step
  is to update the tallest building height from each section we visited.
  '''
  def maxBuilding(self, n: int, restr: List[List[int]]) -> int:
    if not restr:
      return n-1
    
    restr.sort()
    # print(restr)
    
    # tuple section: (startH, endH) 
    section = []
    start = (1, 0)
    
    # first scan, from left to right, each section
    # will be the building heights from left to right 
    # and increamental only
    for i, h in restr:
      limit = start[1] + i - start[0] 
      section.append((start[1], max(start[1], limit-1)))
      start = (i, min(h, limit))
        
    tall = start[1] + n - start[0]
    last = start[1]
    # print(section, tall)
    
    # add the starting point (1, 0) to the restrctions
    # list
    restr = [[1, 0]] + restr
    
    # now scan from right to left, and we check the
    # height limits by comparing the 1st scan limits
    # and the 2nd scan limits, take the highest
    # height permited for the section
    for idx in range(len(section), 0, -1):
      x, y = restr[idx-1][0], restr[idx][0]
      l0, h0 = section[idx-1]
      l1, h1 = last, last + y - x - 1
      # print(x, (l0, h0), y, (l1, h1))
      
      # update building-x's height limits, and update the 
      # tallest building tally
      last = min(l0, h1+1)
      tall = max(tall, last)
      
      # if there are no buildings in between
      if y - x == 1:
        continue
        
      # tallest building from left
      if h0 <= l1+1:
        tall = max(tall, h0)
        continue
                
      # tallest building from right
      if h1 <= l0+1:
        tall = max(tall, h1)
        continue
        
      # the index at which the height will peak
      m = (x + y + l1 - l0) // 2
      tall = max(tall, l0 + m - x)
      
    # print('fin', tall, last)
    return tall
  