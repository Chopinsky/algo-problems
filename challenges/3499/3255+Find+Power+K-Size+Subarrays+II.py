'''
3255. Find the Power of K-Size Subarrays II
'''

from typing import List

class Solution:
  def resultsArray(self, nums: List[int], k: int) -> List[int]:
    ans = []
    prefix = [1]
    n = len(nums)
    
    for i in range(1, n):
      if nums[i] == nums[i-1] + 1:
        prefix.append(prefix[-1]+1)
      else:
        prefix.append(1)
        
    # print('init:', prefix)
    for i in range(k-1, n):
      ln = prefix[i] - prefix[i-k+1] + 1
      if ln == k:
        ans.append(nums[i])
      else:
        ans.append(-1)
    
    return ans
        