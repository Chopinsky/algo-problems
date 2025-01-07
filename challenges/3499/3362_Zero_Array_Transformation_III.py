'''
3362. Zero Array Transformation III

[0,3]
[[0,1],[0,0],[0,1],[0,1],[0,0]]
[2,0,2]
[[0,2],[0,2],[1,1]]
[1,1,1,1]
[[1,3],[0,2],[1,3],[1,2]]
[1,2,3,4]
[[0,3]]
[0,0,1,1,0]
[[3,4],[0,2],[2,3]]
[1,2,2]
[[1,2],[1,1],[1,2],[0,1],[0,1],[0,2],[0,1],[0,0]]
'''

from typing import List
from heapq import heappush, heappop


class Solution:
  def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
    n, qn = len(nums), len(queries)
    i, j = 0, 0
    count = 0
    queries.sort(key=lambda x: (x[0], -x[1]))
    curr = 0
    stack = []
    cand = []
    
    while i < n:
      # print('check:', (i, j), curr, stack, cand)
      # pop any queries out of the range
      while stack and stack[0] < i:
        heappop(stack)
        curr -= 1
        
      # add all queries that matches the condition
      while j < qn and queries[j][0] <= i:
        heappush(cand, -queries[j][1])
        j += 1
        
      # take queries out of the cand
      while cand and curr < nums[i]:
        r = -heappop(cand)
        if r < i:
          continue
          
        heappush(stack, r)
        curr += 1
        count += 1
        
      # can't be done
      if curr < nums[i]:
        return -1
      
      i += 1
    
    return qn-count
  