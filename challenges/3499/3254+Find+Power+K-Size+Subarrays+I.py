'''
3254. Find the Power of K-Size Subarrays I
'''

from typing import List

class Solution:
  def resultsArray(self, nums: List[int], k: int) -> List[int]:
    rising = [0]
    n = len(nums)
    for i in range(1, n):
      if nums[i] == nums[i-1]+1:
        curr = rising[-1]+1
      else:
        curr = 0
        
      rising.append(curr)
      
    # print('init:', rising)
    ans = []
    
    for i in range(k-1, n):
      j = i-k+1
      if rising[i]-rising[j] == k-1:
        res = nums[i]
      else:
        res = -1
        
      ans.append(res)
      
    return ans
        