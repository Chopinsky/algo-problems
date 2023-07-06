'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 105

Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
'''


from typing import List


class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    if not nums or sum(nums) < target:
      return 0
    
    if max(nums) >= target:
      return 1
    
    l, r = 0, 0
    s = 0
    n = len(nums)
    ln = n
    
    while r < n:
      s += nums[r]
      r += 1
      
      while r < n and s < target:
        s += nums[r]
        r += 1
        
      while l < r and s-nums[l] >= target:
        s -= nums[l]
        l += 1
        
      # print(l, r, s)
      if s >= target:
        ln = min(ln, r-l)
    
    return ln
        
        
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    if sum(nums) < target:
      return 0
    
    n = len(nums)
    size = n
    arr_sum = 0
    l, r = 0, 0
    
    while r < n:
      arr_sum += nums[r]
      r += 1
      
      while arr_sum >= target and l < r:
        size = min(size, r-l)
        arr_sum -= nums[l]
        l += 1
    
    return size
      
    