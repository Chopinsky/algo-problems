'''
Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

Example 1:

Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
Output: [1,0,0,0,0]
Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
Example 2:

Input: arr1 = [0], arr2 = [0]
Output: [0]
Example 3:

Input: arr1 = [0], arr2 = [1]
Output: [1]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
arr1[i] and arr2[i] are 0 or 1
arr1 and arr2 have no leading zeros
'''

from typing import List


class Solution:
  def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
    if len(arr1) < len(arr2):
      arr1, arr2 = arr2, arr1
      
    co = 0
    n1, n2 = len(arr1), len(arr2)
    
    for i in range(1, n1+1):
      arr1[n1-i] += (arr2[n2-i] if i <= n2 else 0) + co
      
      if arr1[n1-i] >= 2:
        arr1[n1-i] -= 2
        co = -1
      elif arr1[n1-i] < 0:
        arr1[n1-i] = 1
        co = 1
      else:
        co = 0
        
      # print(i, arr1[n1-i], co)
    
    if co == 1:
      arr1 = [1] + arr1
    
    if co == -1:
      arr1 = [1, 1] + arr1
    
    idx = 0
    while idx < len(arr1)-1 and arr1[idx] == 0:
      idx += 1
      
    return arr1[idx:]
    