'''
2470. Number of Subarrays With LCM Equal to K

Given an integer array nums and an integer k, return the number of subarrays of nums where the least common multiple of the subarray's elements is k.

A subarray is a contiguous non-empty sequence of elements within an array.

The least common multiple of an array is the smallest positive integer that is divisible by all the array elements.

Example 1:

Input: nums = [3,6,2,7,1], k = 6
Output: 4
Explanation: The subarrays of nums where 6 is the least common multiple of all the subarray's elements are:
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
- [3,6,2,7,1]
Example 2:

Input: nums = [3], k = 2
Output: 0
Explanation: There are no subarrays of nums where 2 is the least common multiple of all the subarray's elements.
 
Constraints:

1 <= nums.length <= 1000
1 <= nums[i], k <= 1000

Test cases:

[9,24]
72

[2,1,1,5]
5

[2,3]
6
'''

from typing import List
from math import gcd


class Solution:
  def subarrayLCM(self, nums: List[int], k: int) -> int:
    count = 0
    
    for i in range(len(nums)):
      lcm = nums[i]
      for j in range(i, len(nums)):
        if nums[j] > k or lcm > k or k % nums[j] != 0:
          break

        lcm = (nums[j] * lcm) // gcd(nums[j], lcm)
        # print(i, j, lcm)

        if lcm == k:
          count += 1
    
    return count
    
    