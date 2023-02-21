'''
2572. Count the Number of Square-Free Subsets

You are given a positive integer 0-indexed array nums.

A subset of the array nums is square-free if the product of its elements is a square-free integer.

A square-free integer is an integer that is divisible by no square number other than 1.

Return the number of square-free non-empty subsets of the array nums. Since the answer may be too large, return it modulo 109 + 7.

A non-empty subset of nums is an array that can be obtained by deleting some (possibly none but not all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:

Input: nums = [3,4,4,5]
Output: 3
Explanation: There are 3 square-free subsets in this example:
- The subset consisting of the 0th element [3]. The product of its elements is 3, which is a square-free integer.
- The subset consisting of the 3rd element [5]. The product of its elements is 5, which is a square-free integer.
- The subset consisting of 0th and 3rd elements [3,5]. The product of its elements is 15, which is a square-free integer.
It can be proven that there are no more than 3 square-free subsets in the given array.
Example 2:

Input: nums = [1]
Output: 1
Explanation: There is 1 square-free subset in this example:
- The subset consisting of the 0th element [1]. The product of its elements is 1, which is a square-free integer.
It can be proven that there is no more than 1 square-free subset in the given array.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 30
'''

from typing import List
from collections import Counter
from functools import lru_cache


class Solution:
  def shift(self, val):
    src = {2:0,3:1,5:2,7:3,11:4,13:5,17:6,19:7,23:8,29:9}
    return 1 << src.get(val, 0)
    
    
  def get_sive(self, m):
    s = [i for i in range(m)]
    base_mask = 0
    
    for i in range(2, m):
      if s[i] < i:
        continue
        
      base_mask |= self.shift(i)
      for j in range(2*i, m, i):
        if i < s[j]:
          s[j] = i
          
    return s, base_mask
    
    
  def squareFreeSubsets(self, nums: List[int]) -> int:
    mod = 10**9 + 7
    ones_combo = 1
    
    s, full_mask = self.get_sive(max(nums)+1)
    c = Counter(nums)
    
    if 1 in c:
      ones = c.pop(1)
      ones_combo = pow(2, ones, mod)
      
    cand = sorted(c)
    n = len(cand)
    # print(c, ones_combo)
    
    @lru_cache(None)
    def calc_mask(val):
      if val == 1:
        return 0
      
      mask = 0
      while val > 1:
        shift = self.shift(s[val])
        if mask & shift != 0:
          return -1
        
        mask |= shift
        val //= s[val]
      
      return mask
    
    @lru_cache(None)
    def dp(i, mask):
      if i >= n or mask == full_mask:
        return ones_combo if mask > 0 else (ones_combo-1)
      
      # if we don't add this number to the set
      c0 = dp(i+1, mask) 
      m0 = calc_mask(cand[i])
      
      # can't add this number
      if m0 < 0 or m0&mask > 0:
        return c0
      
      c1 = dp(i+1, mask|m0)
      cnt = c[cand[i]]
      # print(cand[i], c0, c1, bin(mask), bin(m0))
      
      return (c0 + cnt*c1) % mod
    
    return dp(0, 0)
    