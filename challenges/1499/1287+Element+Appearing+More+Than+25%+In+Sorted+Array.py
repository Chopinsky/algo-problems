'''
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
'''

from typing import List
from math import ceil


class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    n = len(arr)
    tgt = ceil(n/4) + (1 if n%4 == 0 else 0)
    # print(n, tgt)
    
    for i in range(n):
      j = i + tgt - 1
      if j >= n:
        break
        
      if arr[i] == arr[j]:
        return arr[i]
      
    return -1
        