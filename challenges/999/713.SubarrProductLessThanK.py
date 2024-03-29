'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
 

Constraints:

1 <= nums.length <= 3 * 10^4
1 <= nums[i] <= 1000
0 <= k <= 10^6
'''

from typing import List

class Solution:
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 0:
      return 0
    
    n = len(nums)
    count, j, prod = 0, 0, 1
    
    for i in range(n):
      if j < i:
        j = i
        prod = 1
      elif i > 0:
        prod //= nums[i-1]
        
      while j < n and prod*nums[j] < k:
        prod *= nums[j]
        j += 1
      
      count += j-i
      # print(i, j, prod)
      
    return count
    
  def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k == 0 or k <= min(nums):
      return 0
      
    l, r = 0, 0
    prod = nums[0]
    count = 0
    n = len(nums)
    
    while r < n:
      if prod >= k:
        if l == r:
          l, r = l+1, r+1
          prod = nums[l] if l < n else 0
        else:
          prod //= nums[l]
          l += 1
          
        continue
        
      count += r-l+1
      r += 1
      
      if r < n:
        prod *= nums[r]
        
    return count