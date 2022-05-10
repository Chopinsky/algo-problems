'''
Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.

Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:

Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 

Constraints:

3 <= arr.length <= 5 * 10^4
-10^4 <= arr[i] <= 10^4
'''

from typing import List
from collections import defaultdict


class Solution:
  def canThreePartsEqualSum(self, arr: List[int]) -> bool:
    suffix = [val for val in arr]
    n = len(arr)
    
    for i in range(n-2, -1, -1):
      suffix[i] += suffix[i+1]
      
    left = 0
    svals = defaultdict(int)
    for i in range(n):
      svals[suffix[i]] += 1
    
    for i in range(n-2):
      left += arr[i]
      svals[suffix[i]] -= 1
      r0 = suffix[i+1]
      
      if r0 == 0 and left == 0 and svals[r0] > 1:
        return True
      
      if r0 % 2 == 0 and svals[r0 // 2] > 0 and left == r0//2:
        # print(i)
        if r0 != 0:
          return True
        
        if svals[r0] > 1:
          return True
    
    return False
  