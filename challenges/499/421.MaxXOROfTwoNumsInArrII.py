'''
Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127

Constraints:

1 <= nums.length <= 2 * 10^5
0 <= nums[i] <= 2^31 - 1
'''


from typing import List


class Solution:
  def findMaximumXOR(self, nums: List[int]) -> int:
    res = 0
    l = len(bin(max(nums))) - 2
    
    # guess the results
    for i in range(l, -1, -1):
      res  = res << 1
      nxt_high = res | 1
      prefix = {num >> i for num in nums}

      # if high ^ p = x, then it means there's a 
      # number that will give us x^p = high
      for p in prefix:
        # possible to obtain the 1 for i-th digit,
        # update the results and break
        if nxt_high ^ p in prefix:
          res = res | 1
          break
                
    return res
      
    
  def findMaximumXOR0(self, nums: List[int]) -> int:
    root = {}
    
    def insert(val: int) -> int:
      curr = root
      shift = 30
      
      while shift >= 0:
        idx = (val >> shift) & 1
        if idx not in curr:
          curr[idx] = {}
          
        curr = curr[idx]
        shift -= 1
      
    def query(val: int) -> int:
      curr = root
      shift = 30
      ans = 0
      
      while shift >= 0:
        idx = 1 - ((val >> shift) & 1)
        if idx in curr:
          ans = (ans << 1) | 1
          curr = curr[idx]
        else:
          ans <<= 1
          curr = curr[1-idx]
          
        shift -= 1
        
      return ans

    res = 0
    for val in nums:
      insert(val)
      res = max(res, query(val))
      # print(val, res)
      
    # print(root)
    return res
  