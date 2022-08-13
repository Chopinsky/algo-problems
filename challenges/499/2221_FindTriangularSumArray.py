'''
2221. Find Triangular Sum of an Array

You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as (nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.
Return the triangular sum of nums.

Example 1:

Input: nums = [1,2,3,4,5]
Output: 8
Explanation:
The above diagram depicts the process from which we obtain the triangular sum of the array.
Example 2:

Input: nums = [5]
Output: 5
Explanation:
Since there is only one element in nums, the triangular sum is the value of that element itself.

Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 9
'''

from typing import List


class Solution:
  def triangularSum(self, nums: List[int]) -> int:
    ans = 0
    n = len(nums)-1
    coeff = 1
    
    for i, val in enumerate(nums):
      ans = (ans + coeff * val) % 10
      
      # manually calculate comb(n, i), as it can be 
      # increamentally calculated from:
      #     comb(n, i) = comb(n, i-1) * (n-i) // (i+1)
      coeff *= (n - i)
      coeff //= (i+1)
      
    return ans
      
    
  def triangularSum0(self, nums: List[int]) -> int:
    nxt = []
    
    while len(nums) > 1:
      for i in range(1, len(nums)):
        nxt.append((nums[i-1] + nums[i]) % 10)
        
      nums, nxt = nxt, nums
      nxt.clear()
      
    return  nums[0]
  