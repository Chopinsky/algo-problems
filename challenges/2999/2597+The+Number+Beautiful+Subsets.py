'''
2597. The Number of Beautiful Subsets

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].
Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

Constraints:

1 <= nums.length <= 20
1 <= nums[i], k <= 1000
'''

from typing import List, Tuple
from functools import lru_cache

class Solution:
  def beautifulSubsets(self, nums: List[int], k: int) -> int:
    n = len(nums)
    if n == 1:
      return 1
    
    nums.sort()
    # print(nums)
    
    @lru_cache(None)
    def count(i: int, vals: Tuple[int]) -> int:
      if i >= n:
        return 0
      
      val = nums[i]
      is_valid = val-k not in vals
      
      if i == n-1:
        # print('end:', (i, val), is_valid, vals)
        return 1 if (i == 0 or is_valid) else 0
      
      # if not using number @ i
      c0 = count(i+1, vals)
      if not is_valid:
        return c0
      
      # if using number @ i
      c1 = count(i+1, vals + (val, )) + (1 if is_valid else 0)
      # print('iter:', (i, val), is_valid, c0, c1, vals)
      
      return c0 + c1
        
    return count(0, tuple())
        
  def beautifulSubsets(self, nums: List[int], k: int) -> int:
    n = len(nums)
    if n == 1:
      return 1
    
    pos = {val:i for i, val in enumerate(nums)}
    pairs = set()
    cnt = 0
    
    for i in range(n):
      val = nums[i]
      left = val-k
      right = val+k
      
      if left in pos:
        mask = (1 << i) | (1 << pos[left])
        pairs.add(mask)
      
      if right in pos:
        mask = (1 << i) | (1 << pos[right])
        pairs.add(mask)
    
    if not pairs:
      return (1<<n) - 1
      
    # print(pairs)
    for subset in range(1, (1<<n)):
      found = False
      for mask in pairs:
        if (subset & mask) == mask:
          found = True
          # print('..', subset, mask, subset&mask)
          break
          
      # print(subset, found)
      if not found:
        cnt += 1
    
    return cnt
    