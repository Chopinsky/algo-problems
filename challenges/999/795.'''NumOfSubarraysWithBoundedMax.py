'''
We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
Input: 
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

left, right, and nums[i] will be an integer in the range [0, 10 ** 9].
The length of nums will be in the range of [1, 50000].
'''

from typing import List

class Solution:
  def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
    # beginning index of the window
    start = 0
    # total count of subarrays
    count = 0
    # current count of left boundaries
    curr = 0
    
    for i, n in enumerate(nums):
      if left <= n <= right:
        # if the number is in the range, update the left positions that can be 
        # the start of the subarray
        curr = i - start + 1
        # add the count of all subarray from i-start+1 and ends at i
        count += curr
      elif n < left:
        # we will add extra subarrays within the range [i-start+1, i] 
        count += curr
      else:
        # reset the window left boundary, set the start to the next number (may 
        # or may not be in the range)
        start = i+1
        # reset the scores
        curr = 0
    
    return count
    
    
  def numSubarrayBoundedMax0(self, nums: List[int], left: int, right: int) -> int:
    count = 0
    stack = []
    
    def count_subarray(start: int, end: int) -> int:
      if start < 0 or len(stack) == 0:
        return 0
      
      cnt = 0
      size = len(stack)
      
      for i in range(size):
        l = stack[i]-stack[i-1] if i > 0 else stack[i]-start+1
        r = end-stack[i]
        # print(i, l, r)
        cnt += l*r
      
      return cnt
    
    start = -1
    
    for i, n in enumerate(nums):
      if n > right:
        count += count_subarray(start, i)
        start = -1
        stack.clear()
        
        continue
        
      if start < 0:
        start = i

      if n >= left:
        stack.append(i)
        
    count += count_subarray(start, len(nums))
    # print(stack, start, len(nums), count)
    
    return count
  