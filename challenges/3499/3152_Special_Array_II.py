'''
3152. Special Array II
'''

from typing import List

class Solution:
  def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    prefix = [0]
    for i in range(1, len(nums)):
      v0, v1 = nums[i-1], nums[i]
      change = 1 if (v0%2)+(v1%2) == 1 else 0
      prefix.append(prefix[-1]+change)
      
    ans = []
    for l, r in queries:
      if l == r:
        ans.append(True)
        continue
        
      ln = r-l
      count = prefix[r]-prefix[l]
      ans.append(count == ln)
    
    return ans
        