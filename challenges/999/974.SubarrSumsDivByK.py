'''
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
Example 2:

Input: nums = [5], k = 9
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
2 <= k <= 10^4
'''


from typing import List
from collections import defaultdict


class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    store = defaultdict(int)
    store[0] += 1
    prefix_sum = 0
    count = 0
    
    for val in nums:
      prefix_sum += val
      mod = prefix_sum % k
      count += store[mod]
      store[mod] += 1
      
    return count
    
    
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    prefix = 0
    mod_counter = defaultdict(int)
    count = 0
    
    for val in nums:
      prefix += val
      mod = prefix % k
      if mod == 0:
        count += 1
      
      if mod in mod_counter:
        # print(val, prefix, mod, mod_counter)
        count += mod_counter[mod]
        
      mod_counter[mod] += 1
      
    return count
  