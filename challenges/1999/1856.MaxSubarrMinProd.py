'''
The min-product of an array is equal to the minimum value in the array multiplied by the array's sum.

For example, the array [3,2,5] (minimum value is 2) has a min-product of 2 * (3+2+5) = 2 * 10 = 20.
Given an array of integers nums, return the maximum min-product of any non-empty subarray of nums. Since the answer may be large, return it modulo 109 + 7.

Note that the min-product should be maximized before performing the modulo operation. Testcases are generated such that the maximum min-product without modulo will fit in a 64-bit signed integer.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,3,2]
Output: 14
Explanation: The maximum min-product is achieved with the subarray [2,3,2] (minimum value is 2).
2 * (2+3+2) = 2 * 7 = 14.
Example 2:

Input: nums = [2,3,3,1,2]
Output: 18
Explanation: The maximum min-product is achieved with the subarray [3,3] (minimum value is 3).
3 * (3+3) = 3 * 6 = 18.
Example 3:

Input: nums = [3,1,5,6,4,2]
Output: 60
Explanation: The maximum min-product is achieved with the subarray [5,6,4] (minimum value is 4).
4 * (5+6+4) = 4 * 15 = 60.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^7
'''


from typing import List


class Solution:
  def maxSumMinProduct(self, nums: List[int]) -> int:
    nums = [0] + nums + [0]
    prefix = [val for val in nums]
    
    for i in range(1, len(nums)):
      prefix[i] += prefix[i-1]
      
    stack = [0]
    res = 0
    
    for i, val in enumerate(nums[1:], 1):
      while val < nums[stack[-1]]:
        j = stack.pop()
        height = nums[j]
        sums = prefix[i-1] - prefix[stack[-1]]
        res = max(res, height * sums)

      stack.append(i)

    return res % (10**9 + 7)
      
      
  def maxSumMinProduct0(self, nums: List[int]) -> int:
    n = len(nums)
    bounds = [[i, i] for i in range(n)]
    prefix = [val for val in nums]
    stack = []
    
    for i in range(n):
      if i > 0:
        prefix[i] += prefix[i-1]
        
      if not stack:
        stack.append(i)
        bounds[i][0] = 0
        continue
        
      while stack and nums[i] <= nums[stack[-1]]:
        stack.pop()
        
      bounds[i][0] = min(i, 0 if not stack else stack[-1]+1)
      stack.append(i)
    
    # print(bounds)
    stack.clear()
    
    for i in range(n-1, -1, -1):
      if not stack:
        stack.append(i)
        bounds[i][1] = n-1
        continue
        
      while stack and nums[i] <= nums[stack[-1]]:
        stack.pop()

      # print(i, stack)
      bounds[i][1] = max(i, n-1 if not stack else stack[-1]-1)
      stack.append(i)
    
    # print(bounds)
    largest = 0
    
    for i, [l, r] in enumerate(bounds):
      sums = prefix[r] - (prefix[l-1] if l > 0 else 0)
      largest = max(largest, nums[i] * sums)
    
    return largest % (10**9 + 7)
  