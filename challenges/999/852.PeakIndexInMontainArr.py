'''
852. Peak Index in a Mountain Array

An array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1

Constraints:

3 <= arr.length <= 10^5
0 <= arr[i] <= 10^6
arr is guaranteed to be a mountain array.
'''

from typing import List


class Solution:
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    n = len(arr)
    
    def check(idx: int) -> int:
      if arr[idx-1] < arr[idx] < arr[idx+1]:
        return 1
      
      if arr[idx-1] > arr[idx] > arr[idx+1]:
        return -1
      
      return 0
    
    l, r = 1, n-2
    while l <= r:
      mid = (l + r) // 2
      res = check(mid)
      # print((l, r), mid, res)
      
      if res == 0:
        return mid
      
      if res > 0:
        l = mid + 1
      else:
        r = mid - 1
      
    return l
    
    
  def peakIndexInMountainArray(self, arr: List[int]) -> int:
    n = len(arr)
    
    def check(idx: int) -> int:
      if idx == 0 or idx == n-1 or (arr[idx-1] < arr[idx] and arr[idx+1] < arr[idx]):
        return 0
      
      if arr[idx-1] <= arr[idx] <= arr[idx+1]:
        return 1
      
      return -1
    
    l, r = 0, n
    
    while l <= r:
      mid = (l + r) // 2
      res = check(mid)
      # print(mid, res)
      
      if res == 0:
        return mid
      
      if res < 0:
        r = mid
      else:
        l = mid
      
    return l
  