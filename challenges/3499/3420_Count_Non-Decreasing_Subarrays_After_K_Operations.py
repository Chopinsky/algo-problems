'''
3420. Count Non-Decreasing Subarrays After K Operations
'''

from typing import List
from collections import deque


class Solution:
  def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
    n = len(nums)
    nums = nums[::-1]
    count = 0
    i = 0
    q = deque()
    
    for j in range(n):
      val = nums[j]

      # popping all previous "markers" that
      # are lower
      while q and nums[q[-1]] < val:
        r = q.pop()
        l = q[-1] if q else i-1
        
        # ops required to make the range (l, r] 
        # raised to val 
        k -= (r-l)*(val-nums[r])

      q.append(j)

      # used too many ops, shift i such that
      # we can get k above negative value
      while k < 0:
        l = q[0]

        # no longer needs to raise nums[i] to
        # nums[l], take the ops back
        k += nums[l] - nums[i]
        if l == i:
          q.popleft()

        i += 1

      # all subarrays in [i, j] is legal
      count += j-i+1

    return count
        