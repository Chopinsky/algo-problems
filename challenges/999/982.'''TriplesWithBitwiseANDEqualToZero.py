'''
Given an integer array nums, return the number of AND triples.

An AND triple is a triple of indices (i, j, k) such that:

0 <= i < nums.length
0 <= j < nums.length
0 <= k < nums.length
nums[i] & nums[j] & nums[k] == 0, where & represents the bitwise-AND operator.
 

Example 1:

Input: nums = [2,1,3]
Output: 12
Explanation: We could choose the following i, j, k triples:
(i=0, j=0, k=1) : 2 & 2 & 1
(i=0, j=1, k=0) : 2 & 1 & 2
(i=0, j=1, k=1) : 2 & 1 & 1
(i=0, j=1, k=2) : 2 & 1 & 3
(i=0, j=2, k=1) : 2 & 3 & 1
(i=1, j=0, k=0) : 1 & 2 & 2
(i=1, j=0, k=1) : 1 & 2 & 1
(i=1, j=0, k=2) : 1 & 2 & 3
(i=1, j=1, k=0) : 1 & 1 & 2
(i=1, j=2, k=0) : 1 & 3 & 2
(i=2, j=0, k=1) : 3 & 2 & 1
(i=2, j=1, k=0) : 3 & 1 & 2
Example 2:

Input: nums = [0,0,0]
Output: 27
 

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] < 2^16
'''


from typing import List
from collections import defaultdict


class Solution:
  def countTriplets0(self, nums: List[int]) -> int:
    tuples = defaultdict(int)
    
    for a in nums:
      for b in nums:
        tuples[a&b] += 1
        
    count = 0
    for a in nums:
      for t in tuples:
        if t & a == 0:
          count += tuples[t]
          
    return count
  
  
  def countTriplets(self, nums: List[int]) -> int:
    counter = [0] * (1<<16)
    counter[0] = len(nums)
    max_mask = (1<<16) - 1
    
    # get all the complementary numbers `s` to `val`, such 
    # that `val & s == 0`, and we add 1 count under this 
    # compementary number `s`.
    for val in nums:
      # print(val, format(val, '010b'))
      base = val ^ max_mask 
      s = base
      
      # enumerate all the complementary numbers from `base`, 
      # such that `s & val == 0` because `base & val == 0`, and
      # `s` are enumeration of the base where the binary digit is 1
      while s > 0:
        counter[s] += 1
        s = (s-1) & base

    # for all tuples (n1, n2), we just count the number of
    # `val`s that will make `val & (n1 & n2) == 0`.
    total = 0
    for n1 in nums:
      for n2 in nums:
        total += counter[n1&n2]
        
    return total
  