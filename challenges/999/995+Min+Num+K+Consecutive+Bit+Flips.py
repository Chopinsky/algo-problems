'''
You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].

Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].

Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation: 
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]

Constraints:

1 <= nums.length <= 10^5
1 <= k <= nums.length
'''

from typing import List
from collections import deque

class Solution:
  def minKBitFlips(self, nums: List[int], k: int) -> int:
    if k == 1:
      return nums.count(0)
    
    n = len(nums)
    changes = [0]*n
    curr = 0
    ops = 0
    
    for i in range(n):
      curr += changes[i]
      val = nums[i]
      post_flips = val if curr%2 == 0 else 1-val
      
      if i+k > n:
        if post_flips == 0:
          return -1
        
        continue
      
      if post_flips == 0:
        ops += 1
        curr += 1
        if i+k < n:
          changes[i+k] -= 1
      
    return ops
  
  def minKBitFlips(self, nums: List[int], k: int) -> int:
    n = len(nums)
    presum = nums.copy()
        
    for i in range(1, n):
      presum[i] += presum[i-1]
    
    if k == 1:
      return n - presum[-1]
    
    if presum[-1] == n:
      return 0
    
    if presum[-1] == 0:
      return (n // k) if (n%k == 0) else -1
      
    if k == n:
      return 0 if (presum[-1] == n or presum[-1] == 0) else -1

    count = 0
    l = 0
    r = deque([])
    flip = 0
    
    while l < n:
      # print(l, r, flip)
      if not r and nums[l] == 1:
        l += 1
        continue
        
      while r and r[0][0] < l:
        r.popleft()
        
      # this coin has flipped the proper times and is now 1
      if (r and r[0][1] != flip and nums[l] == 0) or ((not r or r[0][1] == flip) and nums[l] == 1):
        l += 1
        continue
        
      # the current coin @l is 0, let's flip all k-coins in the range
      count += 1
      nxt_right = l + k - 1
      # print('flip at', l, r)

      # the 0-coin is in the range that can't be flipped to 1, fail
      if nxt_right >= n:
        # print('out', l, r, nxt_right)
        return -1
      
      r.append((nxt_right, flip))
      flip ^= 1
      l += 1
      
    return count  
