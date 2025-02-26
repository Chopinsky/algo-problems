'''
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.
Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.
Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:

n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
'''

from typing import List

class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    nums.sort()
    n = len(nums[0])
    base = '0'*n

    if nums[0] != base:
      return base

    # print('init:', nums)
    prev = 0

    def to_num(s: str):
      i = n-1
      val = 0
      mask = 1

      while i >= 0:
        if s[i] == '1':
          val |= mask

        mask <<= 1
        i -= 1

      return val

    for val in nums[1:]:
      curr = to_num(val)
      if curr != prev+1:
        s = bin(prev+1)[2:]
        s = '0'*(n-len(s)) + s
        # print('end:', prev+1, curr, s)
        return s

      prev = curr

    return '1'*n

      
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    val = 1
    n = len(nums[0])
    base = set(nums)
    
    while val < (1<<n):
      s = bin(val)[2:]
      n0 = len(s)
      s0 = '0'*(n-n0) + s
      if s0 not in base:
        return s0
      
      val += 1
    
    return '0'*n
        
        
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    n = len(nums)
    if n == 1:
      return '0' if nums[0] == '1' else '1'
    
    nums.sort()
    # print(nums)

    if nums[0] != '0' * n:
      return '0' * n
    
    for i in range(1, len(nums)):
      last = int(nums[i-1], 2)  
      curr = int(nums[i], 2)
      # print(i, last, curr)
      
      if last+1 == curr:
        continue
        
      base = last + 1
      res = ''
      mask = 1 << (n-1)
      
      while mask > 0:
        if base & mask > 0:
          res += '1'
        else:
          res += '0'
          
        mask >>= 1
      
      return res
    
    return '1' * n
    