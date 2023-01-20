'''
Given an integer array nums, return all the different possible increasing subsequences of the given array with at least two elements. You may return the answer in any order.

The given array may contain duplicates, and two equal integers should also be considered a special case of increasing sequence.

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100
'''

from typing import List


class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    store = set()
    nxt = set()
    
    for val in nums:
      nxt.clear()
      for arr in store:
        if val >= arr[-1]:
          nxt.add(arr + (val, ))
      
      store.add((val, ))
      store |= nxt
    
    return [list(arr) for arr in store if len(arr) > 1]
    
    
  def findSubsequences(self, nums):
    subs = {()}
    for num in nums:
      subs |= {sub + (num,) for sub in subs if not sub or sub[-1] <= num}
      
    return [sub for sub in subs if len(sub) >= 2]
      
      
  def findSubsequences0(self, nums: List[int]) -> List[List[int]]:
    arr = []
    seen = set()
    
    for val in nums:
      nxt = [[val]]
      for a in arr:
        if val >= a[-1]:
          a0 = a + [val]
          b0 = tuple(a0)
          if b0 in seen:
            continue
            
          nxt.append(a0)
          seen.add(b0)
          
      arr += nxt
      
    res = []
    for a in arr:
      if len(a) >= 2:
        res.append(a)
        
    return res
    