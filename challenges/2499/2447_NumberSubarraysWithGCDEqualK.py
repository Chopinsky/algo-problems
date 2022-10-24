'''
2447. Number of Subarrays With GCD Equal to K

Given an integer array nums and an integer k, return the number of subarrays of nums where the greatest common divisor of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The greatest common divisor of an array is the largest integer that evenly divides all the array elements.

Example 1:

Input: nums = [9,3,1,2,6,3], k = 3
Output: 4
Explanation: The subarrays of nums where 3 is the greatest common divisor of all the subarray's elements are:
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
- [9,3,1,2,6,3]
Example 2:

Input: nums = [4], k = 7
Output: 0
Explanation: There are no subarrays of nums where 7 is the greatest common divisor of all the subarray's elements.

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 10^9
'''

from math import gcd
from typing import List


class Solution:
  def subarrayGCD(self, nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    
    for i in range(n):
      curr_gcd = nums[i]
      for j in range(i, n):
        curr_gcd = gcd(curr_gcd, nums[j])
        if curr_gcd == k:
          # print(i, j)
          count += 1
          
        if curr_gcd < k:
          break
      
    return count
  