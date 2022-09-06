'''
6169. Longest Nice Subarray

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.

Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from typing import List
from functools import lru_cache


class Solution:
  def longestNiceSubarray(self, nums: List[int]) -> int:
    start = 0
    long = 1
    curr = {}
    
    @lru_cache(None)
    def get_ones(val: int):
      lst = []
      idx = 0
      
      while val > 0:
        if val & 1 == 1:
          lst.append(idx)
          
        idx += 1
        val >>= 1
        
      return lst
        
    for i, val in enumerate(nums):
      for d in get_ones(val):
        if d in curr:
          start = max(start, curr[d]+1)
          
        curr[d] = i
        
      long = max(long, i-start+1)
    
    return long
    