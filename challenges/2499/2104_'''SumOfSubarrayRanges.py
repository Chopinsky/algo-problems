'''
You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.

Return the sum of all subarray ranges of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0 
[2], range = 2 - 2 = 0
[3], range = 3 - 3 = 0
[1,2], range = 2 - 1 = 1
[2,3], range = 3 - 2 = 1
[1,2,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
Example 2:

Input: nums = [1,3,3]
Output: 4
Explanation: The 6 subarrays of nums are the following:
[1], range = largest - smallest = 1 - 1 = 0
[3], range = 3 - 3 = 0
[3], range = 3 - 3 = 0
[1,3], range = 3 - 1 = 2
[3,3], range = 3 - 3 = 0
[1,3,3], range = 3 - 1 = 2
So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.
Example 3:

Input: nums = [4,-2,-3,4,1]
Output: 59
Explanation: The sum of all subarray ranges of nums is 59.

Constraints:

1 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9

Follow-up: Could you find a solution with O(n) time complexity?
'''

from typing import List
import math


class Solution:
  def subArrayRanges(self, nums: List[int]) -> int:
    result = 0
    stack = []
    values = [math.inf] + nums + [math.inf]

    # monotonic decrease, make the "+ <largest number>" part
    for i in range(len(values)):
      while stack and values[i] > values[stack[-1]]:
        j = stack.pop()
        result += values[j] * (i-j) * (j-stack[-1]) # val * width * height

      stack.append(i)

    stack = []
    values = [-math.inf] + nums + [-math.inf]

    # monotonic increase, make the "- <smallest number>" part
    for i in range(len(values)):
      while stack and values[i] < values[stack[-1]]:
        j = stack.pop()
        result -= values[j] * (i-j) * (j-stack[-1]) # val * width * height

      stack.append(i)

    # result is the combination of the "large - small" for 
    # all subarrays
    return result
  
  
  def subArrayRanges0(self, nums: List[int]) -> int:
    sums = 0
    n = len(nums)
    
    for i in range(n-1):
      s, l = nums[i], nums[i]
      for j in range(i+1, n):
        s = min(s, nums[j])
        l = max(l, nums[j])
        sums += l - s
    
    return sums
  