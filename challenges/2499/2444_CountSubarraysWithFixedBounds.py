'''
2444. Count Subarrays With Fixed Bounds

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i], minK, maxK <= 10^6
'''

from bisect import bisect_left
from typing import List


class Solution:
  def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
    if minK > maxK:
      return 0
    
    a0, a1 = [], []
    last, cnt = 0, 0
    n = len(nums)
    
    def count(lower, upper, start, end) -> int:
      # print('count:', lower, upper, start)
      if not upper or not lower or start <= end-1:
        return 0
      
      total = 0
      for i in range(start, end):
        j = bisect_left(lower, i)
        k = bisect_left(upper, i)
        # print(i, j, k)
        
        if j >= len(lower) or k >= len(upper):
          break
          
        right = max(lower[j], upper[k])
        # print('right:', right)
        total += end - right
      
      return total
      
    for i in range(n):
      if nums[i] == minK:
        a0.append(i)
        
      if nums[i] == maxK:
        a1.append(i)
        
      if nums[i] < minK or nums[i] > maxK:
        cnt += count(a0, a1, last, i)
        last = i+1
        a0.clear()
        a1.clear()
        
    if a0 and a1:
      cnt += count(a0, a1, last, n)

    return cnt
    