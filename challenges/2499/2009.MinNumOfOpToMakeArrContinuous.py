'''
You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
'''

from bisect import bisect_left
from typing import List
from collections import deque


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
      return 0
    
    nums = sorted(set(nums))
    ops = n-1
    
    for i, val in enumerate(nums):
      # if val is the right bound
      left = val-n+1
      j = bisect_left(nums, left)
      cnt = i-j+1
      ops = min(ops, n-cnt)
      # print((i, val), ops)
      
      # if val is the left bound
      right = val+n
      j = bisect_left(nums, right) - 1
      cnt = j-i+1
      ops = min(ops, n-cnt)
      # print((i, val), ops)
      
      if ops == 0:
        break
    
    return ops
        

  def minOperations(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    count = n - 1
    stack = deque([])
    
    for val in nums:
      if not stack:
        stack.append(val)
        continue
        
      while stack and val-stack[0]+1 > n:
        stack.popleft()
        
      if not stack or val != stack[-1]:
        stack.append(val)
      
      if stack:
        count = min(count, n-len(stack))
    
    return count
  