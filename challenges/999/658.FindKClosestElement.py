'''
Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
arr is sorted in ascending order.
-104 <= arr[i], x <= 104
'''


from typing import List
from bisect import bisect_left, bisect_right


class Solution:
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    n = len(arr)
    if k >= n:
      return arr
    
    l = bisect_right(arr, x)-1
    r = l+1
    ans = []
    # print(l, r, arr[l])
    
    while len(ans) < k:
      if l < 0:
        ans.append(arr[r])
        r += 1
        continue
        
      if r >= n:
        ans.append(arr[l])
        l -= 1
        continue
        
      if x-arr[l] <= arr[r]-x:
        ans.append(arr[l])
        l -= 1
      else:
        ans.append(arr[r])
        r += 1
    
    ans.sort()
    return ans


  '''
  idea is to find the left bound for the window, where we can run a binary search to 
  quickly locate. The initial left bound's range must fall in the [0, len(arr)-k-1],
  then if x is out of the [mid, mid+k] range, we move the window (i.e. the left bound)
  accordingly; otherwise, we check if the left bound is closer to x than the right bound, 
  if so we can move the window to the left, and if not, we can move the window to the
  right, until hi == lo.
  '''
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    # range of lo must be in [0, len(arr)-k-1]
    lo = 0
    hi = len(arr)-k-1
    
    while lo <= hi:
      mid = (lo + hi) // 2
      front = arr[mid]
      end = arr[mid+k]
      
      if x < front:
        # x is smaller than the beginning of the window, move left
        hi = mid - 1
      elif x >= end:
        # x is greater or equal to the end of the window, move right
        lo = mid + 1
      else:
        if abs(x-front) <= abs(end-x):
          # we should move the window to the left
          hi = mid - 1
        else:
          # we should move the window to the right
          lo = mid + 1
          
    return arr[lo:lo+k]
    
    
  def findClosestElements1(self, arr: List[int], k: int, x: int) -> List[int]:
    if k == len(arr):
      return arr
    
    if x <= arr[0]:
      return arr[:k]
    
    if x >= arr[-1]:
      return arr[-k:]
    
    l = bisect_left(arr, x)
    if l > 0 and abs(arr[l-1]-x) <= abs(arr[l]-x):
      l -= 1
    
    # print(l, arr[l])
    r = l
    n = len(arr)
    
    while r-l+1 < k:
      if l == 0:
        r += 1
        continue
        
      if r == n-1:
        l -= 1
        continue
        
      if abs(arr[l-1]-x) <= abs(arr[r+1]-x):
        l -= 1
      else:
        r += 1
    
    # print(l, r, arr[l:r+1])
    
    return arr[l:r+1]
    