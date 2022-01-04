'''
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.

Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.
 

Constraints:

1 <= n <= 10^4
ranges.length == n + 1
0 <= ranges[i] <= 100
'''


from typing import List
from bisect import bisect_left


class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    ends = [0] * (n+1)
    for x, r in enumerate(ranges):
      l = max(0, x-r)
      ends[l] = max(ends[l], x+r)
      
    steps, start, end = 0, 0, 0
    while end < n:
      # jump from [start, end] to the next segment: [end+1, max(ends[start:end+1])]
      start, end = end+1, max(ends[start:end+1])
      
      # the furthest point we can jump from the previous [start:end]
      # won't be found with start = prev_end + 1, fail
      if start > end:
        return -1
      
      # we can make this jump
      steps += 1
      
    return steps
  
      
  def minTaps0(self, n: int, ranges: List[int]) -> int:
    start = []
    end = []
    
    for i, r in enumerate(ranges):
      if (not r) or (end and i+r <= end[-1]):
        continue
        
      if (not end) or (i-r >= end[-1]) or (i-r <= 0):
        if i-r <= 0:
          start.clear()
          end.clear()
          
        start.append(i-r)
        end.append(i+r)
        continue
        
      # while start and i-r <= start[-1]:
      #   start.pop()
      #   end.pop()
        
      idx = bisect_left(end, i-r)
      if idx < len(start)-1:
        start = start[:idx+1]
        end = end[:idx+1]
        
      if not end or end[-1] < n:
        start.append(i-r)
        end.append(i+r)
      
    # print(start, end)
    if not start or start[0] > 0 or end[-1] < n:
      return -1
    
    for i in range(1, len(start)):
      # if there's a gap, fail
      if start[i] > end[i-1]:
        return -1
      
    return len(start)
    