'''
1574. Shortest Subarray to be Removed to Make Array Sorted

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.

Constraints:

1 <= arr.length <= 10^5
0 <= arr[i] <= 10^9
'''

from typing import List
from bisect import bisect_left


class Solution:
  def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    n = len(arr)
    idx = n-1
    while idx > 0 and arr[idx-1] <= arr[idx]:
      idx -= 1
      
    back = arr[idx:]
    m = len(back)
    removes = n-m
    prev = -1
    # print('back:', back)
    
    for i in range(idx):
      val = arr[i]
      if val < prev:
        break
        
      j = bisect_left(back, val)
      keep = (i+1) + (m-j)
      # print('iter:', (i, val, back[j:]), keep)
      removes = min(removes, n-keep)
      prev = val
    
    return removes
        
  def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    n = len(arr)
    l, r = 0, n-1
    
    while l < n-1 and arr[l] <= arr[l+1]:
      l += 1
      
    while r > 0 and arr[r] >= arr[r-1]:
      r -= 1
      
    # print(l, r)
    if l >= r:
      return 0
    
    if arr[l] <= arr[r]:
      return r-l-1
    
    ln = n-1
    j = r
    
    for i in range(l+1):
      while j < n and arr[i] > arr[j]:
        j += 1
        
      l0 = n - (i + 1) - (n - j)
      # print('prefix', arr[:i+1], arr[r+j:], l0)
      ln = min(ln, l0)
    
    j = 0
    for i in range(r, n):
      # j = bisect_right(arr[:l+1], arr[i])
      while j <= l and arr[j] <= arr[i]:
        j += 1
      
      l1 = n - (n - i) - j
      # print('suffix', arr[:j], arr[i:], l1)
      ln = min(ln, l1)

    return ln
  