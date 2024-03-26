'''
41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1

Test cases:

[1,2,0]
[3,4,-1,1]
[7,8,9,11,12]
[2]
[0]
'''

import math
from typing import List

class Solution:
  def firstMissingPositive(self, nums: List[int]) -> int:
    small = math.inf
    for val in nums:
      if val > 0:
        small = min(val, small)
        
    if small > 1:
      return 1
    
    n = len(nums)
    
    def iterate(i: int):
      # print('iter:', i)
      val = nums[i]
      
      while val is not None and val > 0:
        # print('loop:', val, i)
        i = val-1
        if i >= n:
          break
          
        val = nums[i]
        nums[i] = None
    
    idx = 0
    while idx < n:
      if nums[idx] is None:
        idx += 1
        continue
      
      iterate(idx)
      idx += 1
      
    # print(nums)
    for i in range(n):
      if nums[i] is not None:
        return 1+i
    
    return 1+len(nums)
        