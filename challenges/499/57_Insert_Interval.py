'''
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5

Test cases:

[[1,5]]
[6,8]

[[1,5]]
[0,0]

[[3,8],[9,11]]
[3,7]

[[0,3],[5,8],[9,11]]
[9,18]

[[1,1],[2,10]]
[5,13]

[[2,3],[5,5],[6,6],[7,7],[8,11]]
[6,13]

[[1,1],[2,10]]
[5,13]

[[0,2],[4,6],[10,11],[14,15],[18,20],[26,26],[31,31],[35,42],[43,47],[49,52]]
[59,62]
'''

from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], insert: List[int]) -> List[List[int]]:
    if not intervals or insert[1] < intervals[0][0]:
      return [insert] + intervals
    
    ans = []
    inserted = False
    
    for x, y in intervals:
      if inserted or y < insert[0]:
        ans.append((x, y))
        continue
      
      if x > insert[1]:
        ans.append(insert)
        ans.append((x, y))
        inserted = True
        continue
      
      insert[0] = min(insert[0], x)
      insert[1] = max(insert[1], y)
    
    if not inserted:
      ans.append(insert)
      
    return ans
        
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    result = []
    s0, e0 = newInterval
    added = False
    
    for s, e in intervals:
      if e < s0:
        result.append((s, e))
        continue
        
      if s > e0:
        if not added:
          result.append((s0, e0))
          added = True
          
        result.append((s, e))
        continue
        
      s0 = min(s0, s)
      e0 = max(e0, e)
      
    if not added:
      result.append((s0, e0))
    
    return result
    
