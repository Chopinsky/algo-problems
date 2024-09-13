from typing import List

class Solution:
  '''
  the sum is essentially: i1*(v1-v0) + i2*(v2-v1) + i3*(v3-v2) + ... + vn1*(vn1-vn0), so we 
  will get the maximum scores by doing the jump i->j where nums[j] > nums[i]
  '''
  def findMaximumScore(self, nums: List[int]) -> int:
    n = len(nums)
    scores = {n-1:0}
    stack = [(nums[-1], n-1)]
    
    for i in range(n-2, -1, -1):
      val = nums[i]
      while stack and stack[-1][0] <= val:
        stack.pop()
        
      if not stack:
        score = (n-1-i) * val
      else:
        j = stack[-1][1]
        score = scores[j] + (j-i) * val
        
      scores[i] = score
      stack.append((val, i))
      
    # print(scores)
    return scores[0]
        