'''
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums​​​, return the minimum number of elements to remove to make nums​​​ a mountain array.

Example 1:

Input: nums = [1,3,1]
Output: 0
Explanation: The array itself is a mountain array so we do not need to remove any elements.
Example 2:

Input: nums = [2,1,1,5,6,2,3,1]
Output: 3
Explanation: One solution is to remove the elements at indices 0, 1, and 5, making the array nums = [1,5,6,3,1].
 

Constraints:

3 <= nums.length <= 1000
1 <= nums[i] <= 10^9
It is guaranteed that you can make a mountain array out of nums.
'''


from typing import List
from bisect import bisect_left


class Solution:
  def minimumMountainRemovals(self, nums: List[int]) -> int:
    n = len(nums)
    
    def build(src: List[int]) -> List[int]:
      stack = []
      res = []
      
      for i in range(n):
        if not stack or src[i] > stack[-1]:
          res.append(len(stack)+1)
          stack.append(src[i])
          continue

        idx = bisect_left(stack, src[i])
        # print(stack, src[i], idx)
        stack[idx] = src[i]
        res.append(idx+1)
        
      return res

    rise = build(nums)
    nums.reverse()
    fall = build(nums)
    fall.reverse()
    # print(rise, fall)
    
    # if using i-th number as the peak
    long = 1
    
    for i in range(1, n-1):
      if rise[i] == 1 or fall[i] == 1:
        continue
        
      long = max(long, rise[i]+fall[i]-1)
    
    '''
    rise, fall = [1]*n, [1]*n
    seen = set()
    
    for i in range(1, n):
      seen.clear()
      for j in range(i-1, -1, -1):
        if j+2 <= rise[i]:
          break
          
        if nums[j] >= nums[i] or nums[j] in seen:
          continue
          
        seen.add(nums[j])
        rise[i] = max(rise[i], rise[j]+1)
        
    for i in range(n-2, -1, -1):
      seen.clear()
      for j in range(i+1, n):
        if n-j+1 <= fall[i]:
          break
          
        if nums[j] >= nums[i] or nums[j] in seen:
          continue
          
        seen.add(nums[j])
        fall[i] = max(fall[i], fall[j]+1)
    '''
    
    # print(long)
    return n - long
  