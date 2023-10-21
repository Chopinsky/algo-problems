'''
Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

Example 1:

Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].

Example 2:

Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.

Example 3:

Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].

Constraints:

1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''


from collections import deque
from heapq import heappop, heappush
from typing import List


class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    ans = nums[0]
    stack = []
    
    for i in range(len(nums)):
      val = nums[i]
      while stack and i-stack[0][1] > k:
        heappop(stack)
        
      if stack:
        val -= stack[0][0]
        
      ans = max(ans, val)
      if val > 0:
        heappush(stack, (-val, i))
        
      # print((i, val), stack)
    
    return ans
        
        
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
    if all(n >= 0 for n in nums):
      return sum(nums)
    
    large = max(nums)
    q = deque([])
    
    for i, n in enumerate(nums):
      while q and q[0][1] < i-k:
        q.popleft()
        
      s = max(n, n + (q[0][0] if q else 0))
      large = max(large, s)
      
      while q and q[-1][0] < s:
        q.pop()
        
      q.append((s, i))

    return large
    
    
  def constrainedSubsetSum0(self, nums: List[int], k: int) -> int:
    q = []
    large = max(nums)
    
    for i, n in enumerate(nums):
      while q and q[0][1] < i-k:
        heappop(q)
      
      s = max(n, n - (q[0][0] if q else 0))
      large = max(large, s)
      
      heappush(q, (-s, i))
      
    return large
      