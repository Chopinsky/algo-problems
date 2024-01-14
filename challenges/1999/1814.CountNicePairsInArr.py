'''
You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.

Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
'''

from functools import lru_cache
from typing import List
from collections import defaultdict


class Solution:
  def countNicePairs(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    
    @lru_cache(None)
    def rev(val: int) -> int:
      if val <= 0:
        return val
      
      base = 0
      while val > 0:
        val, m = divmod(val, 10)
        base = 10*base + m
        
      return base
    
    c = defaultdict(int)
    for val in nums:
      r = rev(val)
      c[val-r] += 1
      # print(val, r)

    total = 0
    for cnt in c.values():
      if cnt == 1:
        continue
        
      # print(cnt)
      total = (total + cnt*(cnt-1)//2) % mod
      
    return total
  

  def countNicePairs(self, nums: List[int]) -> int:
    diff = defaultdict(int)
    count = 0
    mod = 10**9 + 7
    
    for val in nums:
      rev = int(str(val)[::-1])
      # print(val, rev)
      count = (count + diff[val-rev]) % mod
      diff[val-rev] += 1
      
    return count
      