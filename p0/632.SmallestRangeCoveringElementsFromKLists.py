'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]

Example 3:

Input: nums = [[10,10],[11,11]]
Output: [10,11]

Example 4:

Input: nums = [[10],[11]]
Output: [10,11]

Example 5:

Input: nums = [[1],[2],[3],[4],[5],[6],[7]]
Output: [1,7]

Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.
'''

from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List

class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    lookup = defaultdict(set)
    k = len(nums)
    
    for i, arr in enumerate(nums):
      for num in arr:
        lookup[num].add(i)
        
    scan = sorted(lookup.items())
    # print(scan)
    
    best_size = float('inf')
    win = [float('-inf'), float('inf')]
    
    counts = [0] * k
    list_count = 0
    start, end = 0, 0
    
    while list_count == k or end < len(scan):
      # shrink the window until one array is completely out of the window
      while list_count == k:
        curr_size = scan[end-1][0] - scan[start][0]
        
        # update the best window before shrink, because currently we have
        # all array's numbers present in this window
        if curr_size < best_size or (curr_size == best_size and scan[start][0] < win[0]):
          best_size = curr_size
          win[0] = scan[start][0]
          win[1] = scan[end-1][0]
          
        # now, take the lists and remove the arrays from the window
        num, lists = scan[start]
        
        # actually shrink the window by removing `num` from the window
        for i in lists:
          # since `num` is in this array, remove it
          counts[i] -= 1
          
          # if all numbers in this array are out of the window, remove it
          # from the total tally
          if not counts[i]:
            list_count -= 1
            
        # the number is removed, update the window left bound
        start += 1
        
      # now expand the window until all array are present in the window
      while list_count < k and end < len(scan):
        # adding the arrays into the window
        num, lists = scan[end]
        for i in lists:
          # add the array into the window, if it's not yet in the window,
          # increament the total tally by 1
          if not counts[i]:
            list_count += 1
            
          counts[i] += 1
          
        # now this number is included in the window, update the upper bound
        end += 1
      
    return win
  
  
  def smallestRange0(self, nums: List[List[int]]) -> List[int]:
    k = len(nums)
    if k == 1:
      return [nums[0][0], nums[0][0]]
    
    low = nums[0][0]
    for arr in nums:
      if arr[0] < low:
        low = arr[0]
        
    sq = []
    win_left = low
    win_right = low
    
    # print(low)
    # print(sq)
    
    for i, arr in enumerate(nums):
      j = bisect_left(arr, low)
      heappush(sq, (arr[j], i))
      
      if arr[j] > win_right:
        win_right = arr[j]
    
    # print(win_left, win_right)
    # print('=====')
    
    ans = [win_left, win_right]
    print(ans)
    
    while len(sq) >= k:
      val, i = heappop(sq)
      arr = nums[i]
      
      if val == arr[-1]:
        break
        
      j = bisect_right(arr, val)
      if j >= len(arr):
        # print('done:', arr, val, i)
        break
      
      next_val = arr[j]
      heappush(sq, (next_val, i))
      
      win_left = sq[0][0]
      win_right = max(win_right, next_val)
      
      if win_right - win_left < ans[1] - ans[0]:
        ans[0] = win_left
        ans[1] = win_right
        print(ans)
        
      if win_left == win_right:
        return ans
    
    return ans
