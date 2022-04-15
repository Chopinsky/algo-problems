'''
Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

Example 1:

Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
Example 2:

Input: arr = [2,3,5], target = 10
Output: 5
Example 3:

Input: arr = [60864,25176,27249,21296,20204], target = 56803
Output: 11361
 

Constraints:

1 <= arr.length <= 104
1 <= arr[i], target <= 105
'''

from typing import List


class Solution:
  def findBestValue(self, arr: List[int], target: int) -> int:
    arr.sort()
    n = len(arr)
    prefix = [val for val in arr]
    
    for i in range(1, n):
      prefix[i] += prefix[i-1]
      
    if prefix[-1] <= target:
      return arr[-1]
    
    if arr[0] * n >= target:
      diff = arr[0]*n - target
      diff_val = arr[0]
      # print('low ball', diff, diff_val)
      
      val = target // n
      d0 = abs(val*n - target)
      # print('lb0', val, d0)
      
      if d0 <= diff:
        diff_val = val if d0 < diff else min(diff_val, val)
        diff = d0
        
      d1 = abs((val+1)*n - target)
      # print('lb1', val+1, d1)
      
      if d1 <= diff:
        diff_val = val+1 if d1 < diff else min(diff_val, val+1)
        diff = d1
      
      return diff_val
    
    diff = prefix[-1] - target
    diff_val = arr[-1]
    last = arr[-1]
    
    for i in range(n-2, -1, -1):
      if arr[i] == last:
        continue

      sums = prefix[i] + (n-i-1) * arr[i]
      d = abs(sums - target)
      if d <= diff:
        diff_val = arr[i]
        
      if sums < target:
        rem = target - prefix[i]
        val = rem // (n-i-1)
        # print('less', i, arr[i], val)
        
        if arr[i+1] >= val >= arr[i]:
          d0 = abs(prefix[i] + (n-i-1) * val - target)
          # print(val, d0)
          
          if d0 <= diff:
            diff_val = val if d0 < diff else min(diff_val, val)
            diff = d0
        
        if arr[i+1] >= val+1 >= arr[i]:
          d1 = abs(prefix[i] + (n-i-1) * (val+1) - target)
          # print(val+1, d1)
          
          if d1 <= diff:
            diff_val = val+1 if d1 < diff else min(diff_val, val+1)
            diff = d1
      
      last = arr[i]
        
    return diff_val
      