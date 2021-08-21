'''
You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.

Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 points) 
----> [1, 3, 3, 3, 1] (1*1=1 points) 
----> [1, 1] (3*3=9 points) 
----> [] (2*2=4 points)

Example 2:

Input: boxes = [1,1,1]
Output: 9

Example 3:

Input: boxes = [1]
Output: 1
 

Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100
'''


from typing import List
from functools import cache


class Solution:
  def removeBoxes(self, boxes: List[int]) -> int:
    '''
    l, r represents the boxes[l:r], and k represents the number of boxes that are
    the same as boxes[l] and before l; which means @ position l, there will be k+1 
    boxes with the same number of boxes[l] that we want to merge.
    '''
    @cache
    def dp(l: int, r: int, k: int) -> int:
      if l > r:
        return 0
      
      # count all boxes that are the same color of boxes[l]
      while l < r and boxes[l] == boxes[l+1]:
        l += 1
        k += 1
        
      # k is the number of boxes with the same number *before* boxes[l], so 
      # total of (k+1) boxes that we will remove after taking care of the 
      # boxes[l+1:r] region
      ans = (k+1)*(k+1) + dp(l+1, r, 0)
      
      # keep the (k+1) boxes from this round, remove the middle boxes[l+1:m-1],
      # then merge these boxes with boxes we can get from the boxes[m:r] range
      for m in range(l+1, r+1):
        if boxes[l] == boxes[m]:
          ans = max(ans, dp(l+1, m-1, 0) + dp(m, r, k+1))
      
      return ans
    
    return dp(0, len(boxes)-1, 0)
  
        