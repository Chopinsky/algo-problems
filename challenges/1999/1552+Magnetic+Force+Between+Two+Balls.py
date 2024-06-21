'''
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Example 1:


Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:

Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.
 

Constraints:

n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
'''

from typing import List

class Solution:
  def maxDistance(self, pos: List[int], m: int) -> int:
    if m > len(pos):
      return 0
    
    pos.sort()
    if m == 2:
      return pos[-1] - pos[0]
    
    def check(dist: int) -> bool:
      # place the first ball @ pos[0]
      cnt = m-1
      prev = pos[0]
      
      for p in pos[1:]:
        if p-prev >= dist:
          cnt -= 1
          prev = p
        
        if cnt <= 0:
          break
      
      return cnt <= 0
    
    l, r = 1, pos[-1]
    last = 1
    
    while l <= r:
      mid = (l+r)//2
      if check(mid):
        l = mid+1
        last = mid
      else:
        r = mid-1
        
    return last
        
  def maxDistance(self, pos: List[int], m: int) -> int:
    pos.sort()
    if m == 2:
      return pos[-1] - pos[0]
    
    n = len(pos)
    if m == n:
      return min([pos[i]-pos[i-1] for i in range(1, n)])
    
    def balls_dist(d: int) -> bool:
      i, cnt = 0, 1
      
      for j in range(1, n):
        if cnt >= m:
          break
        
        # place a ball at position-j
        if pos[j] - pos[i] >= d:
          # if d == 4:
            # print('put:', d, i, j)
            
          i = j
          cnt += 1
        
      return cnt >= m
    
    l, r = 1, pos[-1]-pos[0]
    last = 1
    
    while l < r:
      mid = (l + r) // 2
      # print(l, r, mid, balls_dist(mid))
      
      if balls_dist(mid):
        last = mid
        l = mid + 1
      else:
        r = mid - 1
        
    # print('final:', l, last)
    return max(last, l) if balls_dist(l) else last
  