

'''
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

Constraints:

3 <= mountain_arr.length() <= 10^4
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
'''

from functools import lru_cache
from typing import List


# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
  def __init__(self, arr: List[int]):
    self.arr = arr

  def get(self, index: int) -> int:
    if index < 0 or index >= len(self.arr):
      raise 'index error'
    
    return self.arr[index]

  def length(self) -> int:
    return len(self.arr)
  

class Solution:
  def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
    n = arr.length()
    
    @lru_cache(None)
    def get(i: int):
      return arr.get(i)
    
    def is_peak(i: int):
      v0 = get(i-1)
      v1 = get(i)
      v2 = get(i+1)
      
      if v0 < v1 < v2:
        return -1
      
      if v0 > v1 > v2:
        return 1
      
      return 0
      
    def find_peak():
      l, r = 1, n-1
      
      while l <= r:
        mid = (l + r) // 2
        res = is_peak(mid)
        
        if res == 0:
          return mid
        
        if res < 0:
          l = mid+1
        else:
          r = mid-1
          
      return l
    
    def search_left(pdx: int):
      l, r = 0, pdx
      while l <= r:
        mid = (l + r) // 2
        val = get(mid)
        
        if val == target:
          return mid
        
        if val < target:
          l = mid+1
        else:
          r = mid-1
        
      return l if l >= 0 and get(l) == target else -1
    
    def search_right(pdx: int):
      l, r = pdx, n-1
      while l <= r:
        mid = (l + r) // 2
        val = get(mid)
        
        if val == target:
          return mid
        
        if val < target:
          r = mid-1
        else:
          l = mid+1
          
      # print('right:', l, n)
      return l if l < n and get(l) == target else -1
      
    pdx = find_peak()
    # print('peak:', pdx, get(pdx))
    
    jdx = search_left(pdx)
    # print('left', jdx)
    
    if jdx >= 0:
      return jdx
    
    return search_right(pdx)
        