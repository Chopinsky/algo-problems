'''
You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] describes the ith interval starting at lefti and ending at righti (inclusive). The size of an interval is defined as the number of integers it contains, or more formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the size of the smallest interval i such that lefti <= queries[j] <= righti. If no such interval exists, the answer is -1.

Return an array containing the answers to the queries.

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

Constraints:

1 <= intervals.length <= 10^5
1 <= queries.length <= 10^5
intervals[i].length == 2
1 <= lefti <= righti <= 10^7
1 <= queries[j] <= 10^7
'''


from typing import List
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import math


class Solution:
  def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    intervals.sort()
    idx = 0
    n = len(intervals)
    itvl_size = {}
    stack = []
    
    for val in sorted(queries):
      # better answer already visited
      if val in itvl_size: 
        continue

      # keep sweeping through the intervals to find
      # the minimum size, adding all valid intervals
      # while popping out intervals no longer valid
      while idx < n:
        l, r = intervals[idx]
        
        # out of the query bound
        if l > val:
          break
          
        # a valid interval found, push it into the stack
        if r >= val:
          heappush(stack, (r-l+1, r))

        # keep moving
        idx += 1
          
      # popping out all intervals that have moved out
      # of the current query bounds (as queries is 
      # mono-increasing)
      while stack and val > stack[0][1]: 
        heappop(stack)

      # answer to query x is the tip of the min-heap
      itvl_size[val] = stack[0][0] if stack else -1
        
    return [itvl_size[val] for val in queries]
      
      
  def minInterval0(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
    n = len(queries)
    ans = [-1] * n
    shifts = [-1] * n 
    
    q = sorted((val, i) for i, val in enumerate(queries))
    itvl = [(r-l+1, l, r) for l, r in intervals]
    itvl.sort()
    # print(q, itvl)
    
    for ln, l, r in itvl:
      ldx, rdx = bisect_left(q, (l, 0)), bisect_right(q, (r, math.inf))
      i = ldx
      # print('interval:', l, r, ln, ldx, rdx)
      
      while i < rdx:
        if shifts[i] < 0:
          # if this query has not been executed yet
          j = q[i][1]
          ans[j] = ln if ans[j] < 0 else min(ans[j], ln)
          nxt_idx = i + 1
        else:
          # if the query has been executed already, jump
          # to the next (presumably) un-executed one
          nxt_idx = shifts[i]
        
        shifts[i] = rdx
        i = nxt_idx
    
    return ans
  