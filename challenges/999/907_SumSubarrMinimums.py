'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

Constraints:

1 <= arr.length <= 3 * 10^4
1 <= arr[i] <= 3 * 10^4
'''

from typing import List

class Solution:
  def sumSubarrayMins(self, arr: List[int]) -> int:
    stack = []
    lb, rb = [], []
    n = len(arr)
    mod = 10**9 + 7
    
    def update(i, bounds, dr):
      val = arr[i]
      while stack and val <= stack[-1][0]:
        if dr < 0 and val == stack[-1][0]:
          break
        
        stack.pop()
        
      head = 0 if dr == 1 else n-1
      bound = stack[-1][1]+dr if stack else head
      if stack and stack[-1][0] == val:
        stack.pop()
        
      stack.append((val, i))
      bounds.append(bound)
    
    for i in range(n):
      update(i, lb, 1)
      
    stack.clear()
    
    for i in range(n-1, -1, -1):
      update(i, rb, -1)
    
    rb = rb[::-1]
    sums = 0
    # print(lb, rb)
    
    for i in range(n):
      cnt = (i-lb[i]+1) * (rb[i]-i+1)
      # print('calc:', arr[i], cnt)
      sums = (sums + cnt * arr[i]) % mod
    
    return sums
  
  
  def sumSubarrayMins(self, arr: List[int]) -> int:
    mod = 10**9 + 7
    stack = [(-1, -1)]
    accum = []
    ans = 0
    
    for i, val in enumerate(arr):
      if val > stack[-1][0]:
        curr = val + (accum[-1] if accum else 0)
        
      else:
        while stack and stack[-1][0] >= val:
          stack.pop()
        
        last = stack[-1][1] if stack else -1
        curr = val * (i - last) + (accum[last] if last >= 0 else 0)
        
      stack.append((val, i))
      accum.append(curr)
      ans = (ans + curr) % mod
      
    return ans
      