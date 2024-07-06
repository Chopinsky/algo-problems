'''
3209. Number of Subarrays With AND Value of K

Given an array of integers nums and an integer k, return the number of subarrays of nums where the bitwise AND of the elements of the subarray equals k.

Example 1:

Input: nums = [1,1,1], k = 1

Output: 6

Explanation:

All subarrays contain only 1's.

Example 2:

Input: nums = [1,1,2], k = 1

Output: 3

Explanation:

Subarrays having an AND value of 1 are: [1,1,2], [1,1,2], [1,1,2].

Example 3:

Input: nums = [1,2,3], k = 2

Output: 2

Explanation:

Subarrays having an AND value of 2 are: [1,2,3], [1,2,3].

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i], k <= 10^9

Test cases:

[1,1,1]
1
[1,1,2]
1
[1,2,3]
2
[1,9,9,7,4]
1
[2,1,2,4,0]
0
'''

from typing import List
from collections import defaultdict

class Solution:
  def countSubarrays(self, nums: List[int], k: int) -> int:
    n = len(nums)
    i0, i1 = 0, 0
    c0 = defaultdict(int)
    mask = 0
    cnt = 0
    
    def delta(dic, val, d):
      pos = 0
      while val > 0:
        if val & 1 == 1:
          dic[pos] += d
          
        val >>= 1
        pos += 1
      
    def shift():
      nonlocal i0, i1, mask
      
      if mask != k and mask&k == k:
        while i0+1 < n and mask&nums[i0+1]&k == k:
          i0 += 1
          mask &= nums[i0]
          delta(c0, nums[i0], 1)
          
          if mask == k:
            break
          
      if mask == k:
        i1 = max(i1, i0+1)
        while i1 < n and mask&nums[i1]&k == k:
          i1 += 1
      
    def init(i: int):
      nonlocal i0, i1, mask
      
      c0.clear()
      i0 = i
      mask = nums[i0]
      delta(c0, nums[i0], 1)
      shift()
          
    def update(i: int):
      nonlocal i0, i1, mask
      
      delta(c0, nums[i-1], -1)
      tgt = i0-i+1
      mask = 0
      
      for pos, pc in c0.items():
        if pc == tgt:
          mask |= (1<<pos)
          
      # print('update:', (i, i0), mask, c0)
      shift()
      
    for i in range(n):
      if i == 0 or i0 < i:
        init(i)
      else:
        update(i)
        
      # print('pos:', i, mask, (i0, i1), i1-i0)
      if mask == k:
        cnt += i1-i0
        # print('found:', (i, i0, i1), i1-i0)
    
    return cnt
  