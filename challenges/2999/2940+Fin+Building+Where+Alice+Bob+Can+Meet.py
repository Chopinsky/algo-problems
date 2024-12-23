'''
2940. Find Building Where Alice and Bob Can Meet

You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.

If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].

You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.

Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.

 

Example 1:

Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
Output: [2,5,-1,5,2]
Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2]. 
In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5]. 
In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
In the fifth query, Alice and Bob are already in the same building.  
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
Example 2:

Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
Output: [7,6,-1,4,6]
Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.

Constraints:

1 <= heights.length <= 5 * 10^4
1 <= heights[i] <= 10^9
1 <= queries.length <= 5 * 10^4
queries[i] = [ai, bi]
0 <= ai, bi <= heights.length - 1
'''

from typing import List
from heapq import heappop, heappush
from bisect import bisect_left


class Solution:
  def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
    ans = [-1]*len(queries)
    max_h = max(heights)
    q = sorted([(min(query), max(query), i) for i, query in enumerate(queries)], key=lambda x: -x[1])
    h_stack = []
    h_index = []
    jdx = len(heights)-1
    
    for a, b, idx in q:
      while jdx > b:
        h = heights[jdx]
        while h_stack and -h_stack[-1] <= h:
          h_stack.pop()
          h_index.pop()
        
        h_stack.append(-h)
        h_index.append(jdx)
        jdx -= 1
      
      # print('q:', (a, b), idx)
      # print('state:', h_stack, h_index)
      
      if a == b:
        ans[idx] = a
        continue
        
      ha = heights[a]
      hb = heights[b]
      
      # can just go to b
      if hb > ha:
        ans[idx] = b
        continue
        
      # no way
      if not h_stack or ha >= -h_stack[0]:
        continue
        
      # find the way
      kdx = bisect_left(h_stack, -ha)-1
      if kdx >= 0:
        ans[idx] = h_index[kdx]
    
    return ans
        
  def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
    q = [[] for _ in heights]
    h = []
    ans = [-1]*len(queries)
    
    def cmp(a, b):
      if a == b:
        return 0
      
      return 1 if a > b else -1

    for qdx, (i, j) in enumerate(queries):
      # able to meet at the right most index
      if cmp(i, j) == cmp(heights[i], heights[j]):
        # print('set:', qdx, (i, j))
        ans[qdx] = max(i, j)
        continue
        
      # prepare for query
      # print('append:', qdx)
      q[max(i, j)].append((max(heights[i], heights[j]), qdx))
      
    for i, height in enumerate(heights):
      # get all the queries where the meet point is i
      while h and h[0][0] < height:
        _, qdx = heappop(h)
        ans[qdx] = i
        
      # add queries that become available
      for query in q[i]:
        heappush(h, query)
        # print('add:', query)
    
    return ans
        