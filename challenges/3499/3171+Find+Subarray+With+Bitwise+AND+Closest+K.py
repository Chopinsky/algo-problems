'''
3171. Find Subarray With Bitwise AND Closest to K

You are given an array nums and an integer k. You need to find a subarray of nums such that the absolute difference between k and the bitwise AND of the subarray elements is as small as possible. In other words, select a subarray nums[l..r] such that |k - (nums[l] AND nums[l + 1] ... AND nums[r])| is minimum.

Return the minimum possible value of the absolute difference.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,2,4,5], k = 3

Output: 1

Explanation:

The subarray nums[2..3] has AND value 4, which gives the minimum absolute difference |3 - 4| = 1.

Example 2:

Input: nums = [1,2,1,2], k = 2

Output: 0

Explanation:

The subarray nums[1..1] has AND value 2, which gives the minimum absolute difference |2 - 2| = 0.

Example 3:

Input: nums = [1], k = 10

Output: 9

Explanation:

There is a single subarray with AND value 1, which gives the minimum absolute difference |10 - 1| = 9.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= 10^9

Test cases:

[1,2,4,5]
3
[1,2,1,2]
2
[1]
10
[1,10,6]
7
'''

from typing import List
from collections import defaultdict

class Solution:
  def minimumDifference(self, nums: List[int], k: int) -> int:
    diff = float('inf')
    n = len(nums)
    j = -1
    curr = 0
    store = defaultdict(int)
    
    def add(val: int):
      idx = 0
      
      while val > 0:
        if val & 1 > 0:
          store[idx] += 1
          
        val >>= 1
        idx += 1
    
    def remove(val: int, cnt: int):
      if cnt == 0:
        store.clear()
        return 0
      
      idx = 0
      while val > 0:
        if val & 1 > 0:
          store[idx] -= 1
          
        val >>= 1
        idx += 1
        
      result = 0
      for idx, c0 in store.items():
        if c0 == 0:
          continue
          
        if c0 == cnt:
          result |= (1 << idx)
        
      return result
    
    for i in range(n):
      # pop subarray left
      if i > 0:
        curr = remove(nums[i-1], max(0, j-i))
        
      # print('start:', (i, j), curr, store)
      
      # reset
      if j <= i:
        curr = nums[i]
        add(nums[i])
        j = i+1
        
      diff = min(diff, abs(curr-k))
      # print('pre:', (i, j), curr)
      
      while j < n and curr > k:
        curr &= nums[j]
        diff = min(diff, abs(curr-k))
        add(nums[j])
        j += 1
        
      # print('iter:', (i, j), curr)
      
      if diff == 0:
        break
    
    return diff
        