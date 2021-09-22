'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''


class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    prod = 1
    n = len(nums)
    ans = [0] * n
    
    for i in range(0, n):
      ans[i] = prod
      prod *= nums[i]
      
    prod = 1
    for i in range(n-1, -1, -1):
      ans[i] *= prod
      prod *= nums[i]
    
    return ans
  
    
  def productExceptSelf0(self, nums: List[int]) -> List[int]:
    ans = [0] * len(nums)
    zero_count = 0
    total = 1
    
    for n in nums:
      if n == 0:
        zero_count += 1
        continue
        
      total *= n
      
    # print(total, zero_count)
    if zero_count > 1:
      return ans
    
    for i, n in enumerate(nums):
      if zero_count:
        if n == 0:
          ans[i] = total
          
      else:
        ans[i] = total // n
        
    return ans
  
