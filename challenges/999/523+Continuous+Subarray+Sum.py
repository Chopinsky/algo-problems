'''
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
0 <= sum(nums[i]) <= 2^31 - 1
1 <= k <= 2^31 - 1
'''

from typing import List

class Solution:
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    seen_mod = {}
    prefix = 0 
    
    for idx, val in enumerate(nums):
      prefix += val
      mod = prefix % k
      if (idx > 0 and mod == 0):
        return True
      
      if mod not in seen_mod:
        seen_mod[mod] = idx
        continue
        
      if idx-seen_mod[mod] >= 2:
        return True
      
    return False
        
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    prefix = nums[0]
    store = {0: -1}
    if prefix%k > 0:
      store[prefix%k] = 0
    
    for i in range(1, len(nums)):
      prefix += nums[i]
      mod = prefix % k
      # print(i, nums[i], prefix, mod, store)
      
      if mod in store and i-store[mod] >= 2:
        return True
            
      if mod not in store:
        store[mod] = i
      
    return False
    
    
  '''
  the trick is that if the sum(nums[i:j+1]) % k == 0, then sum(nums[:i])%k == sum(nums[:j+1])%k, i.e. the
  mod of the head and tail part that intersects to form the subarray must have the same mod value to k,
  such that the formed subarray will have a mod of 0 to k.
  '''
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    if k == 1:
      return len(nums) > 1
    
    store = {0:-1}
    prefix = 0
    
    for i, val in enumerate(nums):
      prefix = (prefix + val) % k
      if prefix not in store:
        store[prefix] = i
      
      if i-store[prefix] >= 2:
        return True
      
    return False  