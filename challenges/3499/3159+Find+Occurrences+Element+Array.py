'''
3159. Find Occurrences of an Element in an Array
'''

from typing import List

class Solution:
  def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
    arr = []
    for i in range(len(nums)):
      if nums[i] == x:
        arr.append(i)
        
    # print(arr)
    ans = []
    
    for q in queries:
      idx = q - 1
      if idx >= len(arr):
        ans.append(-1)
      else:
        ans.append(arr[idx])
        
    return ans
        